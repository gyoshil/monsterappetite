Router.route('/login/:player_id', function () {
  var player_id = this.params.player_id;
  document.cookie="u_id="+player_id+"; path=/";
  Router.go("/session2")
});

Router.route('/login', function () {
	this.render('login')
});