Router.route('/pregame_l',{
  template: 'pregame_l'
});

Router.configure({
    layoutTemplate: 'main'
});

Template.select.events ({
  'click .done': function(event,template) {
    window.scrollTo(0,0)
	}
})