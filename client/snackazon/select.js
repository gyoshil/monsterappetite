Router.route('snackazon/select',{
  template: 'select'
});

Router.configure({
    layoutTemplate: 'main'
});

var SHOW_ERROR = "showError"
Session.setDefault("showError", false);


Template.select.helpers ({

  showError : function () {
     return Session.get(SHOW_ERROR)
  },

  items : function () {

    var currentStage = getCurrentStage()
    var is = []
    for (i=currentStage*3-3; i<currentStage*3; i++){
      //TODO need proper selection criteria
      //maybe each card in the snackazon deck also has a round associated with it
      //so we know when to display it
      is.push(SNACKAZON_DECK.find().fetch()[i])
    }
    console.log(is);
    return is
  },

})

nextStage = function () {
  var currentStage = getCurrentStage()
  if(currentStage<3){
    return "/snackazon/select?which=" + (currentStage+1)
  }
  else return "/snackazon/PDQ"
}

var getCurrentStage = function(){
    var currentStage = Router.current().params.query.which
    if(currentStage==null){
      return 1
    }
    else return parseInt(currentStage)
  }
Template.select.events ({
  'click .done': function(event,template) {
    //record selected item in db
    var element = template.find('input:radio[name=item]:checked');
    if (element==null) {
      Session.set(SHOW_ERROR, true);
      return;
    }
    Session.set(SHOW_ERROR, false);
    element.checked = false;

    var itemName = $(element).val();
    //player=loggedInPlayer()
    var p = player()
    Players.update({_id:p._id}, {$push: {snackazonItemChoices: itemName}})

    for (i=0; i<3; i++){
      document.getElementById(i).style.display = "none"
      document.getElementById("more_"+i).style.display = "none"
    }
    Router.go(nextStage())
  }

})

Template.item.helpers ({
  itemImg : function() {
    console.log(this);
    return '/imgs/cards/'+this.image_location+'.jpg';
  },

})

Template.item.events ({
  'click .top': function () {
    document.getElementById(this.card_name).style.display = "block"
    //record this in the database for the logged-in player
  },
  'click .bottom': function () {
    document.getElementById("more_"+this.card_name).style.display = "block"
    //record this in the database for the logged-in player
  }
})
