Router.route('/snackazon',{
  template: 'snackazon'
});

Router.configure({
    layoutTemplate: 'main'
});

Template.snackazon.barImg = function () {
  // only show lobby if we're not in a game
  return "https://pixabay.com/static/uploads/photo/2014/04/02/10/18/granola-303384_640.png";
};