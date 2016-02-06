Router.route('/instruction_g',{
  template: 'instruction_g'
});

Router.configure({
    layoutTemplate: 'main'
});


Template.instruction.onRendered( function() {
	window.scrollTo(0,0)
});
