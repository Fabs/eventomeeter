from content_analyst_api import extractKeyWords
from twitter_api import getTwits

twits = getTwits()
words = []
for twit in twits:
    words.append(extractKeyWords(twit))
photos = getFlickers()
for photo in photos:
    photo_tags = extractKeyWords(photo) + photo.tags
    words.append(photo_tags)

print words