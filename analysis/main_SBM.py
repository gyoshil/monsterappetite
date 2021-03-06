import higher_order

import query_dbs
import infoSeekingClicks
from pprint import pprint
import sys

import csv_printer
import research_questions
import card_info

#print (sys.getdefaultencoding())


all = query_dbs.allMongoPlayers()

########
# SNACKZON
#######
def sic(p):
  player = query_dbs.findPlayerInMongo('_id',p[0])
  return len(player['snackazonItemChoices'])
query_dbs.tagMongoPlayers(all,sic)

def times(p):
  player = query_dbs.findPlayerInMongo('_id',p[0])
  return len(player['snackazonItemChoices'])
query_dbs.tagMongoPlayers(all,times)

def group(p):
  player = query_dbs.findPlayerInMongo('_id',p[0])
  try:
      return player['group']
  except Exception as e:
      return "NA"
query_dbs.tagMongoPlayers(all,group)

def pop(p):
  player = query_dbs.findPlayerInMongo('_id',p[0])
  try:
      return (player['pop'])
  except Exception as e:
      return "NA"
query_dbs.tagMongoPlayers(all,pop)

def informationSeekingBehavior(p):
  player = query_dbs.findPlayerInMongo('_id',p[0])
  try:
      return (player['informationSeekingBehavior'])
  except Exception as e:
      return "NA"
query_dbs.tagMongoPlayers(all,informationSeekingBehavior)

# below DEFINES snackChoice function

def snackChoice(round,p):
  player = query_dbs.findPlayerInMongo('_id',p[0])
  score = 0
#round means pre1 = 0 , post1 = 1, pre2 = 2, or post2 = 3. Therefore, round starts from 0 to 4. 
  if ((round+1)*5>len(player['snackazonItemChoices'])):
    return "empty"
  for i in player['snackazonItemChoices']:
    if i['item']['round'] > (round *5) and i['item']['round'] <= ((round+1) *5):
      #this indicates that EACH ITEM is counted separately???
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
# BIQ RISK
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
    # "good_answers" below indicates that the person exhibits HIGH RISK LEVEL BEHAVIOR
    # the CSV questions related to risk level and calorie seeker are 2, 3, 4, 6, and 7 where 3 & 4 are calorie related Qs.
    # unfortunately, it was confusing becuase the numbers used for the "good_answers" coding below translates to 4, 5, 6, 7, 
    # and 8 where 5 & 6 are calorie related Qs.

  good_answers = [(4,4),(4,5),(5,1),(5,2),(7,4),(7,5),(8,4),(8,5)]
  if(csv_answer_check(mongoP,qualtricsP,good_answers)):
    return "1"
  return "0"
query_dbs.tagCSVPlayers("BIQ1.csv",all,"risk_level_pre1",risk_level)
query_dbs.tagCSVPlayers("BIQ2.csv",all,"risk_level_post1",risk_level)
query_dbs.tagCSVPlayers("BIQ3.csv",all,"risk_level_pre2",risk_level)
query_dbs.tagCSVPlayers("BIQ4.csv",all,"risk_level_post2",risk_level)

########
# BIQ Calories
########
def calorie_seeker(mongoP,qualtricsP):
  if(qualtricsP=="NONE"):
    return "empty"
    # "good_answers" below indicates that the person exhibits GOOD behavior (Calorie-seeking behavior which is ideal)
  good_answers = [(5,4),(5,5),(6,4),(6,5)]
  return csv_answer_check(mongoP,qualtricsP,good_answers)

query_dbs.tagCSVPlayers("BIQ1.csv",all,"calorie_seeker_pre1",calorie_seeker)
query_dbs.tagCSVPlayers("BIQ2.csv",all,"calorie_seeker_post1",calorie_seeker)
query_dbs.tagCSVPlayers("BIQ3.csv",all,"calorie_seeker_pre2",calorie_seeker)
query_dbs.tagCSVPlayers("BIQ4.csv",all,"calorie_seeker_post2",calorie_seeker)

########
# BIQ Calories QUESTION #2: how often snack this following week (actional intention)
########
def calorie_seeker_q2(mongoP,qualtricsP):
  if(qualtricsP=="NONE"):
    return "empty"
    # "good_answers" below indicates that the person exhibits GOOD behavior (Calorie-seeking behavior which is ideal)
  good_answers = [(3,1),(3,2),(3,3)]
  return csv_answer_check(mongoP,qualtricsP,good_answers)

query_dbs.tagCSVPlayers("BIQ1.csv",all,"calorie_seeker_q2_pre1",calorie_seeker_q2)
query_dbs.tagCSVPlayers("BIQ2.csv",all,"calorie_seeker_q2_post1",calorie_seeker_q2)
query_dbs.tagCSVPlayers("BIQ3.csv",all,"calorie_seeker_q2_pre2",calorie_seeker_q2)
query_dbs.tagCSVPlayers("BIQ4.csv",all,"calorie_seeker_q2_post2",calorie_seeker_q2)

########
# BIQ Calories QUESTION #3: how often check per-serv calories (info seeking intention)
########
def calorie_seeker_q3(mongoP,qualtricsP):
  if(qualtricsP=="NONE"):
    return "empty"
    # "good_answers" below indicates that the person exhibits GOOD behavior (Calorie-seeking behavior which is ideal)
  good_answers = [(4,4),(4,5)]
  return csv_answer_check(mongoP,qualtricsP,good_answers)

query_dbs.tagCSVPlayers("BIQ1.csv",all,"calorie_seeker_q3_pre1",calorie_seeker_q3)
query_dbs.tagCSVPlayers("BIQ2.csv",all,"calorie_seeker_q3_post1",calorie_seeker_q3)
query_dbs.tagCSVPlayers("BIQ3.csv",all,"calorie_seeker_q3_pre2",calorie_seeker_q3)
query_dbs.tagCSVPlayers("BIQ4.csv",all,"calorie_seeker_q3_post2",calorie_seeker_q3)

########
# BIQ Calories QUESTION #4: how often per-serv matter more than taste etc. (belief/attitude intention)
########
def calorie_seeker_q4(mongoP,qualtricsP):
  if(qualtricsP=="NONE"):
    return "empty"
    # "good_answers" below indicates that the person exhibits GOOD behavior (Calorie-seeking behavior which is ideal)
  good_answers = [(5,4),(5,5)]
  return csv_answer_check(mongoP,qualtricsP,good_answers)

query_dbs.tagCSVPlayers("BIQ1.csv",all,"calorie_seeker_q4_pre1",calorie_seeker_q4)
query_dbs.tagCSVPlayers("BIQ2.csv",all,"calorie_seeker_q4_post1",calorie_seeker_q4)
query_dbs.tagCSVPlayers("BIQ3.csv",all,"calorie_seeker_q4_pre2",calorie_seeker_q4)
query_dbs.tagCSVPlayers("BIQ4.csv",all,"calorie_seeker_q4_post2",calorie_seeker_q4)


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
query_dbs.tagCSVPlayers("PDQ4.csv",all,"calorie_influence_post2",calorie_influence);

def calorie_influence_fake(qs,mongoP,qualtricsP):
  if(qualtricsP=="NONE"):
    return "empty" # if this is referring to empty cells I need to switch this to ZERO, the number
  x = 0.0
  for q in qs:
    if(qualtricsP[q]!=""):
      x += (1.0/int(qualtricsP[q])) # here I would divide it by itself so it just counts as one
      # x += ( (int(qualtricsP[q]) / int(qualtricsP[q])) ) 
      # so the above would count each one as one point    
    #print (str(x)+ "gelato")
  return x

def calorie_influence_pre1_fake(m,q) : return calorie_influence_fake([18,50,66],m,q)
#def calorie_influence_pre1_fake(m,q) : return calorie_influence_fake
#([6,8,10,12,14,16,18,20,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68],m,q)

def calorie_influence_post1_fake(m,q) : return calorie_influence_fake([34,50,66],m,q)
#def calorie_influence_post1_fake(m,q) : return calorie_influence_fake
#([22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68],m,q)

def calorie_influence_pre2_fake(m,q) : return calorie_influence_fake([18,66,82],m,q)
#def calorie_influence_pre2_fake(m,q) : return calorie_influence_fake
#([6,8,10,12,14,16,18,20,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84],m,q)

#I am pretty sure the #s below have to be 50, 66, 82 (originally the #s were 18, 66, 82)
def calorie_influence_post2_fake(m,q) : return calorie_influence_fake([50,66,82],m,q)
#def calorie_influence_post2_fake(m,q) : return calorie_influence_fake
#([38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84],m,q)

query_dbs.tagCSVPlayers("PDQ1.csv",all,"calorie_influence_pre1_fake",calorie_influence_pre1_fake)
query_dbs.tagCSVPlayers("PDQ2.csv",all,"calorie_influence_post1_fake",calorie_influence_post1_fake)
query_dbs.tagCSVPlayers("PDQ3.csv",all,"calorie_influence_pre2_fake",calorie_influence_pre2_fake)
query_dbs.tagCSVPlayers("PDQ4.csv",all,"calorie_influence_post2_fake",calorie_influence_post2_fake);

########
# PDQ all cells produced for chi distribution analysis
#######

def pdq_chi_distribution(qs,mongoP,qualtricsP):
 if(qualtricsP=="NONE"): 
  return -1 
 
 y = ""
 for q in qs: 
  if (qualtricsP[q] == "1" or qualtricsP[q] == "2" or qualtricsP[q] == "3" ): 
    y += "1 "
  else :
    y += "0 "
 return y

def pdq_chi_distribution_pre1_fake(m,q) : return pdq_chi_distribution([6,8,10,12,14,16,18,20,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68],m,q)
def pdq_chi_distribution_post1_fake(m,q) : return pdq_chi_distribution([22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68],m,q)
def pdq_chi_distribution_pre2_fake(m,q) : return pdq_chi_distribution([6,8,10,12,14,16,18,20,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84],m,q)
def pdq_chi_distribution_post2_fake(m,q) : return pdq_chi_distribution([38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84],m,q)

query_dbs.tagCSVPlayers("PDQ1.csv",all,"pdq_chi_distribution_pre1_fake",pdq_chi_distribution_pre1_fake)
query_dbs.tagCSVPlayers("PDQ2.csv",all,"pdq_chi_distribution_post1_fake",pdq_chi_distribution_post1_fake)
query_dbs.tagCSVPlayers("PDQ3.csv",all,"pdq_chi_distribution_pre2_fake",pdq_chi_distribution_pre2_fake)
query_dbs.tagCSVPlayers("PDQ4.csv",all,"pdq_chi_distribution_post2_fake",pdq_chi_distribution_post2_fake);

########
# PDQ all cells produced for chi distribution with RANKED items coded by importance
#######

def pdq_chi_distribution2(qs,mongoP,qualtricsP):
 if(qualtricsP=="NONE"): 
  return -1 
 
 y = ""
 for q in qs: 
  if (qualtricsP[q] == "1" ): 
    y += "3 "
  elif (qualtricsP[q] == "3"):
    y += "1 "
  elif (qualtricsP[q] == "2"):
    y += "2 "
  else :
    y += ". "
 return y

def pdq_chi_distribution2_pre1_fake(m,q) : return pdq_chi_distribution2([6,8,10,12,14,16,18,20,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68],m,q)
def pdq_chi_distribution2_post1_fake(m,q) : return pdq_chi_distribution2([22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68],m,q)
def pdq_chi_distribution2_pre2_fake(m,q) : return pdq_chi_distribution2([6,8,10,12,14,16,18,20,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84],m,q)
def pdq_chi_distribution2_post2_fake(m,q) : return pdq_chi_distribution2([38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84],m,q)

query_dbs.tagCSVPlayers("PDQ1.csv",all,"pdq_chi_distribution2_pre1_fake",pdq_chi_distribution2_pre1_fake)
query_dbs.tagCSVPlayers("PDQ2.csv",all,"pdq_chi_distribution2_post1_fake",pdq_chi_distribution2_post1_fake)
query_dbs.tagCSVPlayers("PDQ3.csv",all,"pdq_chi_distribution2_pre2_fake",pdq_chi_distribution2_pre2_fake)
query_dbs.tagCSVPlayers("PDQ4.csv",all,"pdq_chi_distribution2_post2_fake",pdq_chi_distribution2_post2_fake);




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
  ###################
  ###################
  ######## I know at some point the score should have been calculated with a total of 22 questions. RIGHT???????

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

############# JUST FOUND OUT that below at the end in the parentheses
############# it was (1,2,p) & (2,2,p) 
############# but that means pre2 data are being collected. 
############# so I am switching to (1,3,p) & (2,3,p)
def post2_getInfo_fake(p): return infoSeekingClicks.gatherClicksFake(1,3,p)
def post2_moreInfo_fake(p): return infoSeekingClicks.gatherClicksFake(2,3,p)
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
#Below printed all data with filters applied
#csv_printer.printAll(filtered_all)

######
# ANSWERS TO RESEARCH QUESTIONS
#####
####### SBM FROM HERE

print ("\nSBM_BIQ...\n")
research_SBM.r1_SBM(filtered_all)
print ("DONE\n")




######
# Change in snackazon choices
######

better = 0
worse = 0
same = 0

better1 = 0
worse1 = 0
same1 = 0

better2 = 0
worse2 = 0
same2 = 0

datasetCounter = 0

print (len(all))
print (len(str(attention_measure2)))
print (len(str(filtered_all)))

for (id,p) in all.items(): 
  #if even one of them does not have a score (if it is empty) // 
  #so this means among the three fake items per section (pre1, post1, etc.) if you even have one you have not chosen, 
  #then it was recorded as empty. This filter is different than any other filters throughout this code. 
  
  #print (len(filtered_all)) --- this gives you 288 unique data sets
  if ((not(p['snackChoicePre1']=='empty' or
      p['snackChoicePost1']=='empty' or
      p['snackChoicePre2']=='empty' or
      p['snackChoicePost2']=='empty'))
      #HERE I want to add filters that were applied in other RQs and other CSVs produced
      #and (p['attention_measure2'] and p['attention_measure1'])
      #and (p['completedPDQ2'] and p['completedPDQ4'])
      and (p['completedPDQ2']==True)
      and (p['completedPDQ4']==True)
      ):

      #############################
      ###
      #   These are the filters I need to extract the 136 participants' data.
      ##  something like "comparing two lists to return the matches" seems the way to go.  

    datasetCounter = datasetCounter + 1
    #print (datasetCounter)
    '''print (str(id)+", ") #just to print IDs I used this line and then commented out the print section below so that the 
                         #for loop is not applied to the print below and only to the IDs'''
    
    print ( str(id)+" "+
            str(p['group']) + " " +str(p['pdq_chi_distribution2_pre1_fake'])+" "+
          str(p['pdq_chi_distribution2_post1_fake'])+" "+
          str(p['pdq_chi_distribution2_pre2_fake'])+" "+
          str(p['pdq_chi_distribution2_post2_fake']) )


    '''print ( str(id)+" "+
            str(p['group']) + " " +str(p['snackChoicePre1']) +" "+str(p['calorie_influence_pre1_fake'])+" "+str(p['pre1_getInfo_fake']+p['pre1_moreInfo_fake'])+" "+
            str(p['pdq_chi_distribution_pre1_fake'])+" "+ 
            #remember that these numbers will be 24 numbers right next to each other w/o commas
            str(p['snackChoicePost1'])+" "+str(p['calorie_influence_post1_fake'])+" "+str(p['post1_getInfo_fake']+p['post1_moreInfo_fake'])+" "+
            str(p['pdq_chi_distribution_post1_fake'])+" "+
            str(p['snackChoicePre2'])+" "+str(p['calorie_influence_pre2_fake'])+" "+str(p['pre2_getInfo_fake']+p['pre2_moreInfo_fake'])+" "+
            str(p['pdq_chi_distribution_pre2_fake'])+" "+
            str(p['snackChoicePost2'])+" "+str(p['calorie_influence_post2_fake'])+" "+str(p['post2_getInfo_fake']+p['post2_moreInfo_fake'])+" "+
            str(p['pdq_chi_distribution_post2_fake'])
          )'''

    
    if ((p['snackChoicePre1']+p['snackChoicePost1']) >
        (p['snackChoicePre2']+p['snackChoicePost2'])):
      worse += 1
    if ((p['snackChoicePre1']+p['snackChoicePost1']) <
        (p['snackChoicePre2']+p['snackChoicePost2'])):
      better += 1
    else :
      same += 1
    
    if (str(p['snackChoicePre1']) >
        (str(p['snackChoicePost1']))):
      worse1 += 1
    elif (str(p['snackChoicePre1']) <
        (str(p['snackChoicePost1']))):
      better1 +=1
    else :
        same1 += 1

    if (str(p['snackChoicePre2']) >
        (str(p['snackChoicePost2']))):
      worse2 += 1
    elif (str(p['snackChoicePre2']) <
        (str(p['snackChoicePost2']))):
      better2 +=1
    else :
        same2 += 1

print (better)
print (worse)
print (same)
print (better + worse + same)
print ()
print (better1)
print (worse1)
print (same1)
print (better1 + worse1 + same1)
print ()
print (better2)
print (worse2)
print (same2)
print (better2 + worse2 + same2)
print ()
#finishedSession2 = 0
#for (id,p) in all.items():
#  if(p['completedPDQ4'] and p['sic']>=20): finishedSession2 +=1
#print (finishedSession2)
