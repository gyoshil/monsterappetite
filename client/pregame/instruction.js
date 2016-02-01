Router.route('/instruction',{
  template: 'instruction'
});

Router.configure({
    layoutTemplate: 'main'
});

Template.select.events ({
  'click .done': function(event,template) {
    document.getElementById('header').scrollIntoView();
	}
})