import time,random,feedparser

while True:
  year = str(random.randint(8, 16)).zfill(2)
  if year == '15':
    month = str(random.randint(1, 05)).zfill(2)
  else:
    month = str(random.randint(1, 12)).zfill(2)
  rid = str(random.randint(1, 100)).zfill(2)

  url = 'http://export.arxiv.org/api/query?id_list=' + year +''+ month + '.00' + rid
  article_url = 'http://arxiv.org/abs/' + year +''+ month + '.00' + rid
  
  d = feedparser.parse(url)
  title = d['entries'][0]['title']
  
  print title.encode('utf-8')

  time.sleep(5)

