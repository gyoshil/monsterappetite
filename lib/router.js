//onRun will run only once on every route change
//might be good for data collection
Router.onRun(function(){
  this.next();
});


//onBeforeAction will reactively rerun when the current route data context is modified.
Router.onBeforeAction(function(){
  window.location.hash="back-button-disabled";
  window.location.hash="Back-button-disabled";//again because google chrome don't insert first hash into history
  window.onhashchange=function(){window.location.hash="back-button-disabled";}
  window.onbeforeunload = function() {
    return "Please do not use the back or refresh button. It will destroy our data colelction";
  };

  this.next();

});
