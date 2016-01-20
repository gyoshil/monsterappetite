
player = function () {
  if(getCookieValue('u_id')=='') {
     //console.log("no player found, making a new one");
      var player_id =
         Players.insert({game_id:null,
                         name: "New User",
                         idle: false,
                         avatar: random(5)+1,
                         performance:[],
                         snackazonItemChoices:[],
                         group: "loss"});
      document.cookie="u_id="+player_id+"; path=/";
  }
  else{
     //console.log("ate cookie and found user");
  }
  //this is a huge performance hit i bet
  return Players.findOne(getCookieValue('u_id'));

};

random = function(i) {
  return Math.floor(Math.random() * (i));
}

var trim = function (string) { return string.replace(/^\s+|\s+$/g, ''); };

random_monster = function (sizeVal,avatar) {
  var size = "1"
  if (sizeVal < 1000) size = "1"
  else if (sizeVal < 2500) size = "2"
  else if (sizeVal < 4000) size = "3"
  else if (sizeVal < 5500) size = "4"
  else if (sizeVal < 7000) size = "5"
  else if (sizeVal < 9000) size = "6"
  else if (sizeVal >= 9000) size = "7"
  var color = "Yellow"
  if (avatar==1) color = "Yellow"
  else if (avatar==2) color = "Blue"
  else if (avatar==3) color = "Green"
  else if (avatar==4) color = "Orange"
  else if (avatar==5) color = "Purple"
  return 'imgs/monsters/'+color+"_stage"+size+'.png ';
}

var getCookieValue = function(a) {
  var b = document.cookie.match('(^|;)\\s*' + a + '\\s*=\\s*([^;]+)');
  return b ? b.pop() : '';
}

getPlayerScore = function(me) {

  var days = Math.ceil(game(me).rounds.length/3)
  total_score = 0
  for (var i = 1; i <= days; i++) {
   total_score += getPlayerScoreforDay(me,i)
    }
  return total_score
}

getPlayerScoreforDay = function(me,day_number) {

  var total_score = 0;
  var addScores = function(e,i,l) {
    total_score += e.calories;
  };

  var begin = (day_number-1)*9
  var end = begin +9
  var card_set = game(me).players.find(matchesP).card_set.slice(begin,end);
  card_set.forEach(addScores);
  return total_score;
}

matchesP = function(e,i,l){
  return (e._id == player()._id);
};

game = function (me) {
  //Session.get("game ready trigger");
  if(me == null) return false;
  var g = Games.findOne(me.game_id);
  //console.log(me);
  //console.log(g);
  return g;
};

//ensure you only get the group when the user has already been assigned
getGroup = function (me){
  if (me == null) return ""
  if (me.group=="loss") return "loss"
  else if (me.group=="gain") return "gain"
  else { console.error("user doesn't have a group") }
  return "no group"
};

getGroupAim = function(me){
  aim = ""
  grp = getGroup(me);
  if (grp=="loss") aim = "highest"
  else if (grp=="gain") aim = "lowest"
  return aim
};

CARDS_SELECTED = "cards_selected"
Session.setDefault(CARDS_SELECTED, 0);

endOfRound = function(me,cards_selected){
  var g  = game(me);
  //console.log((g.clock == 0) || (Session.get(CARDS_SELECTED)==3));
  if (!g) {return false}
  if ((g.clock == 0) || (Session.get(CARDS_SELECTED)==3) ){
    return true;
  }
  return false
}
