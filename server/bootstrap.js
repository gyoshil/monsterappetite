Meteor.startup(function() {
  SNACKAZON_DECK.remove({});
  DECK.remove({});
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
          SNACKAZON_DECK.insert(card);
      }
    }
  }
});
