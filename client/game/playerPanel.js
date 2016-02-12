
//This part shows the entire section that lists scores, selected items, avatar
Template.playerPanel.helpers({
  show : function () {
    // !! is turning the object into a boolean
    var me = player();
    return !!game(me);
  },
  players : function () {
    var me = player();
    return game(me).players;
  },
  instructions : function () {
    var me = player();
    var grp = getGroup(me);
      
      if(grp =="loss"){ 
        return "MORE"
      }
      else if (grp =="gain"){
        return "LESS"
      }
  }
});

Template.player.helpers({
  winner : function () {
  //the following winner function was brought back from being commented out and
  //nothing happens. Winner still doesn't show up.
  var me = player();
  var g = game(me);
  if (g.winners && _.include(g.winners, this._id))
    return 'winner';
    return '';
  },

  // how total score is added (selected items show their individual scores even w/o this code,
  // but TOTAL is not calculated w/o this section)
  total_score : function () {
    var me = player();
    var total_score = getPlayerScore(me);

    var oldVal = $("#total_score").text();
    if (oldVal != total_score) {
      foo(oldVal,total_score);
    }

    function foo(oldV,newV) {
      var $el = $("#total_score"),
          value = newV;

      $({percentage: oldV}).stop(true).animate({percentage: value}, {
        duration : 500,
        easing: "linear",
        step: function () {
            // percentage with 1 decimal;
            var percentageVal = Math.round(this.percentage);
            $el.text(percentageVal);
           }
        }).promise().done(function () {
          // hard set the value after animation is done to be
          // sure the value is correct
          $el.text(value);
        });
   };
  },

  //this 'updates' the avatar id every second
  //not good, but works
  random_monster : function () {
    var me = player();
    return random_monster(getPlayerScore(me),me.avatar);
  },

  monster_size : function () {
    //return 'width:'+ '128' + 'px; height:128px';
    return '250px';
  },
  cards : function() {
    var me = player();
    g = game(me);
    console.log(g.players.find(matchesP).card_set);
    return g.players.find(matchesP).card_set.reverse();
  }
});
