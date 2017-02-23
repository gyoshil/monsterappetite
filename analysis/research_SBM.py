import query_dbs
from pprint import pprint



results_dir = "spss_ready/"

def r1(all):

  def completed(p):
    #return ((p['ffq2_score'])!='empty' and (p['ffq2_score'])<=11.45)
    return (p['ffq1_risk']=='1' and (p['ffq2_score']<=11.45))


  filtered_list = {k:v for (k,v) in all.items() if completed(v)}
  print (len(filtered_list))

  with open(results_dir+'RQ1.csv', 'w') as f:
    for (id,p) in filtered_list.items():
      if p['group']=='gain':
        group = 1
      if p['group']=='loss':
        group = 2
      f.write ("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (group,p['risk_level_pre1'],p['risk_level_post1'],p['risk_level_pre2'],p['risk_level_post2'],
                                                (p['calorie_seeker_pre1']),(p['calorie_seeker_post1']),(p['calorie_seeker_pre2']),(p['calorie_seeker_post2']),
                                                (p['calorie_seeker_q4_pre1']),(p['calorie_seeker_q4_post1']),(p['calorie_seeker_q4_pre2']),(p['calorie_seeker_q4_post2'])
                                                ))


# make the same thing as above except do not return ***  p['ffq1_risk']=='1'   ****
####

def r1_CHI(all):

  def completed(p):
    if  p['ffq2_score'] == 'empty':
      return 0

    return ((float (p['ffq2_score']) <=11.45) and (p['completedPDQ2']==True))  
    # I added 'completedPDQ2' and not PDQ4 because I am only considering Session 1 for now

  filtered_list = {k:v for (k,v) in all.items() if completed(v)}
  print (len(filtered_list))

  with open(results_dir+'CHI.csv', 'w') as f:
    for (id,p) in filtered_list.items():
      if p['group']=='gain':
        group = 1
      if p['group']=='loss':
        group = 2
      f.write ("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (group,p['risk_level_pre1'],p['risk_level_post1'],p['risk_level_pre2'],p['risk_level_post2'],
                                                (p['calorie_seeker_pre1']),(p['calorie_seeker_post1']),(p['calorie_seeker_pre2']),(p['calorie_seeker_post2']),
                                                (p['calorie_seeker_q4_pre1']),(p['calorie_seeker_q4_post1']),(p['calorie_seeker_q4_pre2']),(p['calorie_seeker_q4_post2'])
                                                ))

###### now i am making the same CSV with all those who scored above 11.45 so that I have the entire population

def r1_CHI2(all):

  def completed(p):
    if  p['ffq2_score'] == 'empty':
      return 0

    return ((float (p['ffq2_score']) > 11.45) and (p['completedPDQ2']==True)) 
    # I added 'completedPDQ2' and not PDQ4 because I am only considering Session 1 for now

  filtered_list = {k:v for (k,v) in all.items() if completed(v)}
  print (len(filtered_list))

  with open(results_dir+'CHI2.csv', 'w') as f:
    for (id,p) in filtered_list.items():
      if p['group']=='gain':
        group = 1
      if p['group']=='loss':
        group = 2
      f.write ("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (group,p['risk_level_pre1'],p['risk_level_post1'],p['risk_level_pre2'],p['risk_level_post2'],
                                                (p['calorie_seeker_pre1']),(p['calorie_seeker_post1']),(p['calorie_seeker_pre2']),(p['calorie_seeker_post2']),
                                                (p['calorie_seeker_q4_pre1']),(p['calorie_seeker_q4_post1']),(p['calorie_seeker_q4_pre2']),(p['calorie_seeker_q4_post2'])
                                                ))


###############################
############# SBM #############
def r1_SBM (all):
  def completed(p):
    if  p['ffq2_score'] == 'empty':
      return 0

    return (p['completedPDQ4']==True) 

  filtered_list = {k:v for (k,v) in all.items() if completed(v)}
  print (len(filtered_list))

  with open(results_dir+'r1_SBM.csv', 'w') as f:
    for (id,p) in filtered_list.items():
      if p['group']=='gain':
        group = 1
      if p['group']=='loss':
        group = 2
      f.write ("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (group,
                                                (p['calorie_seeker_q2_pre1']),(p['calorie_seeker_q2_post1']),(p['calorie_seeker_q2_pre2']),(p['calorie_seeker_q2_post2']),
                                                
                                                (p['calorie_seeker_q3_pre1']),(p['calorie_seeker_q3_post1']),(p['calorie_seeker_q3_pre2']),(p['calorie_seeker_q3_post2']),
                                                
                                                (p['calorie_seeker_q4_pre1']),(p['calorie_seeker_q4_post1']),(p['calorie_seeker_q4_pre2']),(p['calorie_seeker_q4_post2'])
                                                )


###############################
############# CHI #############
##### going to add some code to produce a CSV that 
##### will give me the 153 data sets 
##### I have seen in Python code for 
##### snackChoices pre vs. post requested by Lena for CHI

###############################

def r_CHI_RQ3(all):
  def completedCHI(p):
    return ((not(p['snackChoicePre1']=='empty' or p['snackChoicePost1']=='empty' or p['snackChoicePre2']=='empty' or p['snackChoicePost2']=='empty')))
  filtered_CHI = {k:v for (k,v) in all.items() if completedCHI(v)}

  with open(results_dir+'r_CHI_RQ3.csv', 'w') as f:
    for (id,p) in filtered_CHI.items():
      sess_pre1 = str(p['snackChoicePre1'])
      sess_post1 = str(p['snackChoicePost1'])
      sess_pre2 = str(p['snackChoicePre2'])
      sess_post2 = str(p['snackChoicePost2'])

      f.write ("%s,%s,%s,%s,%s\n" % (p['group'],sess_pre1, sess_post1, sess_pre2, sess_post2)) 

        #(str(sess_pre1-sess_post1)), (str(sess_post1-sess_pre1)), 
        #(str(sess_pre2-sess_post2)), str((sess_post2-sess_pre2)), (str((sess_pre1+sess_post1)-(sess_pre2+sess_post2))), 
        #(str((sess_pre2+sess_post2)-(sess_pre1+sess_post1)))))

def CHI_r3(all):

  def completed1(p):
    return ( (p['completedPDQ1']==True) and (p['completedPDQ2']==True) and (p['sic']>=10) and
              (not(p['snackChoicePre1']=='empty' or p['snackChoicePost1']=='empty')) )
  filtered_list1 = {k:v for (k,v) in all.items() if completed1(v)}

  # Total number of participants being 212 makes sense as only up to snackChoicePost1 not being empty is counted. On line 156.
  # N=212
  with open(results_dir+'CHI_RQ3_sessPre1.csv', 'w') as f:
    for (id,p) in filtered_list1.items():
      f.write ("%s,%s,%s,%s,%s\n" % (p['group'],p['pre1_getInfo_fake'],p['pre1_moreInfo_fake'], p['snackChoicePre1'], p['calorie_influence_pre1_fake']))

  with open(results_dir+'CHI_RQ3_sessPost1.csv', 'w') as f:
    for (id,p) in filtered_list1.items():
      f.write ("%s,%s,%s,%s,%s\n" % (p['group'],p['post1_getInfo_fake'],p['post1_moreInfo_fake'], p['snackChoicePost1'], p['calorie_influence_post1_fake']))

  def completed2(p):
    return ( (p['completedPDQ3']==True) and (p['completedPDQ4']==True) and (p['sic']>=20) and
             (not(p['snackChoicePre2']=='empty' or p['snackChoicePost2']=='empty')) )

  filtered_list2 = {k:v for (k,v) in all.items() if completed2(v)}
  # Total number of participants being 130 makes sense as PDQ completion conditional is added (so a drop from 153 makes sense)
  # N=130
  with open(results_dir+'CHI_RQ3_sessPre2.csv', 'w') as f:
    for (id,p) in filtered_list2.items():
      f.write ("%s,%s,%s,%s,%s\n" % (p['group'],p['pre2_getInfo_fake'],p['pre2_moreInfo_fake'], p['snackChoicePre2'],p['calorie_influence_pre2_fake']))
  # N=130
  with open(results_dir+'CHI_RQ3_sessPost2.csv', 'w') as f:
    for (id,p) in filtered_list2.items():
      f.write ("%s,%s,%s,%s,%s\n" % (p['group'],p['post2_getInfo_fake'],p['post2_moreInfo_fake'],p['snackChoicePost2'],p['calorie_influence_post2_fake']))


def CHI_session1(all):

  def completed1(p):
    return ( (p['completedPDQ1']==True) and (p['completedPDQ2']==True) and (p['sic']>=10) and
              (not(p['snackChoicePre1']=='empty' or p['snackChoicePost1']=='empty')) )
  filtered_list1 = {k:v for (k,v) in all.items() if completed1(v)}
  # N=212
  with open(results_dir+'CHI_session1.csv', 'w') as f:
    for (id,p) in filtered_list1.items():
      f.write ("%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (p['group'],p['pre1_getInfo_fake'],p['pre1_moreInfo_fake'], p['snackChoicePre1'], p['calorie_influence_pre1_fake'],p['post1_getInfo_fake'],p['post1_moreInfo_fake'], p['snackChoicePost1'], p['calorie_influence_post1_fake']))



def CHI_N130(all):

  def completed1(p):
    return ( (p['completedPDQ1']==True) and (p['completedPDQ2']==True) and (p['completedPDQ3']==True) and (p['completedPDQ4']==True) 
            and (p['sic']>=20) and
            (not(p['snackChoicePre1']=='empty' or p['snackChoicePost1']=='empty' or p['snackChoicePre2']=='empty' or p['snackChoicePost2']=='empty'))
           )
  filtered_list1 = {k:v for (k,v) in all.items() if completed1(v)}

  with open(results_dir+'CHI_N130.csv', 'w') as f:
    for (id,p) in filtered_list1.items():
      f.write ("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % 
        (p['group'],p['pre1_getInfo_fake'],p['pre1_moreInfo_fake'], p['snackChoicePre1'], p['calorie_influence_pre1_fake'],
         p['post1_getInfo_fake'],p['post1_moreInfo_fake'], p['snackChoicePost1'], p['calorie_influence_post1_fake'],
         p['pre2_getInfo_fake'],p['pre2_moreInfo_fake'], p['snackChoicePre2'],p['calorie_influence_pre2_fake'],
         p['post2_getInfo_fake'],p['post2_moreInfo_fake'],p['snackChoicePost2'],p['calorie_influence_post2_fake']
        )
        )


def r3(all):

  def completed1(p):
    return ( (p['completedPDQ1']==True) and (p['completedPDQ2']==True) and (p['sic']>=10) )
  filtered_list1 = {k:v for (k,v) in all.items() if completed1(v)}

  with open(results_dir+'RQ3_sessionPre1.csv', 'w') as f:
    for (id,p) in filtered_list1.items():
      f.write ("%s,%s,%s\n" % (p['pre1_getInfo_fake'],p['pre1_moreInfo_fake'],p['calorie_influence_pre1_fake']))

  with open(results_dir+'RQ3_sessionPost1.csv', 'w') as f:
    for (id,p) in filtered_list1.items():
      f.write ("%s,%s,%s\n" % (p['post1_getInfo_fake'],p['post1_moreInfo_fake'],p['calorie_influence_post1_fake']))

  def completed2(p):
    return ((p['completedPDQ3']==True) and (p['completedPDQ4']==True) and (p['sic']>=20))

  filtered_list2 = {k:v for (k,v) in all.items() if completed2(v)}

  with open(results_dir+'RQ3_sessionPre2.csv', 'w') as f:
    for (id,p) in filtered_list2.items():
      f.write ("%s,%s,%s\n" % (p['pre2_getInfo_fake'],p['pre2_moreInfo_fake'],p['calorie_influence_pre2_fake']))

  with open(results_dir+'RQ3_sessionPost2.csv', 'w') as f:
    for (id,p) in filtered_list2.items():
      f.write ("%s,%s,%s\n" % (p['post2_getInfo_fake'],p['post2_moreInfo_fake'],p['calorie_influence_post2_fake']))



def r4(all):

    def completed1(p):
      return ((p['completedPDQ1']==True) and (p['sic']>=5) and (p['ffq1_risk']!='empty') and (p['ffq2_score']!='empty'))
    filtered_list1 = {k:v for (k,v) in all.items() if completed1(v)}

    with open(results_dir+'RQ4_sessionPre1.csv', 'w') as f:
      for (id,p) in filtered_list1.items():
        snacking_behavior = int((p['ffq1_risk']=='1' and (p['ffq2_score']<=11.45)))
        def toInt(g): return int(g=='gain')
        f.write ("%s,%s,%s,%s,%s,%s,%s,%s\n" %
                (snacking_behavior,
                toInt(p['group']),
                int(p['calorie_seeker_pre1']),
                p['risk_level_pre1'],
                p['pre1_getInfo_fake'],
                p['pre1_moreInfo_fake'],
                p['snackChoicePre1'],
                p['calorie_influence_pre1_fake']))

    def completed2(p):
      return ((p['completedPDQ2']==True) and (p['sic']>=10) and (p['ffq1_risk']!='empty') and (p['ffq2_score']!='empty'))
    filtered_list2 = {k:v for (k,v) in all.items() if completed2(v)}

    with open(results_dir+'RQ4_sessionPost1.csv', 'w') as f:
      for (id,p) in filtered_list2.items():
        snacking_behavior = int((p['ffq1_risk']=='1' and (p['ffq2_score']<=11.45)))
        def toInt(g): return int(g=='gain')
        if(p['calorie_seeker_post1']!='empty'):
          f.write ("%s,%s,%s,%s,%s,%s,%s,%s\n" %
                  (snacking_behavior,
                  toInt(p['group']),
                  int(p['calorie_seeker_post1']),
                  p['risk_level_post1'],
                  p['post1_getInfo_fake'],
                  p['post1_moreInfo_fake'],
                  p['snackChoicePost1'],
                  p['calorie_influence_post1_fake']))

    def completed3(p):
      return ((p['completedPDQ3']==True) and (p['sic']>=15) and (p['ffq1_risk']!='empty') and (p['ffq2_score']!='empty'))
    filtered_list3 = {k:v for (k,v) in all.items() if completed3(v)}

    with open(results_dir+'RQ4_sessionPre2.csv', 'w') as f:
      for (id,p) in filtered_list3.items():
        snacking_behavior = int((p['ffq1_risk']=='1' and (p['ffq2_score']<=11.45)))
        def toInt(g): return int(g=='gain')
        if(p['calorie_seeker_pre2']!='empty'):
          f.write ("%s,%s,%s,%s,%s,%s,%s,%s\n" %
                  (snacking_behavior,
                  toInt(p['group']),
                  int(p['calorie_seeker_pre2']),
                  p['risk_level_pre2'],
                  p['pre2_getInfo_fake'],
                  p['pre2_moreInfo_fake'],
                  p['snackChoicePre2'],
                  p['calorie_influence_pre2_fake']))

    def completed4(p):
      return ((p['completedPDQ4']==True) and (p['sic']>=20) and (p['ffq1_risk']!='empty') and (p['ffq2_score']!='empty'))
    filtered_list4 = {k:v for (k,v) in all.items() if completed4(v)}

    with open(results_dir+'RQ4_sessionPost2.csv', 'w') as f:
      for (id,p) in filtered_list4.items():
        snacking_behavior = int((p['ffq1_risk']=='1' and (p['ffq2_score']<=11.45)))
        def toInt(g): return int(g=='gain')
        if(p['calorie_seeker_post2']!='empty'):
          f.write ("%s,%s,%s,%s,%s,%s,%s,%s\n" %
                  (snacking_behavior,
                  toInt(p['group']),
                  int(p['calorie_seeker_post2']),
                  p['risk_level_post2'],
                  p['post2_getInfo_fake'],
                  p['post2_moreInfo_fake'],
                  p['snackChoicePost2'],
                  p['calorie_influence_post2_fake']))


def rBonus3(all):
    ctr=0

    for (idp,p) in all.items():
     #pprint(p)
     #start counting at 1, leave first spot blank
     #also need an extra for crappy data
     allClickCounts1 = [0]* 22
     allClickCounts2 = [0]* 22

     s = (p['sic'])
     try:
         if (p['ffq1_risk']=='empty'):
             raise Exception
         round_mulitplier = 0
         max_round = 0
         for click in p['informationSeekingBehavior']:
            max_round = max(max_round,click['round'])
            if (max_round > click['round']):
                round_mulitplier += 5
                max_round = 0
            thisRound = click["round"]+round_mulitplier
            if (click['button']==1):
                allClickCounts1[thisRound] +=1
            if (click['button']==2):
                allClickCounts2[thisRound] +=1
         def pr(i):
           return str(allClickCounts1[i])+", "+str(allClickCounts2[i])+""
         print (p['group']+","+p['pop']+","+str(p['sic'])+","+str(p['completedPDQ4']), end=",")
         print (", ".join(list(map(pr,[1,3,4,7,8,9,11,14,15,18,19,20]))))
         ctr+=1

     except Exception as e:
         pass
