def risk_level(file,mongoP,qualtricsP):
  if(qualtricsP=="NONE"):
    return "empty"
  def q2(p):return p[4] =='4' or p[4] =='5'
  def q3(p):return p[5] =='4' or p[5] =='5'
  def q6(p):return p[7] =='1' or p[7] =='2'
  def q7(p):return p[8] =='1' or p[8] =='2'
  if (q2(qualtricsP) or q3(qualtricsP) or q6(qualtricsP) or q7(qualtricsP)):
    return "high"
  return "low"
query_dbs.tagCSVPlayers(file,all,riskLevel)
