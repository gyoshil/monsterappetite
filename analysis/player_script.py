import bson
from pprint import pprint
from bson.codec_options import CodecOptions

bson_file = open('C:/Users/GGU/Documents/GitHub/monsterappetite/analysis/players.bson','rb')
players = bson.decode_all(bson_file.read())

print ("Total players found: "+ str(len(players))+ '\n')

print("Fields available:")
for f in players[0]:
  print (f)
print ("\n")

firstItem = players[0]['snackazonItemChoices'][0]

'''
print (firstItem)
print (firstItem['round'])
print (firstItem['item'])
print (firstItem['item']['round'])
'''


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

'''
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
'''
#print (session1)
#print (session2)
#for player in b:
#  printPlayer(player)
