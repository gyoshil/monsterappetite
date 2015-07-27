////////// Server only logic //////////

Meteor.methods ({

  start_new_game: function () {
    // TIME GIVEN FOR PLAYERS to CHOOSE FOOD ITEMS
    var timeGiven=7;

    // create a new game w/ fresh board
    var game_id = Games.insert({board: new_board(),
                                clock: timeGiven});

    // move everyone who is ready in the lobby to the game
    Players.update({game_id: null, idle: false, name: {$ne: ''}},
                   {$set: {game_id: game_id}},
                   {multi: true});
    // Save a record of who is in the game, so when they leave we can
    // still show them.
    var p = Players.find({game_id: game_id},
                         {fields: {_id: true, name: true}}).fetch();
    Games.update({_id: game_id}, {$set: {players: p}});
    
    execute_round(game_id);

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

  new_round: function(player) {
    var timeGiven=7;  
    var old_round_id = player.round_id;
    var new_round_n;

    //if there is no round for the player (first round)
    //round numbers start at 1
    if (old_round_id == null) {
      new_round_n=1;
    }
    else{
      new_round_n = Rounds.findOne(old_round_id).round_number+1;
    }
    
    //create the new round and save id for future use
    var new_round_id = Rounds.insert({round_number: new_round_n,
                                      player_id: player._id,
                                      game_id: player.game_id});
    Players.update({_id: player._id},
                   {$set: {round_id:new_round_id}});

    //play up to n rounds
    if (new_round_n <=5 ) {
      Games.update({player.game_id},
                   {$set {board: new_board()}});
      execute_round(player.game_id);
    }

    else {
      console.error("On round #" ++ new_round_n);
      //clear_selected_positions();
      //Players.update(Session.get('player_id'), {$set: {game_id: null}});
      //finished - has to be called(?) for "back to lobby" button to show
    }
    }
});

  execute_round = function(game_id) {
    // wind down the game clock
    var clock = 7;
    var interval = Meteor.setInterval(function () {
      Games.update(game_id, {$set: {clock: clock}});
      // end of game
      if (clock === 0) {
        // stop the clock
        Meteor.clearInterval(interval);
        // declare zero or more winners
        var scores = {};
        Words.find({game_id: game_id}).forEach(function (word) {
          if (!scores[word.player_id])
            scores[word.player_id] = 0;
          scores[word.player_id] += word.score;
        });
        var high_score = _.max(scores);
        var winners = [];
        _.each(scores, function (score, player_id) {
          if (score === high_score)
            winners.push(player_id);
        });
        Games.update(game_id, {$set: {winners: winners}});
      }
      clock -= 1;
    }, 1000);

  }

  Meteor.setInterval(function () {
  var now = (new Date()).getTime();
  var idle_threshold = now - 70*1000; // 70 sec
  var remove_threshold = now - 60*60*1000; // 1hr

  Players.update({last_keepalive: {$lt: idle_threshold}},
                 {$set: {idle: true}});

  // XXX need to deal with people coming back!
  Players.remove({$lt: {last_keepalive: remove_threshold}}); //uncommented this so let's see if it makes any changes. 

}, 30*1000);
