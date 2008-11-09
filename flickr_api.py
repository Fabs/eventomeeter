import sys
import simplejson
import flickrapi
from flickr_keys import *
import time

from contextable import Contextable

class Photo(Contextable):
    def __init__(self,url,tags):
        self.tags = tags
        self.url = url
        self.content_tags = {}

    def relevant_content(self):
        return ""

    def __repr__(self):
        return "Flick <%s>"%(self.tags)

    __str__ = __repr__

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
    enter_time = time.time()
    tags = 0
    photos = []
    flickr = authFlickr()
    recent = flickr.photos_search(tags="brhackday08", per_page='500',format='json',extras='tags')
    recent_json = get_json(recent)
    #print "Down: "+str(len(recent_json['photos']['photo']))
    for photo in recent_json['photos']['photo']:
       tag_list = [tag for tag in photo['tags'].split()]
       tags += len(tag_list)
       if not tag_list: continue
       photo_object = Photo(
            ("http://farm%(farm)s.static.flickr.com/%(server)s/%(id)s_%(secret)s.jpg" %     photo),
            tag_list
            )
       photos.append(photo_object)
    #print (time.time() - enter_time) / 60
    #print "Photos: "+str(len(photos))
    #print "Tag: "+str(tags)
    return photos

if __name__=='__main__':
    while True:
        print len(getFlickers())
