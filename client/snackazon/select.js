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
    var is = getItems()
    for (i=0; i<3; i++){
      document.getElementById(is[i].card_name).style.display = "none"
      document.getElementById("more_"+is[i].card_name).style.display = "none"
    }
    window.scrollTo(0,0)

    //record selected item in db
    var element = template.find('input:radio[name=item]:checked');
    if (element==null) {
      Session.set(SHOW_ERROR, true);
      return;
    }
    Session.set(SHOW_ERROR, false);
    element.checked = false;

    var itemName = $(element).val();
    var itemSave = DECK.findOne({card_name:itemName})
  
    var p = player()
    Players.update({_id:p._id}, {$push: {snackazonItemChoices: {item:itemSave,round:getCurrentStage(),date: new Date()}}})

    console.log(nextStage())
    Router.go(nextStage())
  }

})

Template.item.helpers ({
  itemImg : function() {
    console.log(this);
    return '/imgs/cards/'+this.image_location+'.jpeg';
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
    console.log (player())   
    var currentRound = player().snackazonItemChoices.length+1
    if ((player().snackazonItemChoices.length+1) % 5 == 0) {
        setTimeout(function(){ }, 30000);
    }
    console.log(((player().snackazonItemChoices.length+1) % 5 == 0))
    console.log (DECK.find({round:currentRound}).fetch())
    return DECK.find({round:currentRound}).fetch()
  }


  var saveButtonPress = function(i,name){
    var p = player()
    var round = getCurrentStage()
    Players.update({_id:p._id}, {$push: {informationSeekingBehavior: {name:name,button:i,round:round,date: new Date()}}})
  }

  var nextStage = function() {
    var p = player()
    var currentStage = getCurrentStage()
    var r = p.snackazonItemChoices.length/5
    
    if(currentStage<5){
      return "/snackazon/select?which=" + (currentStage+1)
    }
    else {
      var l = p.snackazonItemChoices.slice(-5)
      console.log(l)
      var i1 = l[0].item.image_location
      var i2 = l[1].item.image_location
      var i3 = l[2].item.image_location
      var i4 = l[3].item.image_location
      var i5 = l[4].item.image_location
      
      itemParams = 
        "i1=" + i1 + "&" +
        "i2=" + i2 + "&" + 
        "i3=" + i3 + "&" + 
        "i4=" + i4 + "&" + 
        "i5=" + i5 

        return "/qualtrics"+r+"/"+ "&" + itemParams + "&" + "uid=" + p._id

    }

  }


  var getCurrentStage = function(){
    var currentStage = Router.current().params.query.which
    if(currentStage==null){
      return 1
    }
    else return parseInt(currentStage)
  }

