
Router.configure({
    layoutTemplate: 'main'
});

Template.PDQ.helpers({

  choices : function () {
    console.log(getChosenOnes())
    return getChosenOnes()
  },

//This whole section below is not working. That is probably because now PDQ is done WITHIN qualtrics !!!
  /*afterPDQ : function () {
    d = getAllChosenOnes()
    console.log(d)
    console.log("is this working?")
    if (d.length%10==0) return "/thanks"
      //test if the console.error below shows up or not after running thru all the steps on localhost
      console.error("user should have 6 choices in total but only 3 should show up at PDQ")
    if (d.length%5==0) return "/biq"
    else return "" //shouldnt get here
  }*/
})


var getChosenOnes = function(){
    var p = player()
    var c = p.snackazonItemChoices.slice(-3) //last 3 items
    if (c.length<3){
      console.error("user should have 3 choices by this time, something is wrong")
    }
    return c
}

var getAllChosenOnes = function() {
  var p = player()
  var d = p.snackazonItemChoices
  return d
}

//use http://www.qualtrics.com/university/researchsuite/developer-tools/custom-programming/example-code-snippets/
// to set fields within the survey
Template.chosenItem.helpers({
  itemImg : function () {
    return "/imgs/cards/"+this.item.image_location+".jpeg"
  }
})
