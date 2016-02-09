Router.route('/signup',{
  template: 'make_user'
});

Router.configure({
    layoutTemplate: 'main'
});


var username = ''

var firstName = ["Runny", "Buttercup", "Dinky", "Stinky", "Crusty",
"Greasy","Gidget", "Cheesypoof", "Lumpy", "Wacky", "Tiny", "Flunky",
"Fluffy", "Zippy", "Doofus", "Gobsmacked", "Slimy", "Grimy", "Salamander",
"Oily", "Burrito", "Bumpy", "Loopy", "Snotty", "Irving", "Egbert",
"Waffer", "Lilly","Rugrat","Sand", "Fuzzy","Kitty",
"Puppy", "Snuggles","Rubber", "Stinky", "Lulu", "Lala", "Sparkle", "Glitter",
"Silver", "Golden", "Rainbow", "Cloud", "Rain", "Stormy", "Wink", "Sugar",
"Twinkle", "Star", "Halo", "Angel"];

var lastName1 = ["Snicker", "Buffalo", "Gross", "Bubble", "Sheep",
 "Corset", "Toilet", "Lizard", "Waffle", "Kumquat", "Burger", "Chimp", "Liver",
 "Gorilla", "Rhino", "Emu", "Pizza", "Toad", "Gerbil", "Pickle", "Tofu",
"Chicken", "Potato", "Hamster", "Lemur", "Vermin"];
var lastName2 = ["face", "dip", "nose", "brain", "head", "breath",
"pants", "shorts", "lips", "mouth", "muffin", "butt", "bottom", "elbow",
"honker", "toes", "buns", "spew", "eater", "fanny", "squirt", "chunks",
"brains", "wit", "juice", "shower"];

var random = function(i) {
  return Math.floor(Math.random() * (i));
}

function rI(a) {
  return a[random(a.length)];
}

Template.make_user.helpers({
  userName: function () {
    var nm = rI(firstName) +" "+
             rI(lastName1) +
             rI(lastName2);
    username = nm;
    return nm;
  },
});


Template.make_user.events({
 'submit form': function(event){

    //TODO: this will create a user every time, even if the email is invalid
    var email = event.target.email.value
    var p_id = createUser(email)

    //console.log("trying schedule email to "+event.target.email.value);
    Meteor.call('scheduleMail',{to:"monsterappetite499@gmail.com",
                            subject:username,
                            text:"a new user signed up: username="+username+"email="+email,
                            date:new Date()});

    var link = "http://www.monster.appetite.com/snackazon/intro_session2";
    //email to the participant 24hrs from now
    Meteor.call('scheduleMail',{to:email,
                            subject: "Monster Appetite study Session 2 for: " + username,
                            text:"Thank you for participating in the Monster Appetite study (IRB 16-145)." + 
                            "Session 2 will complete your participation in this study." + 
                            "Please continue the study at "+link+". We appreciate your time.",
                            date:new Date(new Date().getTime() + (1000))});      
    
    window.location.href = "https://tccolumbia.qualtrics.com/SE/?SID=SV_26aaP0rO26NUmB7" + "&"+
                           "uid=" + p_id;

    //just to keep html happy return false
    return false;
  }

});


function createUser(email) {

   var this_group = "";
   if (Math.random()>0.5) {this_group="loss"}
   else {this_group = "gain"};
   var player_id = Players.insert({game_id:null,
                                   name: username,
                                   idle: false,
                                   avatar: random(5)+1,
                                   performance:[],
                                   snackazonItemChoices:[],
                                   group:this_group,
                                   email: email});
   document.cookie="u_id="+player_id+"; path=/";
   return player_id;

}
