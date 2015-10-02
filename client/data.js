Router.route('/datapage',{
  template: 'datapage'
});

Router.configure({
    layoutTemplate: 'main'
});

Template.datapage.helpers({

 returnVal : function () {
  var output = null;
  var players = Players.find();
 
  players.forEach( function (p){
  //calculate performance here
  });

  //output should be the result of processing the data
  return output;
 }

});
