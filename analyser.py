from content_analyst_api import extractKeyWords
from twitter_api import getTwits

twits = getTwits()
words = []
for twit in twits:
   words.append(extractKeyWords(twit))

print words