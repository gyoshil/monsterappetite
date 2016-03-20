import bson
from bson.codec_options import CodecOptions
from pprint import pprint
import csv

import calculate_N


dataDir = 'C:/Users/GGU/Documents/GitHub/monsterappetite/analysis/Qualtrics/'
bson_file = open('C:/Users/GGU/Documents/GitHub/monsterappetite/analysis/players.bson','rb')
mondgoDBplayers = bson.decode_all(bson_file.read())



###### FUCNTIONS #####
def gatherPlayers(session,condition):

  finishedSession_ids = calculate_N.gatherPlayers(session,condition)
  high_risk_participant_ids = []

  csvFile = "BIQ1.csv"
  #['uid', 'V1', 'V8', 'V9', 'Q2_1', 'Q3_1', 'Q4_1', 'Q6_1', 'Q7_1', 'Q8_1', 'Q9_1', 'Q10_1', 'Q11_1', 'Q12_1', 'Q13_1']
  id_index1 = 4
  id_index2 = 5
  id_index3 = 7
  id_index4 = 8

  with open(dataDir+csvFile, mode='r') as infile:
    qualtrics = csv.reader(infile)
    count =0

    def q2(player):return (player[id_index1]) =='4' or player[id_index1] =='5'
    def q3(player):return (player[id_index2]) =='4' or player[id_index2] =='5'
    def q6(player):return (player[id_index3]) =='1' or player[id_index3] =='2'
    def q7(player):return (player[id_index4]) =='1' or player[id_index4] =='2'

    for player in qualtrics:
      if ((player[0] in finishedSession_ids) and
        (   q2(player)
        or q3(player)
        or q6(player)
        or q7(player))
          ):
        participants.append("high")
      else:
        participants.append("low")

    return participant_ids





###### MAIN ########
def high_risk_results (condition):
  global count, session1pre, session2pre, session1post, session2post, num_p

  session1pre = 0
  session1post = 0
  session2pre = 0
  session2post = 0
  high_risk_participant_ids = gatherPlayers(1,condition)
  print (str(len(high_risk_participant_ids))+" high risk participants being considered")
  print ("who finsihed only Session 1")
  for p in mondgoDBplayers:
    if(p['_id'] in high_risk_participant_ids):
      gatherClicks(p)
  print ("1Preclicks  : "+str(session1pre))
  print ("1Postclicks : "+str(session1post))
  print (session1post/session1pre)
  print ()

  session1pre = 0
  session1post = 0
  session2pre = 0
  session2post = 0
  high_risk_participant_ids = gatherPlayers(2,condition)
  print (str(len(high_risk_participant_ids))+" high risk participants being considered")
  print ("who finsihed Session 2")
  for p in mondgoDBplayers:
    if(p['_id'] in high_risk_participant_ids):
      gatherClicks(p)
  print ("1Preclicks  : "+str(session1pre))
  print ("1Postclicks : "+str(session1post))
  print (session1post/session1pre)

  print ("2Preclicks  : "+str(session2pre))
  print ("2Postclicks : "+str(session2post))
  print (session2post/session2pre)
