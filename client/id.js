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


function rI(a) {
  return a[Math.floor(Math.random()*a.length)];
}

Template.id.helpers({
  userName: function () {
    var nm = rI(firstName) +" "+
             rI(lastName1) +
             rI(lastName2);
    username = nm;
    return nm;
  }
});


Template.id.events({
 'submit form': function(event){
    //console.log(event.target.email.value+ " " + username);
    Meteor.call('send_email',event.target.email.value,username);
    console.log("test");
    window.location.href = "https://tccolumbia.qualtrics.com/SE/?SID=SV_9XG239e61jRYgsd" + "&"+
                           "username=" + username;
    return false;
  }

});
