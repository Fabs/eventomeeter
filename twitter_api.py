import twitter

def getTwits():
   tw = twitter.Twitter()
   timeline = tw.statuses.public_timeline()
   twits = []
   for twit in timeline:
      try:
         twits.append(str(twit['text']))
      except UnicodeError:
         pass
         
   return twits
   
if __name__ == '__main__':
   print getTwits()
