Meteor.startup(function() {
  if (DECK.find().count() === 0) {
    var allText = Assets.getText("foodcard_database.csv");
    var allTextLines = allText.split(/\r|\n/);
    var headers = allTextLines[0].split(',');
    //card_name,image_location,calories,fat,sugars,type

    for (var i=1; i<allTextLines.length; i++) {
      var data = allTextLines[i].split(',');
      if (data.length == headers.length) {

          var card = {};
          for (var j=0; j<headers.length; j++) {
            card[headers[j]] = data[j];
            if (j==2) {//calopries should be numbers so we can add later
              card[headers[j]] = parseInt(data[j]);
            }
          }
          DECK.insert(card);
      }
    }
  }
});


SNACKAZON_DECK = [
            //first set of choices
            {card_name:'Brownies_Beaver',calories:110, source_:"local", ingredients: "chocolate + eggs", protein:"none" },
            {card_name:'Brownies_Monkey',calories:90, source_:"local", ingredients: "chocolate", protein:"none" },
            {card_name:'Brownies_Panda',calories:180, source_:"non-local", ingredients: "chocolate", protein:"none" },
            //second set of choices
            {card_name:'goldencrisp',calories:147, source_:"non-local", ingredients: "honey" },
            {card_name:'luckycharms',calories:147, source_:"non-local", ingredients: "sugar" },
            {card_name:'golden_grahams',calories:160, source_:"local", ingredients: "cinnamon" },
            //third set of choices
            {card_name:'trolli_crawlers', calories:110, ingredients: "sugar", source_:"non-local"},
            {card_name:'starburst',calories:160, ingredients: "sugar", source_:"non-local"},
            {card_name:'mike&ike',calories:140, ingredients: "sugar",  source_:"non-local"},
];
