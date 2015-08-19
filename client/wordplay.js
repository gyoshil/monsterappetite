////////// Main client application logic //////////

//////
////// LOBBY template: shows everyone not currently playing, and
////// offers a button to start a fresh game.
//////

Template.lobby.show = function () {
  // only show lobby if we're not in a game
  return !game() && !round();
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

//need some interpretation of this function. ??????????????????
Template.lobby.disabled = function () {
  var me = player();
  if (me && me.name)
    return '';
  return 'disabled';
};

// SOMEHOW the below line, if commented out, disables the "Play solo" button in the start page
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
  var back_of_card_pic = 'imgs/monster'+(random(6)+1)+'.svg';
  return g && g.board && 'imgs/'+g.board[i].card_name+'.jpeg' || back_of_card_pic;
};

//this is where I enlarged the size of the pics on the board and FOOD cards
Template.board.squaresize = function () {
  return 'width:145px; height:142px';
};

Template.board.selected = function (i) {
  return Session.get('selected_' + i);
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

//TODO this is shitty code
var cards_selected=0;
Template.board.events({
  'click .square': function (evt) {
    if (game() && game().clock != 0 && cards_selected < 3) { 
    //when you change the last number on this line, change "instructions" in html
    
    //////////////////////////// WHY have TWO DIVs in the first place????? ///////////////////////////////
    //id might be in this div
    // AND is this id of the food card, player, game? ????????????
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
      card_name =  game().board[id].card_name;                      
      
      //so WHY is the round_id NULL for every round???????
      round_id=player().round_id; //I switched the player() to game() and selected food items didnt show up on score board
      console.error(round_id);

      // THIS IS WHERE selected CARDS are shown with image and calories 
      var card_id = Words.insert({player_id: Session.get('player_id'),
                                game_id: game() && game()._id,
                                round_id: round_id,
                                word: card_name, 
                                img:'imgs/'+card_name+'.jpeg',
                                score: game().board[id].calories,
                                state: 'good'});
      //apparently at NO POINT is the score_card method doing anything. NO ROLE at all. 
      Meteor.call('score_card', card_id);
      //this is the one that limited me to select 3 cards. 
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
    Meteor.call('new_round',player());
  }
});

//////
////// 'SCORES' shows everyone's score and list of selected food cards.
//////


//This part shows the entire section that lists scores, selected items, avatar
Template.scores.show = function () {
  // is !! and != the same meaning?
  return !!game();
};

Template.scores.players = function () {
  return game() && game().players;
};

Template.player.winner = function () {
  var g = game();
  if (g.winners && _.include(g.winners, this._id))
    return 'winner';
  return '';
};

// how total score is added (selected items show their individual scores even w/o this code, 
// but TOTAL is not calculated w/o this section)
Template.player.total_score = function () {
  var words = Words.find({game_id: game() && game()._id,
                          player_id: this._id});
  var score = 0;
  words.forEach(function (word) {
    if (word.score)
      score += word.score;
  });
  return score;
};

//this 'updates' the avatar id every second
//not good, but works
Template.player.random_monster = function () {
    return 'imgs/monster'+Players.findOne(this._id).avatar+'.svg';
}

Template.player.monster_size = function () {
  return 'width:'+ '128' + 'px; height:128px';
}

Template.words.words = function ( ) {
  round_id = player().round_id;
  
  //console.error(round_id);
  return Words.find({game_id: game() && game()._id,
                    player_id: this._id,
                    round_id: round_id});
};


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
  
  var player_id = Players.insert({game_id:null,name: '', idle: false, round_id: null, avatar: random(6)+1});
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
        //here 'words' refers to food cards
        Meteor.subscribe('words', me.game_id, Session.get('player_id'));
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

var player = function () {
  return Players.findOne(Session.get('player_id'));
};

var game = function () {
  var me = player();
  return me && me.game_id && Games.findOne(me.game_id);
};

//when this section is deleted there is no place to enter name and start the game
var round = function () {
  var me = player();
  return me && me.round_id && Rounds.findOne(me.round_id);
};

var clear_selected_positions = function () {
  for (var pos = 0; pos < 16; pos++)
    Session.set('selected_' + pos, false);
};

var random = function(i) {
  return Math.floor(Math.random() * (i));
}

