import query_dbs
import card_info

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
  #I believe if below was "return (count) then the original ALL clicks would be produced"
  return min(9,count)

def gatherClicksFake(which,session,p):
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
    if (b['button']==which and (b['name'] in card_info.fake_cards)):
      count = count+1
  #I believe if below was "return (count) then the original ALL clicks would be produced"
  return min(9,count)
