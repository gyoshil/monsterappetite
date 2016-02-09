Router.route('/pregame',{
  template: 'pregame'
});

Router.configure({
    layoutTemplate: 'main'
});


Template.pregame.helpers({
	condition: function () {
		console.log (player());
	    if (player().group == "gain")  {
	    	return '/pregame_g'
	    }
	    else {
	    	return '/pregame_l'
	    }
	    return "error_no_group"
	}
});
