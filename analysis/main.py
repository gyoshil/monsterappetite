import higher_order

import query_dbs
import infoSeekingClicks
from pprint import pprint
import sys

import csv_printer
import research_questions
import card_info


all = query_dbs.allMongoPlayers()

########
# SNACKZON
#######
def sic(p):
  player = query_dbs.findPlayerInMongo('_id',p[0])
  return len(player['snackazonItemChoices'])
query_dbs.tagMongoPlayers(all,sic)


def snackChoice(round,p):
  player = query_dbs.findPlayerInMongo('_id',p[0])
  score = 0

  if ((round+1)*5>len(player['snackazonItemChoices'])):
    return "empty"
  for i in player['snackazonItemChoices']:
    if i['item']['round'] > (round *5) and i['item']['round'] <= ((round+1) *5):
      if i['item']['card_name'] in card_info.bad_cards :
        score += (-1)
      elif i['item']['card_name'] in card_info.ok_cards :
        score += 0
      elif i['item']['card_name'] in card_info.good_cards :
        score += 1
  return score

def snackChoicePre1(p) : return snackChoice(0,p)
def snackChoicePost1(p) : return snackChoice(1,p)
def snackChoicePre2(p) : return snackChoice(2,p)
def snackChoicePost2(p) : return snackChoice(3,p)


query_dbs.tagMongoPlayers(all,snackChoicePre1)
query_dbs.tagMongoPlayers(all,snackChoicePost1)
query_dbs.tagMongoPlayers(all,snackChoicePre2)
query_dbs.tagMongoPlayers(all,snackChoicePost2)




########
# PDQ COMPLETION
#######
def completedPDQ(mongoP,qualtricsP):
  return (qualtricsP!="NONE")
query_dbs.tagCSVPlayers("PDQ1.csv",all,"completedPDQ1",completedPDQ)
query_dbs.tagCSVPlayers("PDQ2.csv",all,"completedPDQ2",completedPDQ)
query_dbs.tagCSVPlayers("PDQ3.csv",all,"completedPDQ3",completedPDQ)
query_dbs.tagCSVPlayers("PDQ4.csv",all,"completedPDQ4",completedPDQ)

######
# RISK
######
def csv_answer_check(mongoP,qualtricsP,answer_checks):
  if(qualtricsP=="NONE"):
    return "empty"
  meets_condition = False
  for a in answer_checks:
    meets_condition = meets_condition or (qualtricsP[a[0]] ==str(a[1]))
  return meets_condition

def risk_level(mongoP,qualtricsP):
  if(qualtricsP=="NONE"):
    return "empty"
  good_answers = [(4,4),(4,5),(5,4),(5,5),(7,1),(7,2),(8,1),(8,2)]
  if(csv_answer_check(mongoP,qualtricsP,good_answers)):
    return "1"
  return "0"
query_dbs.tagCSVPlayers("BIQ1.csv",all,"risk_level_pre1",risk_level)
query_dbs.tagCSVPlayers("BIQ2.csv",all,"risk_level_post1",risk_level)
query_dbs.tagCSVPlayers("BIQ3.csv",all,"risk_level_pre2",risk_level)
query_dbs.tagCSVPlayers("BIQ3.csv",all,"risk_level_post2",risk_level)

########
# Calories
########
def calorie_seeker(mongoP,qualtricsP):
  if(qualtricsP=="NONE"):
    return "empty"
  good_answers = [(6,4),(6,5)]
  return csv_answer_check(mongoP,qualtricsP,good_answers)

query_dbs.tagCSVPlayers("BIQ1.csv",all,"calorie_seeker_pre1",calorie_seeker)
query_dbs.tagCSVPlayers("BIQ2.csv",all,"calorie_seeker_post1",calorie_seeker)
query_dbs.tagCSVPlayers("BIQ3.csv",all,"calorie_seeker_pre2",calorie_seeker)
query_dbs.tagCSVPlayers("BIQ3.csv",all,"calorie_seeker_post2",calorie_seeker)

########
# PDQ
#######
def calorie_influence(mongoP,qualtricsP):
  if(qualtricsP=="NONE"):
    return "empty"
  x = qualtricsP[18]
  if(x==""): x=0
  return x

query_dbs.tagCSVPlayers("PDQ1.csv",all,"calorie_influence_pre1",calorie_influence)
query_dbs.tagCSVPlayers("PDQ2.csv",all,"calorie_influence_post1",calorie_influence)
query_dbs.tagCSVPlayers("PDQ3.csv",all,"calorie_influence_pre2",calorie_influence)
query_dbs.tagCSVPlayers("PDQ3.csv",all,"calorie_influence_post2",calorie_influence);

def calorie_influence_fake(qs,mongoP,qualtricsP):
  if(qualtricsP=="NONE"):
    return "empty"
  x = 0
  for q in qs:
    if(qualtricsP[q]!=""):
      x += (1/int(qualtricsP[q]))
  return x

def calorie_influence_pre1_fake(m,q) : return calorie_influence_fake([18,50,66],m,q)
def calorie_influence_post1_fake(m,q) : return calorie_influence_fake([34,50,66],m,q)
def calorie_influence_pre2_fake(m,q) : return calorie_influence_fake([18,66,82],m,q)
def calorie_influence_post2_fake(m,q) : return calorie_influence_fake([18,66,82],m,q)

query_dbs.tagCSVPlayers("PDQ1.csv",all,"calorie_influence_pre1_fake",calorie_influence_pre1_fake)
query_dbs.tagCSVPlayers("PDQ2.csv",all,"calorie_influence_post1_fake",calorie_influence_post1_fake)
query_dbs.tagCSVPlayers("PDQ3.csv",all,"calorie_influence_pre2_fake",calorie_influence_pre2_fake)
query_dbs.tagCSVPlayers("PDQ3.csv",all,"calorie_influence_post2_fake",calorie_influence_post2_fake);
########
# DQ
#######
def dq(q_num,mongoP,qualtricsP):
  if(qualtricsP=="NONE"):
    return "empty"
  x = qualtricsP[q_num]
  return x

def dq2(m,q) : return dq(3,m,q)
def dq3(m,q) : return dq(4,m,q)
def dq4(m,q) : return dq(5,m,q)
def dq5(m,q) : return dq(6,m,q)
def dq6(m,q) : return dq(7,m,q)
def dq7(m,q) : return dq(8,m,q)
def dq8(m,q) : return dq(9,m,q)

query_dbs.tagCSVPlayers("DQ.csv",all,"dq2",dq2)
query_dbs.tagCSVPlayers("DQ.csv",all,"dq3",dq3)
query_dbs.tagCSVPlayers("DQ.csv",all,"dq4",dq4)
query_dbs.tagCSVPlayers("DQ.csv",all,"dq5",dq5)
query_dbs.tagCSVPlayers("DQ.csv",all,"dq6",dq6)
query_dbs.tagCSVPlayers("DQ.csv",all,"dq7",dq7)
query_dbs.tagCSVPlayers("DQ.csv",all,"dq8",dq8)


########
# FFQ 1st
#######
def ffq1_risk(mongoP,qualtricsP):
  if(qualtricsP=="NONE"):
    return "empty"
  good_answers = [(2,1),(2,2),
                  (3,1),(3,2),
                  (12,1),(12,2),(12,3),
                  (13,1),(13,2),(13,3),
                  (14,1),(14,2),(14,3)]
  if(csv_answer_check(mongoP,qualtricsP,good_answers)):
    return "1"
  return "0"

query_dbs.tagCSVPlayers("FFQ1.csv",all,"ffq1_risk",ffq1_risk)




########
# FFQ 2nd
#######
score = 0
def ffq2_score(mongoP,qualtricsP):
  global score
  if(qualtricsP=="NONE"):
    return "empty"
  score = 0
  completed = 23 #(22 now tho...)
  def check2(q) :
    global score
    if (qualtricsP[q]=='2'): score+=1
  def check1(q) :
    global score
    if (qualtricsP[q]=='1'): score+=1
  #healthy answer is 2
  healthy2 = [4,9,16,20,24]
  #healthy answer is 1
  healthy1 = [2,3,5,6,7,8,10,11,13,14,15,17,18,19,21,23]
  #no 12 and 22 (see attention_pass)

  for n in healthy1:
    check1(n)
  for n in healthy2:
    check2(n)

  return score*(23/completed)

query_dbs.tagCSVPlayers("FFQ2.csv",all,"ffq2_score",ffq2_score)


########
## INFO SEEKING
#######
def pre1_getInfo(p): return infoSeekingClicks.gatherClicks(1,0,p)
def pre1_moreInfo(p): return infoSeekingClicks.gatherClicks(2,0,p)
query_dbs.tagMongoPlayers(all,pre1_getInfo)
query_dbs.tagMongoPlayers(all,pre1_moreInfo)

def post1_getInfo(p): return infoSeekingClicks.gatherClicks(1,1,p)
def post1_moreInfo(p): return infoSeekingClicks.gatherClicks(2,1,p)
query_dbs.tagMongoPlayers(all,post1_getInfo)
query_dbs.tagMongoPlayers(all,post1_moreInfo)

def pre2_getInfo(p): return infoSeekingClicks.gatherClicks(1,2,p)
def pre2_moreInfo(p): return infoSeekingClicks.gatherClicks(2,2,p)
query_dbs.tagMongoPlayers(all,pre2_getInfo)
query_dbs.tagMongoPlayers(all,pre2_moreInfo)

def post2_getInfo(p): return infoSeekingClicks.gatherClicks(1,3,p)
def post2_moreInfo(p): return infoSeekingClicks.gatherClicks(2,3,p)
query_dbs.tagMongoPlayers(all,post2_getInfo)
query_dbs.tagMongoPlayers(all,post2_moreInfo)

########
## INFO SEEKING FAKE
#######
def pre1_getInfo_fake(p): return infoSeekingClicks.gatherClicksFake(1,0,p)
def pre1_moreInfo_fake(p): return infoSeekingClicks.gatherClicksFake(2,0,p)
query_dbs.tagMongoPlayers(all,pre1_getInfo_fake)
query_dbs.tagMongoPlayers(all,pre1_moreInfo_fake)

def post1_getInfo_fake(p): return infoSeekingClicks.gatherClicksFake(1,1,p)
def post1_moreInfo_fake(p): return infoSeekingClicks.gatherClicksFake(2,1,p)
query_dbs.tagMongoPlayers(all,post1_getInfo_fake)
query_dbs.tagMongoPlayers(all,post1_moreInfo_fake)

def pre2_getInfo_fake(p): return infoSeekingClicks.gatherClicksFake(1,2,p)
def pre2_moreInfo_fake(p): return infoSeekingClicks.gatherClicksFake(2,2,p)
query_dbs.tagMongoPlayers(all,pre2_getInfo_fake)
query_dbs.tagMongoPlayers(all,pre2_moreInfo_fake)

def post2_getInfo_fake(p): return infoSeekingClicks.gatherClicksFake(1,2,p)
def post2_moreInfo_fake(p): return infoSeekingClicks.gatherClicksFake(2,2,p)
query_dbs.tagMongoPlayers(all,post2_getInfo_fake)
query_dbs.tagMongoPlayers(all,post2_moreInfo_fake)

######
# GROUP
######
def group(p):
  player = query_dbs.findPlayerInMongo('_id',p[0])
  return player['group']
query_dbs.tagMongoPlayers(all,group)

######
# PERFORMANCE
######

# :: String -> Int -> [Int] -> Int
def collapseOneRound (group,prev_score,this_round):
  h = this_round[2]
  l = this_round[1]
  a = this_round[0]-prev_score
  score = (a-l)/(h-l)
  if(score<0 or score>1):
    print ("%s,%s,%s(%s) -> %s" % (h,l,a,this_round[0],score))

  return score

# :: Player -> [Int]
def collapseOnePlayer (mongoP):
  group = mongoP['group']
  rounds = mongoP['performance'] # [[Int]]
  prev_score = 0
  average_scores = []
  for r in rounds:
    r_avg = collapseOneRound(group,prev_score,r)
    average_scores.append(r_avg)
    prev_score = r[0]
    #print (mongoP[''])
  print()
  return average_scores

def average(l):
  return sum(l)/len(l)

#x = list(map(collapseOnePlayer,query_dbs.mongoPlayers))

#pprint (x)

'''
average_scores = [(0,0)]*23 #(avg,len)
for (round_num,round_avg_score) in enumerate(average_scores):
  round_score = []
  for p in all.items():
    player = query_dbs.findPlayerInMongo('_id',p[0])
    try :
      h = player['performance'][round_num]
      l = player['performance'][round_num]
      a = player['performance'][round_num]
      if (player['group']=='gain'):
        score = (l-h)/(a-h)
      if (player['group']=='loss'):
        score = (l-h)/(a-h)
      round_score.append(score)
    except:
      pass
    if (len(player['performance'])>0):
      print (player['performance'],end=', \n')

  sum_scores = sum(round_score)
  try:
    average_scores[round_num] = (sum_scores/len(round_score),len(round_score))
  except ZeroDivisionError:
    pass

pprint (average_scores)
'''


######
# FILTER ATTENTION
######
def attention_measure1(mongoP,qualtricsP):
  if(qualtricsP=="NONE"):
    return True
  good_answers = [(9,4)]
  if(csv_answer_check(mongoP,qualtricsP,good_answers)):
    return True
  return False

def attention_measure2(mongoP,qualtricsP):
  if(qualtricsP=="NONE"):
    return True
  good_answer1 = [(12,4)]
  good_answer2 = [(22,3)]
  if(csv_answer_check(mongoP,qualtricsP,good_answer1) and
     csv_answer_check(mongoP,qualtricsP,good_answer2)):
    return True
  return False

query_dbs.tagCSVPlayers("FFQ1.csv",all,"attention_measure1",attention_measure1)
query_dbs.tagCSVPlayers("FFQ2.csv",all,"attention_measure2",attention_measure2)

def attention_pass(p) :
  return (p['attention_measure2'] and p['attention_measure1'])

filtered_all = {k:v for (k,v) in all.items() if attention_pass(v)}

print ("Removed "+ str(len(all) - (len(filtered_all)))+" players who didnt pay attention\n")
######
# PRINT
######
csv_printer.printAll(filtered_all)

######
# ANSWERS TO RESEARCH QUESTIONS
######
print ("RQ1...\n")
research_questions.r1(filtered_all)
print ("DONE\n")

print ("\nRQ2...\n")
research_questions.r2(filtered_all)
print ("DONE\n")

print ("\nRQ3...\n")
research_questions.r3(filtered_all)
print ("DONE\n")

print ("\nRQ4...\n")
research_questions.r4(filtered_all)
print ("DONE\n")

print ("\nRQBONUS...\n")
research_questions.rBonus(filtered_all)
print ("DONE\n")

print ("\nRQBONUS2...\n")
research_questions.rBonus2(filtered_all)
print ("DONE\n")

######
# Change in snackazon choices
######

better = 0
worse = 0
same = 0

for (id,p) in all.items():
  if (not(p['snackChoicePre1']=='empty' or
      p['snackChoicePost1']=='empty' or
      p['snackChoicePre2']=='empty' or
      p['snackChoicePost2']=='empty')):
    '''print (str(p['snackChoicePre1']) +" "+str(p['snackChoicePost1'])
           +" "+str(p['snackChoicePre2'])+" "+str(p['snackChoicePost1']))'''
    if ((p['snackChoicePre1']+p['snackChoicePost1']) >
        (p['snackChoicePre2']+p['snackChoicePost2'])):
      worse += 1
    if ((p['snackChoicePre1']+p['snackChoicePost1']) <
        (p['snackChoicePre2']+p['snackChoicePost2'])):
      better += 1
    else :
      same += 1
  '''if ((p['snackChoicePre1']) >
      (p['snackChoicePost1'])):
    worse += 1
  elif ((p['snackChoicePre1']) <
      (p['snackChoicePost1'])):
    better +=1
print (better)
print (worse)
print (same)'''

finishedSession2 = 0
for (id,p) in all.items():
  if(p['completedPDQ4'] and p['sic']>=20): finishedSession2 +=1
#print (finishedSession2)
