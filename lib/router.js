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
  if((typeof this.options.layout==='undefined') || window.location.href.indexOf('login')>=0){
    this.next();
  }
  else {
    try{
      window.location.hash="back-button-disabled";
      window.location.hash="Back-button-disabled";//again because google chrome don't insert first hash into history
      //window.onhashchange=function(){window.location.hash="back-button-disabled";}
      //console.log(window.location.href);
      
      if(window.location.href.indexOf('snackazon')<=0){
        window.onbeforeunload = function() {
          return "Please do not use the back or refresh button. It will destroy our data collection";
        };
      }
    }
    catch(e){
     //dont care
    }
    this.next();
  }
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

