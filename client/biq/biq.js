Router.route('/biq',{
  template: 'biq'
});

Router.configure({
    layoutTemplate: 'main'
});

//taken from Snackazon select.js page
Template.biq.events ({
  'click button': function(event,template) {
    //record selected item in db
    //var element = template.find('input:radio[name=item]:checked');
    //var itemName = $(element).val();
    //player=loggedInPlayer()
    var p = Players.findOne(getCookieValue('u_id'))
    Players.update({_id:p._id}, {$push: {biqTimes: 1}})
  }
})

//taken from Snackazon PDQ.js page
Template.biq.helpers({
  choices : function () {
    console.log(getAnswers())
    return getAnswers()
  },

  afterBIQ : function () {
    c = getAnswers()
    console.log(c)
    if (c.length%2==0) return "/pregame"
    if (c.length%1==0) return "/snackazon/select"
    else return "" //shouldnt get here
  }
}) 

var getAnswers = function(){
    var p = Players.findOne(getCookieValue('u_id'))
    //my question is where is "intentionItemChoices" defined?
    //in PDQ it is return p.snackazonItemChoices. WHERE is this defined?
    if (p.biqTimes==null) return []
    return p.biqTimes
}