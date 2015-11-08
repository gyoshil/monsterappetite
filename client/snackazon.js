var group;

Router.route('/snackazon', function () {
  this.render('snackazon');
  group = this.params.query.group;
  console.log(group);
});

Router.configure({
    layoutTemplate: 'main'
});

Template.snackazon.barImg = function () {
  // only show lobby if we're not in a game
  //return "https://pixabay.com/static/uploads/photo/2014/04/02/10/18/granola-303384_640.png";
  return group;
};
