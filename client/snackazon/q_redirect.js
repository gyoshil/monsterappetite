Router.route('snackazon/q_redirect',{
  template: 'q_redirect'
});

Router.configure({
    layoutTemplate: 'main'
});

Template.q_redirect.helpers ({
	moving : function () {

	var p = player()
    //var currentStage = getCurrentStage()
    var r = p.snackazonItemChoices.length/5
    var l = p.snackazonItemChoices.slice(-5)
	      
	var i1 = l[0].item.image_location
	var i2 = l[1].item.image_location
	var i3 = l[2].item.image_location
	var i4 = l[3].item.image_location
	var i5 = l[4].item.image_location
	  
	itemParams = 
	    "i1=" + i1 + "&" +
	    "i2=" + i2 + "&" + 
	    "i3=" + i3 + "&" + 
	    "i4=" + i4 + "&" + 
	    "i5=" + i5 
         
        window.location.href="/qualtrics"+r+"/"+ "&" + itemParams + "&" + "uid=" + p._id;  
    	return ""
    	
	}
			
	/*var getCurrentStage = function(){
	    var currentStage = Router.current().params.query.which
	    if(currentStage==null){
	      return 1
	    }
	    else return parseInt(currentStage)
	  }*/
})
