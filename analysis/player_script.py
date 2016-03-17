import bson
from pprint import pprint
from bson.codec_options import CodecOptions

bson_file = open('players.bson','rb')
b = bson.decode_all(bson_file.read())

print len(b)


def printPlayer(player):
  for f in player:
    print f
  #print player[u'snackazonItemChoices']
  print player[u'informationSeekingBehavior']

printPlayer(b[200])
print b[200][u'name']

for player in b:
  printPlayer(player)

