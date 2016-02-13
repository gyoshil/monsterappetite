///////////////////////////////// Server only logic ///////////////////////////////////

Meteor.methods ({

  start_new_game: function (player_id) {
    // TIME GIVEN FOR PLAYERS to CHOOSE FOOD ITEMS

    // create a new game w/ no rounds and a blank board
    var game_id = Games.insert({rounds: []});

    // move everyone who is ready in the lobby to the game
    //Players.update({game_id: null, idle: false, name: {$ne: ''}},
    //console.log("assigning players to new game");
    //console.log(Players.findOne(player_id).game_id );
    Players.update({_id:player_id},
                   {$set: {game_id: game_id}});
                   //{multi: true});
    //console.log(Players.findOne(player_id).game_id );

    // Save a record of who is in the game, so when they leave we can
    // still show them.

    var p = Players.find({game_id: game_id},
                         {fields: {_id: true, name: true}}).fetch();
    var p_game_data = p.map(function(one_p,i,l){
      return {_id:one_p._id, name:one_p.name, card_set:[]}
    })
    //TODO add card_set to players, then add to game
    Games.update({_id: game_id}, {$set: {players: p_game_data}});

    //debug lines
    //var pl = Games.findOne({_id: game_id});
    //console.error("starting game with...\n "+JSON.stringify(pl,null,4));
    //console.error(pl.rounds[pl.rounds.length-1][0]);

    //execute_round(game_id);
    //console.log(Players.findOne(player_id).game_id );
    return game_id;
  },
  //this must be the part that keeps or chaches the players to show multiple players
  //does this also keep the same player_id alive after the game session has ended???
  keepalive: function (player_id) {
    check(player_id, String);
    Players.update({_id: player_id},
                  {$set: {last_keepalive: (new Date()).getTime(),
                          idle: false}});
  },
  killuser: function (player_id) {
    check(player_id, String);
    Players.update({_id: player_id},
                  {$set: {idle: true}});
  },

  new_round: function(player,game_id) {

    var g = Games.findOne(game_id);
    //console.log(g);
    //play up to n rounds
    if (g.rounds.length < roundsPerGame ) {
      new_round_set = g.rounds;//.push() returns new length
      new_round_set.push(new_board());
      Games.update({_id: game_id},
                   {$set: {rounds: new_round_set}});
      execute_round(player,game_id);
    }

    else{//when all the rounds are over... kill the player?
      console.error("finsihed the game, but no code here");
      Players.update(player._id, {$set: {game_id: null, round_id:null}});
    }

  }
});


execute_round = function(player,game_id) {


  // wind down the game CLOCK
  var clock = 20;
  Games.update({_id: game_id}, {$set: {clock: clock}});
  var thisRoundNum = Games.findOne({_id: game_id}).rounds.length
  var interval = Meteor.setInterval(function () {
    Games.update({_id: game_id}, {$set: {clock: clock}});
    //every round, check to see if the player has a new round number
    var g = Games.findOne({_id: game_id})
    // end of game
    if (clock === 0 || g.rounds.length > thisRoundNum) {
      // stop the clock
      Meteor.clearInterval(interval);
      //when the clock stops, record the players performance data for easy retrival later
      var actual_score = 0;//this needs to be actual score ONLY for a single round
      var addScores = function(e,i,l) {
        actual_score += e.calories;
      };
      var matchesP = function(e,i,l){
        return (e._id == player._id);
      };
      g = Games.findOne({_id : game_id});
      var card_set = g.players.find(matchesP).card_set;
      //console.log(card_set);
      /*while ( g.players.find(matchesP).card_set.length%3!=0) {
        console.log("added");
        var blank_card = {card_name:"Nothing",calories:0}
        g.players.find(matchesP).card_set.push(blank_card);
      }*/
      card_set.forEach(addScores);

      r = Games.findOne({_id: game_id}).rounds;
      
     /* var perRoundCalories = 0
      var addPerRoundCalories = function () {
        perRoundCalories = calories //?????????????????????
      }*/
      
      //TODO: this is where we're doing a bit of data crunching to make analysis later on
      //below:accumulative,        lowest,                               highest  
      perf = [actual_score,        lowest_possible_score(r[r.length-1]), highest_possible_score(r[r.length-1])];

      Players.update({_id:player._id}, {$push: {performance:perf}});

      // declare zero or more winners

    };
    clock -= 1;
  }, 1000);

}

  Meteor.setInterval(function () {
  var now = (new Date()).getTime();
  var idle_threshold = now - 10*1000;

  Players.update({last_keepalive: {$lt: idle_threshold}},
                 {$set: {idle: true}});

}, 10*1000);
