from pprint import pprint
import csv

def printAll(ps):

  #########
  ## HEADERS
  #########
  print ('uid',end=', ')
  for fields in sorted(ps.popitem()[1]):
    print (fields,end=', ')
  print ()

  #########
  ## VALUES
  #########
  for p in ps.items():
    print (p[0],end=', ')
    for key in sorted(p[1]):
      print (p[1][key],end=', ')
    print ()


#with open('compiled_results.csv', 'w') as f:
#  w = csv.DictWriter(f, ps['peZip3nZ25pQ4ism4'].keys())
  #w.writeheader()
