Router.route('snackazon/select',{
  template: 'select'
});

Router.configure({
    layoutTemplate: 'main'
});

Template.select.helpers ({

  items : function () {
    
    var is = []
    for (i=0;i<3;i++){
      is.push(DECK[i])
    }
    return is
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
  } 
})

Template.item.events ({
  'click .top': function () {
    document.getElementById(this.ind).style.display = "block"
  },
  'click .bottom': function () {
    document.getElementById("more_"+this.ind).style.display = "block"
  }
})

