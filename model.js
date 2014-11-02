////////// Shared code (client and server) //////////

Games = new Mongo.Collection('games');
// { board: ['A','I',...], clock: 60,
//   players: [{player_id, name}], winners: [player_id] }

Words = new Mongo.Collection('words');
// {player_id: 10, game_id: 123, word: 'hello', state: 'good', score: 4}

Players = new Mongo.Collection('players');
// {name: 'matt', game_id: 123}


/////////////////////////////////////////////////////////////////
//ADDED
Rounds = new Mongo.Collection('rounds');
// {player_id: 10, game_id: 123, word: 'hello', state: 'good', score: 10}

// 6 faces per die, 16 dice.  Q really means Qu.
//
//
// 16 dice with 6 faces will result in 96 food items in total (I have 99 items in total)
// What is an efficient way to declare each die that has 6 sides of different food items?
var DECK = [
            
            //pairs that are on the pre and post test
            {card_name:'goldencrisp',calories:147},
            {card_name:'luckycharms',calories:147},

            {card_name:'jujubes',calories:110},
            {card_name: 'trolli_crawlers', calories:110},


            {card_name:'salsa',calories:10},
            {card_name:'smuckers',calories:50},
            {card_name:'hersheys',calories:60},
            {card_name:'lays_dip',calories:60},
            {card_name:'popcorn',calories:80},
            {card_name:'caramel',calories:170},
            {card_name:'butterfinger_stixx',calories:90},
            {card_name:'cheezwhiz',calories:90},
            {card_name:'fudgesicle',calories:100},
            {card_name:'klondike',calories:100},
            {card_name:'chocolate_IC',calories:100},
            {card_name:'hummus',calories:35},
            {card_name:'nutrigrain_nuts',calories:140},
            {card_name:'soycrisps_cheddar',calories:120},
            {card_name:'ritz_sourcream',calories:130},
            {card_name:'pumpernickel_pretzels',calories:130},
            
            {card_name:'nutrigrain_rasberry',calories:140},
            {card_name:'almondcrisps',calories:140},
            {card_name:'honey_cheerios',calories:160},
            {card_name:'breyers_ICsandwich',calories:160},
            {card_name:'rye_chips',calories:160},
            {card_name:'reeses_puffs_cereal',calories:160},
            {card_name:'hostess_cupcake',calories:180},
            {card_name:'hostess_suzyQ',calories:220},
            {card_name:'m&m_ICsandwich',calories:220},
            {card_name:'reeses_bigcup',calories:230},
            {card_name:'strawberry_shortcake',calories:240}, 
            {card_name:'butterfinger',calories:270}, 
            {card_name:'twix_PB',calories:280}, 
            {card_name:'brownies',calories:280}, 
            {card_name:'haagendazs_vanilla',calories:290}, 
            {card_name:'whitecastle_CB',calories:310}, 
            {card_name:'nestle_drumstick',calories:360}, 
            {card_name:'quakes_rice_snacks',calories:140}, 
            {card_name:'redhots',calories:120}, 
            {card_name:'ruffles_cheddar',calories:160}, 
            {card_name:'snyders_pretzel',calories:100}, 
            {card_name:'stacys_pitachips_parmesan',calories:140}, 
            {card_name:'thousand_island',calories:140}, 
            {card_name:'tollhouse_ICsandwich',calories:499}, 
            {card_name:'smartfood_whitecheddar',calories:160}, 
            
            {card_name:'cheerios_snackmix',calories:120},  
            {card_name:'pretzel_flatz',calories:120},
            {card_name:'chexmix',calories:130},
            {card_name:'lifesaver_gummies',calories:130},
            {card_name:'entenmanns_donuts',calories:310},
            {card_name:'frootloops',calories:110},
            {card_name:'pecan',calories:210},
            {card_name:'calzone',calories:560},
            {card_name:'smuckers_raspberry',calories:50},
            {card_name:'mike&ike',calories:140},
            {card_name:'nillawafers',calories:140},
            {card_name:'capn_crunch',calories:147},
            {card_name:'fiberone_oats_chocolate',calories:140},
            {card_name:'munchies_ranch',calories:140},
            {card_name:'oreo_cakesters',calories:250},
            {card_name:'twinkies',calories:300},
            {card_name:'fudge_brownies',calories:310},
            {card_name:'nestle_drumstick',calories:360},
            {card_name:'oatmeal_creampie',calories:470},
            {card_name:'applecinnamon_cheerios',calories:160},
            {card_name:'goldfish',calories:150},
            {card_name:'zingers',calories:150},
            {card_name:'cheezit',calories:160},

            {card_name:'golden_grahams',calories:160},
            {card_name:'tartar_sauce',calories:160},
            {card_name:'honeynut_cheerios_bar',calories:160},
            {card_name:'starburst',calories:160},
            {card_name:'lindt_dark',calories:210},
            {card_name:'m&m-peanut',calories:220},
            {card_name:'starbucks_coffee_IC',calories:250},
            {card_name:'onionrings',calories:230},
            ];

// generate a new random selection of letters.
new_board = function () {
  var board = [];
  var i;

  // pick random letter from each die
  for (i = 0; i < 16; i += 1) {
    board[i] = Random.choice(DECK);
  }

  // knuth shuffle
  // pretty sure un-needed now, doesnt hurt tho
  for (i = 15; i > 0; i -= 1) {
    var j = Math.floor(Math.random() * (i + 1));
    var tmp = board[i];
    board[i] = board[j];
    board[j] = tmp;
  }
  return board;
};

Meteor.methods({
    score_card: function (card_name) {
    //find card name in DECK and get score
    /*for (var i = DECK.length - 1; i >= 0; i--) {
      if(DECK[i].card_name == card_name){
        return DECK[i].calories;
      }
    };*/

    /*if (game.clock === 0){
      return;
    }
    var card = Words.findOne(card_id);

    Words.update(card._id, {$set: {score: score, state: 'good'}});
    */
  },
  score_word: function (word_id) {
    check(word_id, String);
    var word = Words.findOne(word_id);
    var game = Games.findOne(word.game_id);
    ////////////////////////////////////////// at this point is it thinking words are the FOOD CARDS????
    var round = Rounds.findOne(word.round_id); 
    // client and server can both check that the game has time remaining, and
    // that the word is at least three chars, isn't already used, and is
    // possible to make on the board.
    if (game.clock === 0
        || !word.word
        || word.word.length < 3
        || Words.find({game_id: word.game_id, word: word.word}).count() > 1
        || paths_for_word(game.board, word.word).length === 0) {
      Words.update(word._id, {$set: {score: 0, state: 'bad'}});
      return;
    }
  ////////////////////////////////////////////////////////////////  
  //I added this HERE!  
  // is this the right place for this fxn??? 
  /*new_round: function (round_id) {
    check(game_id, player_id);
    var game = Games.findOne(game_id);
    var player = Player.findOne(game.player_id);
  }*/
});


if (Meteor.isServer) {
  // publish all the non-idle players.
  Meteor.publish('players', function () {
    return Players.find({idle: false});
  });

  // publish single games
  Meteor.publish('games', function (id) {
    check(id, String);
    return Games.find({_id: id});
  });

  // publish all my words and opponents' words that the server has
  // scored as good.
  Meteor.publish('words', function (game_id, player_id) {
    check(game_id, String);
    check(player_id, String);
    return Words.find({$or: [{game_id: game_id, state: 'good'},
                             {player_id: player_id}]});
  });
}
