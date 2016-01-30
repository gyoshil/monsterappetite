////////// Main client application logic //////////

Router.route('/game',{
  template: 'page'
});

Router.configure({
    layoutTemplate: 'main'
});

Template.postgame.helpers({
  inGame: function () {
    var me = player();
    return game(me);
    //return true;
  },
  finishedGame: function () {
    var me = player();
    var g = game(me);
    return (g && g.rounds.length == roundsPerGame && g.clock ==0);
  },
  endOfRound: function () {
    console.log(endOfRound(player(),Session.get(CARDS_SELECTED)));
    return endOfRound(player(),Session.get(CARDS_SELECTED))
  }
});

Template.postgame.events({

  'click button': function (evt) {
    var me = player();
    var g = game(me);
    //this is where you will change the NUMBER OF ROUNDS TO PLAY
    if (g.rounds.length == 6){
      window.location.href = "https://tccolumbia.qualtrics.com/SE/?SID=SV_3DUw19B1ItmEKQl" + "&" + "uid=" + me._id
    }
    else{
      //clear_selected_positions
      for (var pos = 0; pos < 16; pos++)
        Session.set('selected_' + pos, false);

      Session.set(CARDS_SELECTED,0) ;

      //multiple ROUNDS fxn is called here
      Meteor.call('new_round',me,game(me)._id);
    }
  }
});


//////
////// Initialization
//////

Meteor.startup(function () {
  // Allocate a new player id.
  //
  // XXX this does not handle hot reload. In the reload case,
  // Session.get('player_id') will return a real id. We should check for
  // a pre-existing player, and if it exists, make sure the server still
  // knows about us.
  Meteor.subscribe('deck');
  Meteor.subscribe('snackazon_deck');
  Meteor.subscribe('players');
  // subscribe to all the players, the game i'm in, and all
  // the words(i.e., food cards) in that game.
  //Deps.autorun(function () {
  //  Meteor.subscribe('players');


  Tracker.autorun(function () {
    //console.log("checking for games");
    if (Session.get("ingame")) {
      //console.log("really checking for games");
      var me = player();
      if (me) {
        Meteor.subscribe('games', me._id);
        //console.log("got games from server, ready to play");
        Session.set("game ready trigger",Math.random());
      }
    }
  });
  //Meteor.subscribe('games');
  // send keepalives so the server can tell when we go away.
  //
  // XXX this is not a great idiom. meteor server does not yet have a
  // way to expose connection status to user code. Once it does, this
  // code can go away.
  /*Meteor.setInterval(function() {
    if (Meteor.status().connected)
      Meteor.call('keepalive', Session.get('player_id'));
  }, 5*1000);*/


});
