import flickrapi
from flickr_keys import *
import sys

class Photo:
   def __init__(self,url,tags):
      self.tags = tags
      self.url = url
   
   def relevant_content(self):
      pass
   
   def __str__(self):
      "text: %s tags: %s"%(self.text,self.tags)
      
   __repr__ = __str__
   

def authFlickr(format='etree'):
    """login no flickr"""
    f = flickrapi.FlickrAPI(webapi,secret=websecret,format=format)
    return f

def getFlickers(xml='etree'):
    """retorna o XML das fotos"""
    flickr = authFlickr()
    recent = flickr.photos_getrecent(user_id=userid, per_page='1',format='json')
    return recent

    
if __name__=='__main__':
    print getFlickers()
