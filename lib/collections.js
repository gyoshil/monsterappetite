
Games = new Mongo.Collection('games');
/*  { clock: Int
    , players: [{player_id : Int, cards : [cards]}]
    , rounds: [ [card] ] //the current round is the last in this list
    }
   */

Players = new Mongo.Collection('players');
/* {  name: String
    , avatar: Int
    , game_id: Int //for now, a player can only exist for a single game. a new user is created everytime we go to lobby.
    , performance : [Double] //what % of possible pts did they get for every round
    }
*/
DECK = new Mongo.Collection('deck');


if (Meteor.isServer) {
  // publish all the non-idle players.
  Meteor.publish('players', function () {
    return Players.find();
  });

  Meteor.publish('deck', function () {
    return DECK.find();
  });

  // publish single games
  Meteor.publish('games', function (id) {
    check(id, String);
    console.log("subscripbing to");//TODO this subscribes to all games from the user, not just the current one
    console.log(Games.find({players: { $elemMatch : {_id : id}}}).fetch());
    return (Games.find({players: { $elemMatch : {_id : id}}}));
  });
}
