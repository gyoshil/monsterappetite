////////// Server only logic //////////

Meteor.methods ({
  start_new_game: function () {
    // TIME GIVEN
    var timeGiven=2;

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

    //move this code out of this method. should only be in new_round
    //new game only creates the record, but new reound actually plays it
    // wind down the game clock
    var clock = timeGiven;
    var interval = Meteor.setInterval(function () {
      clock -= 1;
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
    }, 1000);

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
    var timeGiven=2;  
    var old_round_id = player.round_id;
    
    if (old_round_id == 0) { 
       var new_round_id = Rounds.insert({round_number: 1,
                                         player_id: player.player_id,
                                         game_id: player.game_id,
                                         clock: timeGiven});
       new_round_n=1;
    }
    else {  
      var old_round = Rounds.findOne(old_round_id);
      var new_round_n = old_round.round_number+1;
      var new_round_id = Rounds.insert({round_number: 0,
                                        player_id: player.player_id,
                                        game_id: player.game_id,
                                        clock: timeGiven});
    }
    // round_number will go up as each round is played, once a total of two games are played, entire game ends.  
    if (new_round_n <2 ) {
      //play another round 
      // wind down the game clock
      var clock = timeGiven;
      var interval = Meteor.setInterval(function () {
        clock -= 1;
          Games.update(player.game_id, {$set: {clock: clock}});

        //Rounds.update(new_round_id, {$set: {clock: clock}});

        // end of game
        if (clock === 0) {
          // stop the clock
          Meteor.clearInterval(interval);
          // declare zero or more winners
          var scores = {};
          Words.find({game_id: player.game_id}).forEach(function (word) {
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
          Rounds.update(round_id, {$set: {winners: winners}}); 
        }
      }, 1000);
    }

    else {
      clear_selected_positions();
      cards_selected = 0;
      Players.update(Session.get('player_id'), {$set: {game_id: null}});
    }
    }
});


Meteor.setInterval(function () {
  var now = (new Date()).getTime();
  var idle_threshold = now - 70*1000; // 70 sec
  var remove_threshold = now - 60*60*1000; // 1hr

  Players.update({last_keepalive: {$lt: idle_threshold}},
                 {$set: {idle: true}});

  // XXX need to deal with people coming back!
  Players.remove({$lt: {last_keepalive: remove_threshold}}); //uncommented this so let's see if it makes any changes. 

}, 30*1000);
