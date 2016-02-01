Router.route('/pregame_g',{
  template: 'pregame_g'
});

Router.configure({
    layoutTemplate: 'main'
});

Template.select.events ({
  'click .done': function(event,template) {
    document.getElementById('header').scrollIntoView();
	}
})