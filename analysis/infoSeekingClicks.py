import query_dbs

def splitInfo(info):
  prev = 0
  for index,x in enumerate(info):
   next = x['round']
   if (next < prev):
     return [info[0:index]] + (splitInfo (info[index:len(info)]))
   prev=next
  return [info]

def gatherClicks(session,p):
  try:
    i = splitInfo(query_dbs.findPlayerInMongo('_id',p[0])['informationSeekingBehavior'])
  except KeyError:
    i = [[]]
  i.append([])
  i.append([])
  i.append([])
  i = list(map(len,i))

  return (i[session])
