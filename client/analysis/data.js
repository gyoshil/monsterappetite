Router.route('/datapage',{
  template: 'datapage'
});

Router.configure({
    layoutTemplate: 'main'
});

Template.datapage.helpers({

 returnVal : function () {
  var output = "";
  var players = Players.find().fetch();
  console.log(Players); 
  console.log(players); 
  players.forEach( function (p){
  	if (p.name!="") {
  	//everytime we load the main page we add a user with ablank user name. ya, this code is that bad
  	//at the very least, we should clean the database out of these entries here
  		output += p.name+ ", "+p.performance+"; ";
      //console.error(p.performance);
  	};
  });

  //output should be the result of processing the data
  return output;
 }

});
