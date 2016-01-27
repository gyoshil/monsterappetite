
Router.route('/thanks',{
  template: 'thanks'
});

Router.configure({
    layoutTemplate: 'main'
});

$(document).ready(function(){    
    $("[data-toggle=tooltip]").tooltip();
});


/*function codeAddress() {  
            var cron = require('cron');
			var cronJob = cron.job("*/5 * * * * *", function(){
    			// perform operation e.g. GET request http.get() etc.
    			console.info('cron job completed');
			}); 
			cronJob.start();
        }
        window.onload = codeAddress;*/