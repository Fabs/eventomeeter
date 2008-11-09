from content_analyst_api import extractKeyWords
from twitter_api import getTwits
from flickr_api import getFlickers

def dig_web():
    twits = getTwits()
    photos = getFlickers()
    words = []
    for twit in twits:
        twit.content_tags = extractKeyWords(twit)
        words.append(twit)
    for photo in photos:
        photo.content_tags = photo.tags
        words.append(photo)
    return words

if __name__ == "__main__":
    print dig_web()