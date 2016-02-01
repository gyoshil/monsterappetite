//////
////// BOARD template: renders the board and the clock given the
////// current game.
//////


Template.board.helpers({
  group_aim : function () {
    me = player();
    return getGroupAim(me) + " caloric"
  },

  cardSet : function (){
    var me = player();
    g = game(me);
    if(g){
      return g.rounds[g.rounds.length-1];
    }
    else {
      return ([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]);
    }
  },

  getImage : function () {
    var me = player();
    var g = game(me);
    var display_card = '';

    if (g != null && g && g.rounds[g.rounds.length-1] != null) {
      display_card = 'imgs/cards/'+this.image_location+'.jpeg';
    }
    else {
      display_card = random_monster(random(1200),random(5)+1);
    }
    return display_card
  },

   //this is where I enlarged the size of the pics on the board and FOOD cards
  squaresize : function () {
    return 'width:145px; height:142px';
  },

  selected : function (i) {
    return Session.get('selected_' + i);
  },

  bkgd : function () {
    //if we are in the lobby, not a game, no background
    var me = player();
    if (!game(me)) {return ""}
    //otherwise show a nice colored background
    var c = game(me).rounds.length % 3;
    if (c==1){//morning
      return "green";
    };
    if (c==2) {//afternoon
      return "blue";
    };
    if (c==0) {//evening
      return "pink";
    };
    return '';
  },

  clock : function () {
    var me = player();
    if (game(me) == null || game(me).clock == 0)
      return;

    var clock =  game(me).clock;
    // format into Minute : Seconds like 0:03
    var min = Math.floor(clock / 60);
    var sec = clock % 60;
    return min + ':' + (sec < 30 ? ('0' + sec) : sec);
  }
});

Template.board.events({
  'click .square': function (evt) {
    var me = player();

    if (game(me) && game(me).clock != 0 && Session.get(CARDS_SELECTED) < 3) {
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
      var g = game(me);
      var this_card_name = g.rounds[g.rounds.length-1][id].card_name;

      new_card = DECK.findOne({card_name:this_card_name});

      all_players = g.players;
      all_players.find(matchesP).card_set.push(new_card);

      //can't set fields of fields. can only change top level fields of mongo
      Games.update({_id:g._id}, {$set: {players: all_players}});
      Session.set(CARDS_SELECTED,Session.get(CARDS_SELECTED)+1);
    }
  }
  }
});
