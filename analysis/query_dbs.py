import bson
from bson.codec_options import CodecOptions
from pprint import pprint
import csv

dataDir = './Qualtrics/'
bson_file = open('./players.bson','rb')
mongoPlayers = bson.decode_all(bson_file.read())

'''def filterMongoPlayers(players,condition):
  filtered = {}
  for p in players.items():
    if (not condition(p)):
      filtered.append(p)'''

def tagMongoPlayers(players,valueFunc):
  for p in players.items():
    players[p[0]][valueFunc.__name__]=valueFunc(p)


def tagCSVPlayers(csvFile,players,fieldName,valueFunc):
  id_index = {
    "BIQ1.csv":0,"BIQ2.csv":0,"BIQ3.csv":0,"BIQ4.csv":0,
    "PDQ1.csv":4,"PDQ2.csv":4,"PDQ3.csv":4,"PDQ4.csv":4,
    "DQ.csv":1,
    "FFQ1.csv":1,"FFQ2.csv":1}
  with open(dataDir+csvFile, mode='r') as infile:
    qualtrics = list(csv.reader(infile))
    count =0
    for p in players.items():
      q = "NONE"
      for qp in qualtrics:
        if(p[0]==qp[id_index[csvFile]]):
          q = qp
      players[p[0]][fieldName]=valueFunc(p,q)


def allMongoPlayers():
  allPlayers = {}
  print (mongoPlayers[0])
  for p in mongoPlayers:
    allPlayers[p['_id']]={}
  return allPlayers

def findPlayerInMongo(field,value):
  global mongoPlayers
  for p in mongoPlayers:
    if (p[field]==value):
      return p
  return False
