Router.route('/login/:player_id', function () {
  var player_id = this.params.player_id;
  document.cookie="u_id="+player_id+"; path=/";
  Router.go("/snackazon/intro_session2")
});