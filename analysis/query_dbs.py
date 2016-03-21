import bson
from bson.codec_options import CodecOptions
from pprint import pprint
import csv

dataDir = 'C:/Users/GGU/Documents/GitHub/monsterappetite/analysis/Qualtrics/'
bson_file = open('C:/Users/GGU/Documents/GitHub/monsterappetite/analysis/players.bson','rb')
mongoPlayers = bson.decode_all(bson_file.read())

'''def filterMongoPlayers(players,condition):
  filtered = {}
  for p in players.items():
    if (not condition(p)):
      filtered.append(p)'''

def tagMongoPlayers(players,valueFunc):
  for p in players.items():
    players[p[0]][valueFunc.__name__]=valueFunc(p)


def tagCSVPlayers(csvFile,players,valueFunc):
  id_index = {"PDQ2.csv":3,"PDQ4.csv":4,"BIQ1.csv":0,"BIQ2.csv":3,"BIQ3.csv":3,"BIQ4.csv":0}
  with open(dataDir+csvFile, mode='r') as infile:
    qualtrics = list(csv.reader(infile))
    count =0
    for p in players.items():
      q = "NONE"
      for qp in qualtrics:
        if(p[0]==qp[id_index[csvFile]]):
          q = qp
      players[p[0]][valueFunc.__name__]=valueFunc(p,q)


def allMongoPlayers():
  allPlayers = {}
  for p in mongoPlayers:
    allPlayers[p['_id']]={}
  return allPlayers

def findPlayerInMongo(field,value):
  global mongoPlayers
  for p in mongoPlayers:
    if (p[field]==value):
      return p
  return False
