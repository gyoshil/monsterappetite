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

def riskLevel(mongoP,qualtricsP):
  if(qualtricsP=="NONE"):
    return "empty"
  def q2(p):return p[4] =='4' or p[4] =='5'
  def q3(p):return p[5] =='4' or p[5] =='5'
  def q6(p):return p[7] =='1' or p[7] =='2'
  def q7(p):return p[8] =='1' or p[8] =='2'
  if (q2(qualtricsP) or q3(qualtricsP) or q6(qualtricsP) or q7(qualtricsP)):
    return "high"
  return "low"
query_dbs.tagCSVPlayers("BIQ1.csv",all,riskLevel)

def pre1(p): return infoSeekingClicks.gatherClicks(0,p)
query_dbs.tagMongoPlayers(all,pre1)

def post1(p): return infoSeekingClicks.gatherClicks(1,p)
query_dbs.tagMongoPlayers(all,post1)

def pre2(p): return infoSeekingClicks.gatherClicks(2,p)
query_dbs.tagMongoPlayers(all,pre2)

def post2(p): return infoSeekingClicks.gatherClicks(3,p)
query_dbs.tagMongoPlayers(all,post2)

print (all['HzyJf3ecpepyFffL9'])
