
results_dir = "analysis/spss_ready/"

def r1(all):

  def completed(p):
    return ((p['ffq1_risk']!='empty') and (p['ffq2_score']!='empty'))
  filtered_list = {k:v for (k,v) in all.items() if completed(v)}

  with open(results_dir+'RQ1.csv', 'w') as f:
    for (id,p) in filtered_list.items():
      if p['group']=='gain':
        group = 1
      if p['group']=='loss':
        group = 2
      f.write ("%s,%s,%s,%s,%s\n" % (group,p['risk_level_pre1'],p['risk_level_post1'],p['risk_level_pre2'],p['risk_level_post2']))


def r2(all):
  def completed1(p):
    return ((p['risk_level_post1']!='empty') and (p['sic']>=10))
  filtered_list1 = {k:v for (k,v) in all.items() if completed1(v)}

  with open(results_dir+'RQ2_session1.csv', 'w') as f:
    for (id,p) in filtered_list1.items():
      f.write ("%s,%s,%s\n" % (p['risk_level_post1'],p['post1_getInfo'],p['post1_moreInfo']))

  def completed2(p):
    return ((p['risk_level_post2']!='empty') and (p['sic']>=20))
  filtered_list2 = {k:v for (k,v) in all.items() if completed2(v)}

  with open(results_dir+'RQ2_session2.csv', 'w') as f:
    for (id,p) in filtered_list2.items():
      f.write ("%s,%s,%s\n" % (p['risk_level_post2'],p['post2_getInfo'],p['post2_moreInfo']))


def r3(all):

  def completed1(p):
    return ((p['completedPDQ1']==True) and p['completedPDQ2']==True) and (p['sic']>=10))
  filtered_list1 = {k:v for (k,v) in all.items() if completed1(v)}

  with open(results_dir+'RQ3_session1.csv', 'w') as f:
    for (id,p) in filtered_list1.items():
      f.write ("%s,%s,%s\n" % (p['pre1_getInfo_fake'],p['pre1_moreInfo_fake'],p['calorie_influence_pre1_fake']))

  def completed2(p):
    return ((p['risk_level_post2']!='empty') and (p['sic']>=20))
  filtered_list2 = {k:v for (k,v) in all.items() if completed2(v)}

  with open(results_dir+'RQ2_session2.csv', 'w') as f:
    for (id,p) in filtered_list2.items():
      f.write ("%s,%s,%s\n" % (p['risk_level_post2'],p['post2_getInfo'],p['post2_moreInfo']))
      '''
