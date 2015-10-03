////////// Main client application logic //////////

//////
////// LOBBY template: shows everyone not currently playing, and
////// offers a button to start a fresh game.
//////
Router.route('/',{
  template: 'page'
});

Router.configure({
    layoutTemplate: 'main'
});

Template.lobby.show = function () {
  // only show lobby if we're not in a game
  return !game();
};

Template.lobby.waiting = function () {
  var players = Players.find({_id: {$ne: Session.get('player_id')},
                              name: {$ne: ''},
                              game_id: {$exists: false}});
  return players;
};

Template.lobby.count = function () { 
  //$ne selects the documents where the value of the field is NOT EQUAL (i.e. !=) to the specified value. 
  //This includes documents that do not contain the field.
  var players = Players.find({_id: {$ne: Session.get('player_id')},
                              name: {$ne: ''},
                              game_id: {$exists: false}});
  return players.count();
};


Template.lobby.disabled = function () {
  var me = player();
  if (me && me.name)
    return '';
  return 'disabled';
};


var trim = function (string) { return string.replace(/^\s+|\s+$/g, ''); };

Template.lobby.events({
  'keyup input#myname': function (evt) {
    var name = trim($('#lobby input#myname').val());
    Players.update(Session.get('player_id'), {$set: {name: name}});
  },
  'click button.startgame': function () {
    //////////////////////////////////// START NEW GAME method is called //////////////////////////////////
  Meteor.call('start_new_game', function (error, result) {
    if (error) {
      // handle error
      console.error("you have made a mistake");
    }  else {
      //////////////////////////////////// NEW ROUND method is called //////////////////////////////////
      Meteor.call('new_round',player(),result);
    }
  });
  }
});


//////
////// BOARD template: renders the board and the clock given the
////// current game.  
//////


Template.board.square = function (i) {
  var g = game();
  var display_card = '';
  if (g) {
      display_card = 'imgs/'+g.rounds[g.rounds.length-1][i].card_name+'.jpeg';
    }
  else display_card = 'imgs/monster'+(random(6)+1)+'.svg';
  return display_card
};

//this is where I enlarged the size of the pics on the board and FOOD cards
Template.board.squaresize = function () {
  return 'width:145px; height:142px';
};

Template.board.selected = function (i) {
  return Session.get('selected_' + i);
};

Template.board.bkgd = function () {
  var c = game().rounds.length%3;
  if (c==0){
    return "green";
  };
  if (c==1) {
    return "blue";
  };
  if (c==2) {
    return "pink";
  };
  return '';

};

Template.board.clock = function () {
  var clock = game() && game().clock;

  if (!clock || clock === 0)
    return;

  // format into Minute : Seconds like 0:03
  var min = Math.floor(clock / 60);
  var sec = clock % 60;
  return min + ':' + (sec < 20 ? ('0' + sec) : sec);
};

var cards_selected=0;
Template.board.events({
  'click .square': function (evt) {
    if (game() && game().clock != 0 && cards_selected < 3) { 
    //when you change the last number on this line, change "instructions" in html
    
    /////////////// this is finding the food card id in a complex way //////////
    // card id might be in this div
    var dom_card_id = evt.target.id;
    var c_id = dom_card_id.substring(5);
    
    //or might be in parent div
    var p_card_id = evt.target.parentNode.id;
    var pc_id = p_card_id.substring(5);
    
    //but it wont be in both (ie one will be empty)
    var id = c_id + pc_id;


    if (Session.get('selected_'+id)!='last_in_path') {
      Session.set('selected_' + id, 'last_in_path');
      
      //GET CARD NAME
      var g = game();
      var card_name = g.rounds[g.rounds.length-1][id].card_name;                      
      
      //TODO - merge and extract these, need currying, does js have this?
      var matchesC = function(e,i,l){
        return (e.card_name == card_name);
      };

      new_card = DECK.find(matchesC id);

      all_players = g.players;
      all_players.find(matchesP).card_set.push(new_card);
      //can't set fields of fields. can only change top level fields of mongo
      Games.update({_id:g._id}, {$set: {players: all_players}}); 
      //console.error(g.players.find(matchesP).card_set);
      cards_selected+=1;
    }
  }
  }
});

Template.postgame.helpers({
  show: function () {
    return game() && game().clock == 0;
  },
  finished: function () {
    return !game();

  }
});

Template.postgame.events({
  'click button': function (evt) {
    clear_selected_positions();
    cards_selected = 0;
    document.getElementById('postgame').style.visibility = 'hidden';
    
    //this pop up window comes up after "NEXT ROUND" is clicked
    //MAYBE have this only after the 10 or so practice rounds before the "TEST" round. 
    //window.alert("Next round will be a test to see if you choose the highest three");

    //multiple ROUNDS fxn is called here
    Meteor.call('new_round',player(),game()._id);
  }
});

//////
////// 'SCORES' shows everyone's score and list of selected food cards.
//////


//This part shows the entire section that lists scores, selected items, avatar
Template.scores.helpers({
  show : function () {
    // !! is turning the object into a boolean
    return !!game();
  },
  players : function () {
    return game().players;
  }
});

Template.player.helpers({
  winner : function () {
  /*var g = game();
  if (g.winners && _.include(g.winners, this._id))
    return 'winner';*/
    return '';
  },

  // how total score is added (selected items show their individual scores even w/o this code, 
  // but TOTAL is not calculated w/o this section)
  total_score : function () {

    var total_score = 0;
    var addScores = function(e,i,l) {
      total_score += e.calories;
      return '';
    };

    var card_set = game().players.find(matchesP).card_set;
    card_set.forEach(addScores);

    return total_score;
  },

  //this 'updates' the avatar id every second
  //not good, but works
  random_monster : function () {
    return 'imgs/monster'+Players.findOne(this._id).avatar+'.svg';
  },

  monster_size : function () {
    return 'width:'+ '128' + 'px; height:128px';
  },
  cards : function() {
    g = game();
    return g.players.find(matchesP).card_set;
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
  
  // This actually ok for us. During data analysis we cansimply query on name rathr than id

  var player_id = Players.insert({game_id:null,name: '', idle: false, avatar: random(6)+1, performance:[]});
  Session.set('player_id', player_id);

  //then how to allocate a NEW ROUND ID????

  // subscribe to all the players, the game i'm in, and all
  // the words(i.e., food cards) in that game.
  Deps.autorun(function () {
    Meteor.subscribe('players');

    if (Session.get('player_id')) {
      var me = player();
      if (me && me.game_id) {
        Meteor.subscribe('games', me.game_id);
        Meteor.subscribe('cards', me.game_id, Session.get('player_id'));
      }
    }
  });

  // send keepalives so the server can tell when we go away.
  //
  // XXX this is not a great idiom. meteor server does not yet have a
  // way to expose connection status to user code. Once it does, this
  // code can go away.
  Meteor.setInterval(function() {
    if (Meteor.status().connected)
      Meteor.call('keepalive', Session.get('player_id'));
  }, 5*1000);
});



//////
////// Utility functions
//////

var matchesP = function(e,i,l){
  return (e._id == player()._id);
};

var player = function () {
  return Players.findOne(Session.get('player_id'));
};

var game = function () {
  var me = player();
  var g = Games.findOne(me.game_id);
  return g;
};

var clear_selected_positions = function () {
  for (var pos = 0; pos < 16; pos++)
    Session.set('selected_' + pos, false);
};

var random = function(i) {
  return Math.floor(Math.random() * (i));
}

