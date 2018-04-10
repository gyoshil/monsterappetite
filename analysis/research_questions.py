import query_dbs
from pprint import pprint



results_dir = "spss_ready/"


###############################
############# SBM #############
def r1_SBM (all):
  def completed(p):
    if  p['ffq2_score'] == 'empty':
      return 0

    return (p['completedPDQ4']==True) 

  filtered_list = {k:v for (k,v) in all.items() if completed(v)}
  #print (len(filtered_list))

  with open(results_dir+'r1_SBM.csv', 'w') as f:
    for (id,p) in filtered_list.items():
      if p['group']=='gain':
        group = 1
      if p['group']=='loss':
        group = 2
      f.write ("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (group,
                                                (p['calorie_seeker_q2_pre1']),(p['calorie_seeker_q2_post1']),(p['calorie_seeker_q2_pre2']),(p['calorie_seeker_q2_post2']),                                               
                                                (p['calorie_seeker_q3_pre1']),(p['calorie_seeker_q3_post1']),(p['calorie_seeker_q3_pre2']),(p['calorie_seeker_q3_post2']),
                                                (p['calorie_seeker_q3_min_pre1']),(p['calorie_seeker_q3_min_post1']),(p['calorie_seeker_q3_min_pre2']),(p['calorie_seeker_q3_min_post2']),
                                                (p['calorie_seeker_q4_pre1']),(p['calorie_seeker_q4_post1']),(p['calorie_seeker_q4_pre2']),(p['calorie_seeker_q4_post2'])
                                                ))

######################## FOR SBM DATA ANALYSIS
############ REPEATED RESEARCH QUESTION 2 FROM MY DISSERTATION EXCEPT THAT I WILL NOW INCLUDE BIQ1 AND BIQ3 NOW

def r2_SBM(all):
  # def completed1(p):
  #   return ((p['risk_level_post1']!='empty') and (p['sic']>=10))
  # filtered_list1 = {k:v for (k,v) in all.items() if completed1(v)}

  # with open(results_dir+'RQ2_session1.csv', 'w') as f:
  #   for (id,p) in filtered_list1.items():
  #     f.write ("%s,%s,%s\n" % (p['risk_level_post1'],p['post1_getInfo'],p['post1_moreInfo']))
  #     # risk_level_post1  is BEHAVIORAL INTENTION !!!!!!
  #     # now just need risk_level -- counted for quesiton 3 and for pre1 and pre 2 !!!!!!!!!!!!!!!

  def completed2(p):
    return (p['sic']>=20)
  filtered_list2 = {k:v for (k,v) in all.items() if completed2(v)}

  with open(results_dir+'RQ2_SBM_BIQ_ISB.csv', 'w') as f:
    for (id,p) in filtered_list2.items():
      f.write ("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (p['calorie_seeker_q3_min_pre1'],p['calorie_seeker_q3_min_post1'],
                                                          p['pre1_getInfo'],p['pre1_moreInfo'],
                                                          p['post1_getInfo'],p['post1_moreInfo'],
                                                          p['calorie_seeker_q3_min_pre2'],p['calorie_seeker_q3_min_post2'],
                                                          p['pre2_getInfo'],p['pre2_moreInfo'],
                                                          p['post2_getInfo'],p['post2_moreInfo'])
              )


def r2_SBM_w_GRP(all):
  # def completed1(p):
  #   return ((p['risk_level_post1']!='empty') and (p['sic']>=10))
  # filtered_list1 = {k:v for (k,v) in all.items() if completed1(v)}

  # with open(results_dir+'RQ2_session1.csv', 'w') as f:
  #   for (id,p) in filtered_list1.items():
  #     f.write ("%s,%s,%s\n" % (p['risk_level_post1'],p['post1_getInfo'],p['post1_moreInfo']))
  #     # risk_level_post1  is BEHAVIORAL INTENTION !!!!!!
  #     # now just need risk_level -- counted for quesiton 3 and for pre1 and pre 2 !!!!!!!!!!!!!!!

  def completed2(p):
    return (p['sic']>=20)
  filtered_list2 = {k:v for (k,v) in all.items() if completed2(v)}

  with open(results_dir+'RQ2_SBM_BIQ_ISB_w_GRP.csv', 'w') as f:
    for (id,p) in filtered_list2.items():
      f.write ("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (p['group'],str(id),
                                                          p['calorie_seeker_q3_min_pre1'],p['calorie_seeker_q3_min_post1'],
                                                          p['pre1_getInfo'],p['pre1_moreInfo'],
                                                          p['post1_getInfo'],p['post1_moreInfo'],
                                                          p['calorie_seeker_q3_min_pre2'],p['calorie_seeker_q3_min_post2'],
                                                          p['pre2_getInfo'],p['pre2_moreInfo'],
                                                          p['post2_getInfo'],p['post2_moreInfo'])
              )
######################## for SBM RQ3 and RQ4 regarding logistic linear regression ########################
  
#      return ((p['completedPDQ4']==True) and (p['sic']>=20) and (p['ffq1_risk']!='empty') and (p['ffq2_score']!='empty'))
#      ABOVE is how I got N=136 in my dissertation 

def r4_SBM(all):
  def completed4(p):
    return ((p['completedPDQ4']==True) and (p['sic']>=20))  # added the 'completedPDQ4' since we will include reasons as well 
  filtered_list4 = {k:v for (k,v) in all.items() if completed4(v)}

  with open(results_dir+'RQ3_RQ4_SBM_BIQ_ISB_SIC_PDQ.csv', 'w') as f:
    for (id,p) in filtered_list4.items():
      #snacking_behavior = int((p['ffq1_risk']=='1' and (p['ffq2_score']<=11.45)))
      #def toInt(g): return int(g=='gain')
        #if(p['calorie_seeker_q3_min_post2']!='empty'):
          f.write ("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" %
                  #(#snacking_behavior,
                  (p['group'],
                  #int(p['calorie_seeker_post2']),
                  
                  p['calorie_seeker_q3_min_pre1'],
                  p['pre1_getInfo'],p['pre1_moreInfo'],
                  int(p['pre1_getInfo']+p['pre1_moreInfo']),
                  int(p['snackChoicePre1']), p['calorie_influence_pre1_fake'],

                  p['calorie_seeker_q3_min_post1'],
                  p['post1_getInfo'],p['post1_moreInfo'],
                  int(p['post1_getInfo']+p['post1_moreInfo']),
                  int(p['snackChoicePost1']),p['calorie_influence_post1_fake'],
                  
                  p['calorie_seeker_q3_min_pre2'],
                  p['pre2_getInfo'],p['pre2_moreInfo'],
                  int(p['pre2_getInfo']+p['pre2_moreInfo']),
                  int(p['snackChoicePre2']), p['calorie_influence_pre2_fake'],

                  p['calorie_seeker_q3_min_post2'],
                  p['post2_getInfo'],p['post2_moreInfo'],
                  int(p['post2_getInfo']+p['post2_moreInfo']),
                  int(p['snackChoicePost2']), p['calorie_influence_post2_fake']))


      


def r1(all):

  def completed(p):
    #return ((p['ffq2_score'])!='empty' and (p['ffq2_score'])<=11.45)
    return (p['ffq1_risk']=='1' and (p['ffq2_score']<=11.45))


  filtered_list = {k:v for (k,v) in all.items() if completed(v)}
  #print (len(filtered_list))

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
  #print (len(filtered_list))

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
  #print (len(filtered_list))

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



def r2(all):
  def completed1(p):
    return ((p['risk_level_post1']!='empty') and (p['sic']>=10))
  filtered_list1 = {k:v for (k,v) in all.items() if completed1(v)}

  with open(results_dir+'RQ2_session1.csv', 'w') as f:
    for (id,p) in filtered_list1.items():
      f.write ("%s,%s,%s\n" % (p['risk_level_post1'],p['post1_getInfo'],p['post1_moreInfo']))
      # risk_level_post1  is BEHAVIORAL INTENTION !!!!!!
      # now just need risk_level -- counted for quesiton 3 and for pre1 and pre 2 !!!!!!!!!!!!!!!

  def completed2(p):
    return ((p['risk_level_post2']!='empty') and (p['sic']>=20))
  filtered_list2 = {k:v for (k,v) in all.items() if completed2(v)}

  with open(results_dir+'RQ2_session2.csv', 'w') as f:
    for (id,p) in filtered_list2.items():
      f.write ("%s,%s,%s\n" % (p['risk_level_post2'],p['post2_getInfo'],p['post2_moreInfo']))



def rBonus(all):

  def completed1(p):
    return ((p['completedPDQ3']==True) and (p['completedPDQ4']==True) and (p['sic']>=20))
  filtered_list1 = {k:v for (k,v) in all.items() if completed1(v)}

  with open(results_dir+'RBonus.csv', 'w') as f:
    for (id,p) in filtered_list1.items():
      sess1pre = p['pre1_getInfo']+ p['pre1_moreInfo']
      sess1post =  p['post1_getInfo']+ p['post1_moreInfo']
      sess2pre = p['pre2_getInfo']+ p['pre2_moreInfo']
      sess2post = p['post2_getInfo']+ p['post2_moreInfo']
      f.write ("%s,%s,%s,%s,%s\n" % (p['group'],sess1pre,sess1post,sess2pre,sess2post))

# "write another research question output here that modifies r2 above but one that splits gain and loss framing"


def rBonus2(all):
  def completed1(p):
    return ((p['completedPDQ3']==True) and (p['completedPDQ4']==True) and (p['sic']>=20))
  filtered_list1 = {k:v for (k,v) in all.items() if completed1(v)}

  with open(results_dir+'RBonus2.csv', 'w') as f:
    for (id,p) in filtered_list1.items():
      sess1 = p['snackChoicePre1']+ p['snackChoicePost1']
      sess2 = p['snackChoicePre2']+ p['snackChoicePost2']
      f.write ("%s,%s,%s,%s\n" % (p['group'],sess1,sess2,(sess1-sess2)))

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
    # k: key , v:value -- in a dictionary
  filtered_list1 = {k:v for (k,v) in all.items() if completed1(v)}
  # N=212
  with open(results_dir+'CHI_session1.csv', 'w') as f:
    for (id,p) in filtered_list1.items():
      f.write ("%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (p['group'],p['pre1_getInfo_fake'],p['pre1_moreInfo_fake'], p['snackChoicePre1'], p['calorie_influence_pre1_fake'],p['post1_getInfo_fake'],p['post1_moreInfo_fake'], p['snackChoicePost1'], p['calorie_influence_post1_fake']))

##################
# QUALITATIVE DATA    I ALSO need to add the printing of chi_qual1 and chi_qual2 in the main.py
##################

def CHI_qual(all):
  def chi_qual1(p):
    return (p['completedPDQ2']==True)  
  filtered_list1 = {k:v for (k,v) in all.items() if chi_qual1(v)}
  # results_dir = "spss_ready/"
  with open(results_dir+'qual_sess1.csv', 'w') as f:
    for (id,p) in filtered_list1.items():
      f.write("%s,%s\n"%(p['group'], p['qual_sess1'])) #I also need to print the 86th column (comments) of PDQ2.csv 

  def chi_qual2(p):
    return (p['completedPDQ4']==True)  
  filtered_list2 = {k:v for (k,v) in all.items() if chi_qual2(v)}
  with open(results_dir+'qual_sess2.csv', 'w') as f:
    for (id,p) in filtered_list2.items():
      f.write("%s,%s\n"%(p['group'], p['qual_sess2'])) #I also need to print the 86th column (comments) of PDQ4.csv 

######################################


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
      f.write ("%s,%s,%s,%s,%s,%s\n" % (str(id),p['group'],p['pre1_getInfo_fake'],p['pre1_moreInfo_fake'],p['snackChoicePre1'],p['calorie_influence_pre1_fake']))

  with open(results_dir+'RQ3_sessionPost1.csv', 'w') as f:
    for (id,p) in filtered_list1.items():
      f.write ("%s,%s,%s,%s,%s,%s\n" % (str(id),p['group'],p['post1_getInfo_fake'],p['post1_moreInfo_fake'],p['snackChoicePre1'],p['calorie_influence_post1_fake']))

  def completed2(p):
    return ((p['completedPDQ3']==True) and (p['completedPDQ4']==True) and (p['sic']>=20))

  filtered_list2 = {k:v for (k,v) in all.items() if completed2(v)}

  with open(results_dir+'RQ3_sessionPre2.csv', 'w') as f:
    for (id,p) in filtered_list2.items():
      f.write ("%s,%s,%s,%s,%s,%s\n" % (str(id),p['group'],p['pre2_getInfo_fake'],p['pre2_moreInfo_fake'],p['snackChoicePre1'],p['calorie_influence_pre2_fake']))

  with open(results_dir+'RQ3_sessionPost2.csv', 'w') as f:
    for (id,p) in filtered_list2.items():
      f.write ("%s,%s,%s,%s,%s,%s\n" % (str(id),p['group'],p['post2_getInfo_fake'],p['post2_moreInfo_fake'],p['snackChoicePre1'],p['calorie_influence_post2_fake']))

def r4(all):

    def completed1(p):
      return ((p['completedPDQ1']==True) and (p['sic']>=5) and (p['ffq1_risk']!='empty') and (p['ffq2_score']!='empty'))
    filtered_list1 = {k:v for (k,v) in all.items() if completed1(v)}

    with open(results_dir+'RQ4_sessionPre1.csv', 'w') as f:
      for (id,p) in filtered_list1.items():
        snacking_behavior = int((p['ffq1_risk']=='1' and (p['ffq2_score']<=11.45)))
        def toInt(g): return int(g=='gain')
        f.write ("%s,%s,%s,%s,%s,%s,%s,%s,%s\n" %
                (str(id),
                snacking_behavior,
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
          f.write ("%s,%s,%s,%s,%s,%s,%s,%s,%s\n" %
                  (str(id),
                  snacking_behavior,
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
          f.write ("%s,%s,%s,%s,%s,%s,%s,%s,%s\n" %
                  (str(id),
                  snacking_behavior,
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
          f.write ("%s,%s,%s,%s,%s,%s,%s,%s,%s\n" %
                  (str(id),
                  snacking_behavior,
                  toInt(p['group']),
                  int(p['calorie_seeker_post2']),
                  p['risk_level_post2'],
                  p['post2_getInfo_fake'],
                  p['post2_moreInfo_fake'],
                  p['snackChoicePost2'],
                  p['calorie_influence_post2_fake']))


##################################################################################################################################################
##################################################################################################################################################
##################################################################################################################################################
###################################### FOR COMPUTERS IN HUMAN BEHAVIOR JOURNAL analysis (NAMED G4H for NOW) ######################################
##################################################################################################################################################
##################################################################################################################################################
##################################################################################################################################################
##################################################################################################################################################
##################################################################################################################################################
##################################################################################################################################################
def r4_G4H(all):

    def completed1(p):
      return ((p['completedPDQ1']==True) #and (p['sic']>=5)
      )
    filtered_list1 = {k:v for (k,v) in all.items() if completed1(v)}

    with open(results_dir+'RQ4_G4H_aPre1.csv', 'w') as f:
      f.write ("snackBehav, grp, oftenSnack, checkCal, abovePrice, BIQseek, all_risky, button1, button2, buttons_all, SIC, PDQ")

      for (idp,p) in filtered_list1.items():
        snacking_behavior = int((p['ffq1_risk']=='1' and (p['ffq2_score']<=11.45)))
        def toInt(g): return int(g=='gain')

        f.write ("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" %
                (snacking_behavior,
                toInt(p['group']),
                int(p['calorie_seeker_pre1']), 
                int(p['calorie_seeker_q2_min_pre1']), 
                int(p['calorie_seeker_q3_min_pre1']), 
                int(p['calorie_seeker_q4_min_pre1']), 
                p['risk_level_pre1'], ## 1 means that you are exhibiting risky behavior overall. 
                p['pre1_getInfo_fake'],
                p['pre1_moreInfo_fake'],
                (p['pre1_getInfo_fake'] + p['pre1_moreInfo_fake']),
                p['snackChoicePre1'],
                p['calorie_influence_pre1_fake']))

        #### maybe consider adding calorie_seeker_q2, calorie_seeker_q3, calorie_seeker_q3_min, calorie_seeker_q4, and see if they make a difference. 

    def completed2(p):
      return ((p['completedPDQ2']==True) #and (p['sic']>=10)
      )
    filtered_list2 = {k:v for (k,v) in all.items() if completed2(v)}

    with open(results_dir+'RQ4_G4H_bPost1.csv', 'w') as f:
      f.write ("snackBehav, grp, oftenSnack, checkCal, abovePrice, BIQseek, all_risky, button1, button2, buttons_all, SIC, PDQ")

      for (idp,p) in filtered_list2.items():
        snacking_behavior = int((p['ffq1_risk']=='1' and (p['ffq2_score']<=11.45)))
        def toInt(g): return int(g=='gain')

        if(p['calorie_seeker_post1']!='empty'):
          f.write ("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" %
                  (snacking_behavior,
                  toInt(p['group']),
                  int(p['calorie_seeker_post1']),
                  int(p['calorie_seeker_q2_min_post1']), 
                  int(p['calorie_seeker_q3_min_post1']), 
                  int(p['calorie_seeker_q4_min_post1']), 
                  p['risk_level_post1'],
                  p['post1_getInfo_fake'],
                  p['post1_moreInfo_fake'],
                  p['pre1_getInfo_fake'] + p['pre1_moreInfo_fake'],
                  p['snackChoicePost1'],
                  p['calorie_influence_post1_fake']))

    def completed3(p):
      return ((p['completedPDQ3']==True) #and (p['sic']>=15) 
        )
    filtered_list3 = {k:v for (k,v) in all.items() if completed3(v)}

    with open(results_dir+'RQ4_G4H_cPre2.csv', 'w') as f:
      f.write ("snackBehav, grp, BIQseek, all_risky, button1, button2, buttons_all, SIC, PDQ")

      for (id,p) in filtered_list3.items():
        snacking_behavior = int((p['ffq1_risk']=='1' and (p['ffq2_score']<=11.45)))
        def toInt(g): return int(g=='gain')

        if(p['calorie_seeker_pre2']!='empty'):
          f.write ("%s,%s,%s,%s,%s,%s,%s,%s,%s\n" %
                  (snacking_behavior,
                  toInt(p['group']),
                  int(p['calorie_seeker_pre2']),
                  p['risk_level_pre2'],
                  p['pre2_getInfo_fake'],
                  p['pre2_moreInfo_fake'],
                  p['pre1_getInfo_fake'] + p['pre1_moreInfo_fake'],
                  p['snackChoicePre2'],
                  p['calorie_influence_pre2_fake']))

    def completed4(p):
      return ((p['completedPDQ4']==True) #and (p['sic']>=20) 
        )
    filtered_list4 = {k:v for (k,v) in all.items() if completed4(v)}

    with open(results_dir+'RQ4_G4H_dPost2.csv', 'w') as f:  ###since we opened up the CSV file, before the for loop we want to add a header
      f.write ("snackBehav, grp, BIQseek, all_risky, button1, button2, buttons_all, SIC, PDQ")

      for (idp,p) in filtered_list4.items():
        snacking_behavior = int((p['ffq1_risk']=='1' and (p['ffq2_score']<=11.45)))
        def toInt(g): return int(g=='gain')


        if(p['calorie_seeker_post2']!='empty'):
          f.write ("%s,%s,%s,%s,%s,%s,%s,%s,%s\n" %
                  (snacking_behavior,
                  toInt(p['group']),
                  int(p['calorie_seeker_post2']),
                  p['risk_level_post2'],
                  p['post2_getInfo_fake'],
                  p['post2_moreInfo_fake'],
                  p['pre1_getInfo_fake'] + p['pre1_moreInfo_fake'],
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
        # print (p['group']+","+p['pop']+","+str(p['sic'])+","+str(p['completedPDQ4'])) #, +end=",")
        # print (", ".join(list(map(pr,[1,3,4,7,8,9,11,14,15,18,19,20]))))
         ctr+=1

     except Exception as e:
         pass



