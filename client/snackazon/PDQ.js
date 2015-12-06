Router.route('/snackazon/PDQ',{
  template: 'PDQ'
});

Router.configure({
    layoutTemplate: 'main'
});

Template.PDQ.helpers({

  choices : function () {
    console.log(getChosenOnes())
    return getChosenOnes()
  },
  afterPDQ : function () {
    c = getChosenOnes()
    if (c.length%6==0) return "/thanks"
    if (c.length%3==0) return "/biq"
    else return "" //shouldnt get here
  }
})


var getChosenOnes = function(){
    var p = Players.findOne(getCookieValue('u_id'))
    return p.snackazonItemChoices
}
//use http://www.qualtrics.com/university/researchsuite/developer-tools/custom-programming/example-code-snippets/
// to set fields within the survey
Template.chosenItem.helpers({
  itemImg : function () {
    return "/imgs/cards/"+this+".jpeg"
  }
})

