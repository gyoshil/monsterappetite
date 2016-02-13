Meteor.startup(function () {

//all this is taken care of by mup.json
//this is just for testing - comment out when deploying
  u="monsterappetite499"
  p = "m0nster99!"
  process.env.MAIL_URL = 'smtp://'+u+':'+p+'@smtp.gmail.com:587';
  //process.env.MAIL_URL = 'smtp://localhost:25';


  FutureTasks.find().forEach(function(mail) {
    if (mail.date < new Date()) {
	  FutureTasks.remove(mail._id);
  	  SyncedCron.remove(mail._id);
      Meteor.call('sendMail',mail)
    } else {
      Meteor.call('addTask',mail._id, mail);
    }
  });
  SyncedCron.start();
});

// In this case, "details" should be an object containing a date, plus required e-mail details (recipient, content, etc.)
Meteor.methods ({

sendMail : function(details) {

  // Let other method calls from the same client start running,
  // without waiting for the email sending to complete.
  this.unblock();

	Email.send({
		from: "monsterappetite499@gmail.com",
	  to: details.to,
    subject: details.subject,
    text: details.text
	});
},

 addTask:function(id, details) {

	SyncedCron.add({
		name: id,
		schedule: function(parser) {
			return parser.recur().on(details.date).fullDate();
		},
		job: function() {
			Meteor.call('sendMail',details);
			FutureTasks.remove(id);
			SyncedCron.remove(id);
    		return id;
		}
	});

},

 scheduleMail:function(details) {

	if (details.date < new Date()) {
		Meteor.call('sendMail',details);
	} else {
		var thisId = FutureTasks.insert(details);
		Meteor.call('addTask',thisId, details);
	}
	return true;

}

});
