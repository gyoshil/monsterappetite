Router.route('snackazon_1',{
  template: 'snackazon_1'
});

Router.configure({
    layoutTemplate: 'main'
});
Template.snackazon_1.barImg = function () {
  // only show lobby if we're not in a game
  //return "https://pixabay.com/static/uploads/photo/2014/04/02/10/18/granola-303384_640.png";
  return "imgs/banner.png";
};

Template.snackazon_1.boxImg = function () {
  var x = Math.random() ;
  x = Math.floor(x*6+1);
  return "imgs/monster" + x + ".png";
};