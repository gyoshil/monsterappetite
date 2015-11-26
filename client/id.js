Router.route('/makeUser',{
  template: 'id'
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

Template.id.helpers({
  userName: function () {
    var nm = rI(firstName) +" "+
             rI(lastName1) +
             rI(lastName2);
    username = nm;
    return nm;
  },
});


Template.id.events({
 'submit form': function(event){
    
    var p_id = createUser()
    console.log("sent email to "+event.target.email.vale);
    Meteor.call('send_email',event.target.email.value, username);
    window.location.href = "https://tccolumbia.qualtrics.com/SE/?SID=SV_9XG239e61jRYgsd" + "&"+
                           "uid=" + p_id;

   //just to keep html happy return false
    return false;
  }

});


function createUser() {

   var this_group = "";
   if (Math.random()>0.5) {this_group="loss"}
   else {this_group = "gain"};
   var player_id = Players.insert({game_id:null,name: username, idle: false, avatar: random(6)+1, performance:[], group:this_group});
   document.cookie="u_id="+player_id+"; path=/";
   return player_id;

}
