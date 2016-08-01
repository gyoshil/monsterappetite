//onRun will run only once on every route change
//might be good for data collection
Router.onRun(function(){

  //var p = player()
  //Players.update({_id:p._id}, {$push: {snackazonStartTimes: {date: new Date()}}})
  this.next();

});


//onBeforeAction will reactively rerun when the current route data context is modified.
Router.onBeforeAction(function(){
  this.next()
},  {where: 'client'});


Router.route('/game',function () {
  this.render( 'page');
});


Router.route('/', function () {
  this.render('consent');
});
Router.route('/consent2',function () {
  this.render('consent2');
});

Router.route('/datapage',function () {
  template: 'datapage'
});


Router.route('/instruction_g',{
  template: 'instruction_g'
});
Router.route('/instruction',{
  template: 'instruction'
});

Router.route('/pregame_g',{
  template: 'pregame_g'
});
Router.route('/pregame_l',{
  template: 'pregame_l'
});
Router.route('/pregame',{
  template: 'pregame'
});

Router.route('/demo/:player_id', function () {
  var player_id = this.params.player_id;
  document.cookie="u_id="+player_id+"; path=/";
  Router.go("/game")
});


Router.route('/login/:player_id', function () {
  var player_id = this.params.player_id;
  document.cookie="u_id="+player_id+"; path=/";
  Router.go("/session2")
});

Router.route('/login', function () {
	this.render('login')
});

Router.route('/signup',{
  template: 'make_user'
});

Router.route('/session2',{
  template: 'session2'
});

Router.route('/snackazon/intro', function () {
  this.render('intro');
});


Router.route('/snackazon/intro2', function () {
  this.render('intro2');
});
Router.route('/snackazon/PDQ',{
  template: 'PDQ'
});

Router.route('snackazon/q_redirect',{
  template: 'q_redirect'
});

Router.route('snackazon/select',{
  template: 'select'
});








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
