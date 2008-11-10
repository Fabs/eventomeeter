import sys
import simplejson
import flickrapi
from flickr_keys import *
import time, cPickle

from contextable import Contextable

class Photo(Contextable):
    def __init__(self, url, tags, username, lastupdate):
        self.tags = tags
        self.url = url
        self.username = username
        self.content_tags = {}
        self.lastupdate = lastupdate

    def relevant_content(self):
        return ""

    def __repr__(self):
        return "Flick <%s> <%s> <%s> <%s>"%(self.tags, self.url, self.username, self.lastupdate)

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
    tags = 0
    photos = []
    flickr = authFlickr()
    recent = flickr.photos_search(tags="brhackday08", 
                                  per_page='500',format='json',
                                  extras='tags,last_update,owner_name')
    recent_json = get_json(recent)
    for photo in recent_json['photos']['photo']:
       tag_list = [tag for tag in photo['tags'].split()]
       tags += len(tag_list)
       photo_object = Photo(
        ("http://farm%(farm)s.static.flickr.com/%(server)s/%(id)s_%(secret)s.jpg" %     photo),
        tag_list,
        photo['ownername'],
        photo['lastupdate'],
       )
       photos.append(photo_object)
    return photos
