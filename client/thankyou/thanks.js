
Router.route('/thanks',{
  template: 'thanks'
});

Router.configure({
    layoutTemplate: 'main'
});

$(document).ready(function(){    
    $("[data-toggle=tooltip]").tooltip();
});