import twitter

'''
IDEAS
   Follow tyniurl no twitter
'''

class Twit:
    def __init__(self,text):
        self.text = text
        self.content_tags = {}

    def relevant_content(self):
        return self.text

    def __str__(self):
        return "'%s'"%(self.text)

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
   print getTwits()
