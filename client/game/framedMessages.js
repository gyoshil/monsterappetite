
Template.overlay.helpers({
  show : function () {
    var me = player()
    g = game(me)
    return (g.rounds.length % 3 == 0 && endOfRound(me,Session.get(CARDS_SELECTED)))
  },

  text : function () {
    var me = player();
    var grp = getGroup(me);
    var g  = game(me);
    if (g == null) return ""

    var r = g.rounds;
    var totalPossiblePoints = 0
    if(grp =="loss"){
      x =
          highest_possible_score(r[r.length-1]) +
          highest_possible_score(r[r.length-2]) +
          highest_possible_score(r[r.length-3])
      console.log(x)
      totalPossiblePoints = x

    }
    else if (grp =="gain"){
      x =
          lowest_possible_score(r[r.length-1]) +
          lowest_possible_score(r[r.length-2]) +
          lowest_possible_score(r[r.length-3])
      console.log(x)
      totalPossiblePoints = x
    }

    //TODO getPLayerScore PER DAY
    var day_number = Math.floor(r.length/3)
    var score_sentance = "SUMMARY OF DAY "+day_number+": You ate "+ getPlayerScoreforDay(me,day_number) +" calories today. "

    var framing_sentance = ""
    if (grp =="loss" && (day_number % 2 ==1)) {
      framing_sentance =
        "The HIGHEST possible calories your monster could have consumed today was " +
        totalPossiblePoints + ". If you had eaten " + (totalPossiblePoints - getPlayerScoreforDay(me,day_number))+
        " MORE calories to reach the HIGHEST CALORIC consumption of DAY " + day_number+ ", you would be at a HIGHER RISK for type 2 diabetes. "
    }
    else if (grp =="loss" && (day_number % 2 ==0)) {
      framing_sentance =
        "The HIGHEST possible calories your monster could have consumed today was " +
        totalPossiblePoints + ". If you had eaten " + (totalPossiblePoints - getPlayerScoreforDay(me,day_number))+
        " MORE calories to reach the HIGHEST CALORIC consumption of DAY " + day_number+ ", you would be at a HIGHER RISK for a cardiovascular disease. "
    }

    else if (grp =="gain" && (day_number % 2 ==1)){
      framing_sentance = "The LOWEST possible calories your monster could have consumed today was " +
      totalPossiblePoints+ ". If you had eaten " + (getPlayerScoreforDay(me,day_number ) - totalPossiblePoints) +
       " FEWER calories to reach the LOWEST CALORIC consumption of DAY "+ day_number+ ", you would be at a LOWER RISK for type 2 diabetes. "
      //can I make it switch from type 2 diabetes, heart attack, and something else?
    }

    else if (grp =="gain" && (day_number % 2 ==0)) {
      framing_sentance = "The LOWEST possible calories your monster could have consumed today was " +
      totalPossiblePoints+ ". If you had eaten " + (getPlayerScoreforDay(me,day_number ) - totalPossiblePoints) +
       " FEWER calories to reach the LOWEST CALORIC consumption of DAY "+ day_number+ ", you would be at a LOWER RISK for a cardiovascular disease. "
    }
    return score_sentance + framing_sentance ;
  }
});
