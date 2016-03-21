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
query_dbs.tagCSVPlayers("PDQ2.csv",all,completedPDQ2)

def completedPDQ4(mongoP,qualtricsP):
  return (qualtricsP!="NONE")
query_dbs.tagCSVPlayers("PDQ4.csv",all,completedPDQ4)

######
# RISK
######
def risk_level(mongoP,qualtricsP):
  if(qualtricsP=="NONE"):
    return "empty"
  def q2(p):return p[4] =='4' or p[4] =='5'
  def q3(p):return p[5] =='4' or p[5] =='5'
  def q6(p):return p[7] =='1' or p[7] =='2'
  def q7(p):return p[8] =='1' or p[8] =='2'
  if (q2(qualtricsP) or q3(qualtricsP) or q6(qualtricsP) or q7(qualtricsP)):
    return "high"
  return "low"
def risk_level_pre1(m,q): return risk_level(m,q)
query_dbs.tagCSVPlayers("BIQ1.csv",all,risk_level_pre1)
def risk_level_post1(m,q): return risk_level(m,q)
query_dbs.tagCSVPlayers("BIQ2.csv",all,risk_level_post1)
def risk_level_pre2(m,q): return risk_level(m,q)
query_dbs.tagCSVPlayers("BIQ3.csv",all,risk_level_pre2)
def risk_level_post2(m,q): return risk_level(m,q)
query_dbs.tagCSVPlayers("BIQ3.csv",all,risk_level_post2)

########
# Calories
########
def calorie_seeker(mongoP,qualtricsP):
  if(qualtricsP=="NONE"):
    return "empty"
  def q4(p):return p[4] =='4' or p[4] =='5'
  if (q4(qualtricsP)):
    return "high"
  return "low"
def calorie_seeker_pre1(m,q): return calorie_seeker(m,q)
query_dbs.tagCSVPlayers("BIQ1.csv",all,calorie_seeker_pre1)
def calorie_seeker_post1(m,q): return calorie_seeker(m,q)
query_dbs.tagCSVPlayers("BIQ2.csv",all,calorie_seeker_post1)
def calorie_seeker_pre2(m,q): return calorie_seeker(m,q)
query_dbs.tagCSVPlayers("BIQ3.csv",all,calorie_seeker_pre2)
def calorie_seeker_post2(m,q): return calorie_seeker(m,q)
query_dbs.tagCSVPlayers("BIQ3.csv",all,calorie_seeker_post2)


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
