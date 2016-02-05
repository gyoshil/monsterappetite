Router.route('/instruction',{
  template: 'instruction'
});

Router.configure({
    layoutTemplate: 'main'
});


Template.instruction.onRendered( function() {
	window.scrollTo(0,0)
});