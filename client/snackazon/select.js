Router.route('snackazon/select',{
  template: 'select'
});

Router.configure({
    layoutTemplate: 'main'
});


var SHOW_ERROR = "showError"
Session.setDefault(SHOW_ERROR, false);


Template.select.helpers ({
  showError : function () {
     return Session.get(SHOW_ERROR)
  },
  items : function () {
    return getItems()
  },
})

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
    var itemSave = SNACKAZON_DECK.findOne({card_name:itemName})
    var p = player()
    Players.update({_id:p._id}, {$push: {snackazonItemChoices: {item:itemSave,round:getCurrentStage(),date: new Date()}}})

    var is = getItems()
    for (i=0; i<3; i++){
      document.getElementById(is[i].card_name).style.display = "none"
      document.getElementById("more_"+is[i].card_name).style.display = "none"
    }
    window.scrollTo(0,0)
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
    //TODO: record info seeking behavior
    saveButtonPress(1,this.card_name)
  },
  'click .bottom': function () {
    document.getElementById("more_"+this.card_name).style.display = "block"
    saveButtonPress(2,this.card_name)
  }
})

  var getItems = function() {   
    var currentStage = getCurrentStage()
    var is = []
    for (i=currentStage*3-3; i<currentStage*3; i++){
      //TODO need proper selection criteria
      //maybe each card in the snackazon deck also has a round associated with it
      //so we know when to display it
      is.push(SNACKAZON_DECK.find().fetch()[i])
    }
    return is
  }

  var saveButtonPress = function(i,name){
    var p = player()
    var round = getCurrentStage()
    Players.update({_id:p._id}, {$push: {informationSeekingBehavior: {name:name,button:i,round:round,date: new Date()}}})
  }

  var nextStage = function() {
    var p = player()
    var currentStage = getCurrentStage()
    if(currentStage<3){
      return "/snackazon/select?which=" + (currentStage+1)
    }
    else {
      var l = p.snackazonItemChoices.slice(-3)
      console.log(l)
      var i1 = l[0].item.image_location
      var i2 = l[1].item.image_location
      var i3 = l[2].item.image_location
      window.location.href = "https://tccolumbia.qualtrics.com/SE/?SID=SV_8G1eWjPG3kRA2gd" + "&" + 
                              "i1=" + i1 + "&" +
                              "i2=" + i2 + "&" + 
                              "i3=" + i3 
    }
  }

  var getCurrentStage = function(){
    var currentStage = Router.current().params.query.which
    if(currentStage==null){
      return 1
    }
    else return parseInt(currentStage)
  }

