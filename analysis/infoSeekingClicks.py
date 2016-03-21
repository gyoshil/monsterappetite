import query_dbs

def splitInfo(info):
  prev = 0
  for index,x in enumerate(info):
   next = x['round']
   if (next < prev):
     return [info[0:index]] + (splitInfo (info[index:len(info)]))
   prev=next
  return [info]

def gatherClicks(which,session,p):
  try:
    mongoPlayer = query_dbs.findPlayerInMongo('_id',p[0])
    filteredInfo = mongoPlayer['informationSeekingBehavior']
    i = splitInfo(filteredInfo)
  except KeyError:
    i = [[]]
  i.append([])
  i.append([])
  i.append([])

  sessionInfo = i[session]
  count = 0
  for b in sessionInfo:
    if (b['button']==which):
      count = count+1
  return count
