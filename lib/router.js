//onRun will run only once on every route change
//might be good for data collection
Router.onRun(function(){

  //var p = player()
  //Players.update({_id:p._id}, {$push: {snackazonStartTimes: {date: new Date()}}})
  this.next();

});

/*Router.route('/', function () {
  this.render('main');
});*/



//onBeforeAction will reactively rerun when the current route data context is modified.
Router.onBeforeAction(function(){
  this.next()
},  {where: 'client'});


//PDQ1
Router.route('/qualtrics1/:items', function() {
  this.response.writeHead(302, {
    'Location':
      "https://tccolumbia.qualtrics.com/SE/?SID=SV_e4isOXkrY07CTZ3" + this.params.items
  });
  this.response.end();
}, {where: 'server'});

//PDQ2
Router.route('/qualtrics2/:items', function() {
  this.response.writeHead(302, {
    'Location':
      "https://tccolumbia.qualtrics.com/SE/?SID=SV_3dQKAjLQI3ZJhl3" + this.params.items
  });
  this.response.end();
}, {where: 'server'});

//PDQ3
Router.route('/qualtrics3/:items', function() {
  this.response.writeHead(302, {
    'Location':
      "https://tccolumbia.qualtrics.com/SE/?SID=SV_6f1GXgGqGMHDB7D" + this.params.items
  });
  this.response.end();
}, {where: 'server'});

//PDQ4
Router.route('/qualtrics4/:items', function() {
  this.response.writeHead(302, {
    'Location':
      "https://tccolumbia.qualtrics.com/SE/?SID=SV_aXmPBcnOyaBg8pD" + this.params.items
  });
  this.response.end();
}, {where: 'server'});

//PDQ4_MT
Router.route('/qualtrics5/:items', function() {
  this.response.writeHead(302, {
    'Location':
      "https://tccolumbia.qualtrics.com/jfe/form/SV_9XivTnkJ0ccC0wl?" + this.params.items
  });
  this.response.end();
}, {where: 'server'});

