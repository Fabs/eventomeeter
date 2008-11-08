import sys
import simplejson
import flickrapi
from flickr_keys import *


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
    flickr = authFlickr()
    recent = flickr.photos_getrecent(user_id=userid, per_page='3',format='json')
    recent_json = get_json(recent)
    photos = []
    for photo in recent_json['photos']['photo']:
        photo_json = get_json(flickr.photos_getInfo(photo_id=photo['id'], format='json'))
        photos.append({'url': ("http://farm%(farm)s.static.flickr.com/%(server)s/%(id)s_%(secret)s.jpg" % photo),
                     'json': photo_json,
                    })

    for photo in photos:
        print photo
    return photos

    
if __name__=='__main__':
    recent = getFlickers()
    print recent
	
