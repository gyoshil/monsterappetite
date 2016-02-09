
// generate a new random selection of cards.
new_board = function () {
  var board = [];
  var i;

  // pick random card from deck
  for (i = 0; i < 16; i += 1) {
    board[i] = Random.choice(DECK.find().fetch());
  }

  // knuth shuffle
  // This section displays the food cards on the board for each round. w/o this only monsters appear
  // on the board in each round.
  for (i = 15; i > 0; i -= 1) {
    var j = Math.floor(Math.random() * (i + 1));
    var tmp = board[i];
    board[i] = board[j];
    board[j] = tmp;
  }
  return board;
};

lowest_possible_score = function(board) {
  board.sort(function(a,b){
    //ascending order
    return a.calories - b.calories;
  });
  return sumTopThree(board)
};

highest_possible_score = function(board) {

  var b = board.sort(function(a,b){
    //decending order
    return b.calories - a.calories;
  });
  return sumTopThree(b)
};

sumTopThree = function(board) {
  var sum = 0;
  for (var i = 0; i < 3; i++) {
    sum+=board[i].calories;
  };
  return sum;
};

roundsPerGame = 21;

sendEmail = function(player) {
  if (Meteor.isServer) {
    sender = "monsterappetite499@gmail.com"
    recipient = player.email
    toSendTime = Date.Now() + 60*60
    //toSendTime = Date.Now() + 24*60*60

    //we need to make a login page -- DONE !!
    linkToPlay = "monster-appetitie.com/login?uid="+player._id

    Email.send({
      from: sender,
      to: recipient,
      subject: "Monster Appetite study Session 2",
      text: "Thank you for participating in the Monster Appetite study. Session 2 will complete your participation
      in this study. Please continue the study at "+linkToPlay+". We apprecoate your time."
      setSendAt: toSendTime
    });
  }