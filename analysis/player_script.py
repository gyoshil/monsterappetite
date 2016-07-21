import bson
from pprint import pprint
from bson.codec_options import CodecOptions

bson_file = open('./players.bson','rb')
players = bson.decode_all(bson_file.read())

print ("Total players found: "+ str(len(players))+ '\n')

print("Fields available:")
for f in players[0]:
  print (f)
print ("\n")

#pprint ( players[1]['informationSeekingBehavior'])
z05 = 0
z510= 0
z1015 = 0
z1520 = 0


for p in players:
 #start counting at 1, leave first spot blank
 #also need an extra for crappy data
 allClickCounts1 = [0]* 22
 allClickCounts2 = [0]* 22
 try:
     print (p['group']+","+p['pop'], end=",")
 except Exception as e:
      print (p['group']+",NA", end=",")
 s = len(p['snackazonItemChoices'])
 try:
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
     def p(i):
       return str(allClickCounts1[i])+", "+str(allClickCounts2[i])+""
     print (", ".join(list(map(p,[1,3,4,7,8,9,11,14,15,18,19,20]))))
 except KeyError as e:
      print ("NA,NA")

'''
print (firstItem)
print (firstItem['round'])
print (firstItem['item'])
print (firstItem['item']['round'])



def splitInfo(info):
  prev = 0
  for index,x in enumerate(info):
   next = x['round']
   if (next < prev):
     return [info[0:index]] + (splitInfo (info[index:len(info)]))
   prev=next
  return [info]

count = 0
num_p = 0


session1pre = 0
session1post = 0
session2pre = 0
session2post = 0


def printPlayer(player):
  #print (len(player['performance']))
  global count, session1, session2, num_p
  try:
    i = splitInfo(player['informationSeekingBehavior'])
  except KeyError:
    i = [[]]
  i.append([])
  i.append([])
  i.append([])
  i = list(map(len,i))
  #count = count+i[0]+i[1]+i[2]+i[3]
  session1pre += i[0]
  session1post += i[1]
  session2pre += i[2]
  session2post += i[3]
for p in players:
  printPlayer(p)

print (session1)
print (session2)


for p in players:
  if (p['group'] ==("gain")):
    printPlayer(p)
print (num_p)
print (count)
print (session1/session2)
#print (session2)
count = 0
num_p =0
session1 =0
session2 =0
for p in players:
  if (p['group'] ==("loss")):
    printPlayer(p)
print (num_p)
print (count)
print (session1/session2)
#print (session2)

#print (session1)
#print (session2)
#for player in b:
#  printPlayer(player)
'''
