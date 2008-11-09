import twitter
from content_analyst_api import *

from contextable import Contextable

'''
IDEAS
   Follow tinyurl no twitter
'''

class Twit(Contextable):
    def __init__(self,text):
        self.text = text
        self.content_tags = {}

    def relevant_content(self):
        return self.text

    def __str__(self):
        return "Twit <%s>"%(self.text)

    __repr__ = __str__

def getTwits():
    tw = twitter.Twitter()
    timeline = tw.statuses.public_timeline()
    twits = []
    for t in timeline:
        try:
            twit = Twit(str(t['text']))
            twits.append(twit)
        except UnicodeError:
            pass
     
    return twits
   
if __name__ == '__main__':
    dummy=getTwits()
    extractKeyWords(dummy)
