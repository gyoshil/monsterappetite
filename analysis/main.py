import higher_order

import query_dbs
import infoSeekingClicks


all = query_dbs.allMongoPlayers()
def sic(p):
  player = query_dbs.findPlayerInMongo('_id',p[0])
  return len(player['snackazonItemChoices'])
query_dbs.tagMongoPlayers(all,sic)

def completedPDQ2(mongoP,qualtricsP):
  return (qualtricsP!="NONE")
query_dbs.tagCSVPlayers("PDQ2.csv",all,"completedPDQ2",completedPDQ2)

def completedPDQ4(mongoP,qualtricsP):
  return (qualtricsP!="NONE")
query_dbs.tagCSVPlayers("PDQ4.csv",all,"completedPDQ4",completedPDQ4)

######
# RISK
######
def csv_answer_check(mongoP,qualtricsP,answer_checks):
  if(qualtricsP=="NONE"):
    return "empty"
  meets_condition = False
  for a in answer_checks:
    meets_condition = meets_condition or qualtricsP[a[0]] ==a[1]
  return meets_condition

def risk_level(mongoP,qualtricsP):
  if(qualtricsP=="NONE"):
    return "empty"
  good_answers = [(4,4),(4,5),(5,4),(5,5),(7,1),(7,2),(8,1),(8,2)]
  if(csv_answer_check(mongoP,qualtricsP,good_answers)):
    return "high"
  return "low"
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

######
# GROUP
######
def group(p):
  player = query_dbs.findPlayerInMongo('_id',p[0])
  return player['group']
query_dbs.tagMongoPlayers(all,group)



print (all['HzyJf3ecpepyFffL9'])
