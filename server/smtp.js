Meteor.startup(function () {
//  u="monsterappetite499"
//  p = "m0nster99!"
//  process.env.MAIL_URL = 'smtp:///'+u+':'+p+'@smtp.gmail.com:587';


  FutureTasks.find().forEach(function(mail) {
    if (mail.date < new Date()) {
      sendMail(mail)
    } else {
      addTask(mail._id, mail);
    }
  });
  SyncedCron.start();
});


// In this case, "details" should be an object containing a date, plus required e-mail details (recipient, content, etc.)
Meteor.methods ({

sendMail : function(details) {

  console.log("sent an email to "+details.to)
  console.log(details);
  // Let other method calls from the same client start running,
  // without waiting for the email sending to complete.
  this.unblock();

	Email.send({
		from: "root@monster",
	  to: details.to,
    subject: details.subject,
    text: details.text
	});
},

//"Thank you for participating in the study (IRB 16-145). Your monster name for this study is "+name+
// ". You don't have to take any further actions regarding this email. This is just to confirm your email address."


 addTask:function(id, details) {

	SyncedCron.add({
		name: id,
		schedule: function(parser) {
			return parser.recur().on(details.date).fullDate();
		},
		job: function() {
			sendMail(details);
			FutureTasks.remove(id);
			SyncedCron.remove(id);
	        	return id;
		}
	});
  console.log("scehduled to send")
  console.log(details);

},

 scheduleMail:function(details) {

	if (details.date < new Date()) {
		sendMail(details);
	} else {
		var thisId = FutureTasks.insert(details);
		addTask(thisId, details);
	}
	return true;

}

});

/*
send_email: function(email,name){
  console.error(name);
  console.log(email);



  //actual email sending method
  Email.send({
    to: email,
    from: "monsterappetite499@gmail.com",
    subject: "Monster Appetite",
    text: "Thank you for participating in the study (IRB 16-145). Your monster name for this study is "+name+ ". You don't have to take any further actions regarding this email. This is just to confirm your email address."
  });
},*/
