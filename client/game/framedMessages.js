
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
      totalPossiblePoints =
          highest_possible_score(r[r.length-1]) +
          highest_possible_score(r[r.length-2]) +
          highest_possible_score(r[r.length-3])
    }
    else if (grp =="gain"){
      totalPossiblePoints =
          lowest_possible_score(r[r.length-1]) +
          lowest_possible_score(r[r.length-2]) +
          lowest_possible_score(r[r.length-3])
    }

    //TODO getPLayerScore PER DAY
    var day_number = Math.floor(r.length/3)
    var score_sentance = "SUMMARY OF DAY "+day_number+": You ate "+ getPlayerScoreforDay(me,day_number) +" calories today. "

    var framing_sentance = ""
    if (grp =="loss") {
      framing_sentance = "If you EAT " + (totalPossiblePoints - getPlayerScoreforDay(me,day_number))+
       " more calories you are at a HIGHER RISK for type 2 diabetes. "
    }
    // if (grp == "loss" SOMETHING that indicates the round number: roundNumber%3 or %6 as it will be multiples of 3)
    //framing_sentance = "Wow, you sure ATE a LOT of calories. You are at a HIGHER RISK for suffering a STROKE. " }

    else if (grp =="gain"){
      framing_sentance = "if you AVOID " + (getPlayerScore(me) - totalPossiblePoints) +
       " more you are at a LOWER RISK for type 2 diabetes. "
      //can I make it switch from type 2 diabetes, heart attack, and something else?
    }
    //framing_sentance = "Wow, you sure AVOIDED a lot of calories. You are at a LOWER RISK for suffering a STROKE. " }
    //var continue_sentance = "Get ready for the next goal! "

    return score_sentance + framing_sentance ;
  }
});
