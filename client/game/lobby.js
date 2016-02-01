Template.lobby.helpers ({

  show: function () {
    // only show lobby if we're not in a game
    var me = player();
    return !game(me);
  },

  waiting : function () {
    var players = Players.find({_id: {$eq: Session.get('player_id')},
                                game_id: {$exists: false}});
    return players;
  },

  count : function () {
    //$ne selects the documents where the value of the field is NOT EQUAL (i.e. !=) to the specified value.
    //This includes documents that do not contain the field.
    var players = Players.find({_id: {$ne: Session.get('player_id')},
                                name: {$ne: ''},
                                game_id: {$exists: false}});
    return players.count();
  },

  disabled : function () {
    var me = player();
    if (me && me.name)
      return '';
    return 'disabled';
  },

  username : function (){
    var me = player();
    if(me)
      return me.name;
    else{
      return ""
    }
  }

});


Template.lobby.events({
  //'keyup input#myname': function (evt) {
  //  var name = trim($('#lobby input#myname').val());
  //  Players.update(Session.get('player_id'), {$set: {name: name}});
  //},
  'click button.startgame': function () {
    var me = player();
    //////////////////////////////////// START NEW GAME method is called /////////////////
    Meteor.call('start_new_game', me._id, function (error, result) {
      if (error) {
      // handle error
      //console.error("you have made a mistake");
      }  else {
      //////////////////////////////////// NEW ROUND method is called ////////////////////
      //console.log("starting a new round");
      Meteor.call('new_round',player(),result);
      //console.log(result)
      //console.log(player())
      //console.log(Players.findOne({_id:player()._id}))
      Players.update({_id:player()._id}, {$set: {game_id: result}},
                     function(e,i){
                       Session.set("ingame",Math.random());});
    }
    window.scrollTo(0,0)
  });
  }
});
