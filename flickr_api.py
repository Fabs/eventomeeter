import sys
import simplejson
import flickrapi
from flickr_keys import *


class Photo:
    def __init__(self,url,tags):
        self.tags = tags
        self.url = url
        self.content_tags = {}

    def relevant_content(self):
        return ""

    def __str__(self):
        return "text: %s tags: %s"%(self.text,self.tags)

    __repr__ = __str__

def authFlickr(format='etree'):
    """login no flickr"""
    f = flickrapi.FlickrAPI(webapi,secret=websecret,format=format)
    return f

def get_json(text):
    start_str = 'jsonFlickrApi('
    if text.startswith(start_str):
       text = text[len(start_str):-1]
    json = simplejson.loads(text)
    return json

def getFlickers():
   tag_count = 0
   flickr = authFlickr()
   recent = flickr.photos_getrecent(user_id=userid, per_page='300',format='json')
   recent_json = get_json(recent)
   photos = []
   for photo in recent_json['photos']['photo']:
       photo_json = get_json(flickr.photos_getInfo(photo_id=photo['id'], format='json'))
       try:
           photo_object = Photo(
                ("http://farm%(farm)s.static.flickr.com/%(server)s/%(id)s_%(secret)s.jpg" % photo),
                [tag['_content'] for tag in photo_json['photo']['tags']['tag']]
                )
           photos.append(photo_object)
           tag_count += len(photo_object.tags)
       except: pass
   print tag_count       
   return photos


if __name__=='__main__':
    getFlickers()
