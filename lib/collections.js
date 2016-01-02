
Games = new Mongo.Collection('games');

Players = new Mongo.Collection('players');

DECK = new Mongo.Collection('deck');

SNACKAZON_DECK = new Mongo.Collection('snackazon_deck');


if (Meteor.isServer) {
  // publish all the non-idle players.
  Meteor.publish('players', function () {
    return Players.find();
  });

  Meteor.publish('deck', function () {
    return DECK.find();
  });

  Meteor.publish('snackazon_deck', function () {
    return SNACKAZON_DECK.find();
  });

  // publish single games
  Meteor.publish('games', function (id) {
    check(id, String);
    console.log("subscripbing to");//TODO this subscribes to all games from the user, not just the current one
    console.log(Games.find({players: { $elemMatch : {_id : id}}}).fetch());
    return (Games.find({players: { $elemMatch : {_id : id}}}));
  });
}
