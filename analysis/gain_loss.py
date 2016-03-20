import high_risk

def conditionG(p):return (p['group']=='gain')
def conditionL(p):return (p['group']=='loss')

print ("GAIN")
high_risk.high_risk_results(conditionG)
print ()

print ("LOSS")
high_risk.high_risk_results(conditionL)
