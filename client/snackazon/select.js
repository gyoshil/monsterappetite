Router.route('snackazon/select',{
  template: 'select'
});

Router.configure({
    layoutTemplate: 'main'
});

Template.select.helpers ({

  items : function () {
    
    var currentStage = getCurrentStage()
    var is = []
    for (i=currentStage*3-3; i<currentStage*3; i++){
      is.push(SNACKAZON_DECK[i])
    }
    return is
  },

  nextStage : function () {
    var currentStage = getCurrentStage()
    if(currentStage<3){
      return "select?which=" + (currentStage+1)
    }
    else return "PDQ"
  }
})
 
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
    var itemName = $(element).val();
    //player=loggedInPlayer()
    var p = player()
    Players.update({_id:p._id}, {$push: {snackazonItemChoices: itemName}})

    for (i=0; i<3; i++){
      document.getElementById(i).style.display = "none"
      document.getElementById("more_"+i).style.display = "none"
    }
  }

})

Template.item.helpers ({
  itemImg : function() {
    return '/imgs/cards/'+this.cards[this.ind].card_name+'.jpeg';
  },
  
  itemName : function() {
    return this.cards[this.ind].card_name;
  },
 
  itemCalories : function () {
    return this.cards[this.ind].calories
  }, 
  itemIngredients :function () {
    return this.cards[this.ind].ingredients;
  },
  itemSource : function () {
    return this.cards[this.ind].source_;
  }
})

Template.item.events ({
  'click .top': function () {
    document.getElementById(this.ind).style.display = "block"
    //record this in the database for the logged-in player
  },
  'click .bottom': function () {
    document.getElementById("more_"+this.ind).style.display = "block"
    //record this in the database for the logged-in player
  }
})

