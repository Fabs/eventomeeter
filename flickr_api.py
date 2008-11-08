import flickrapi
from flickr_keys import *
import sys

def authFlickr(format='etree'):
    """login no flickr"""
    f = flickrapi.FlickrAPI(webapi,secret=websecret,format=format)
    return f

def getFlickers(xml='etree'):
    flickr = authFlickr()
    recent = flickr.photos_getrecent(user_id=userid, per_page='1',format='json')
    url="""http://farm.static.flickr.com/server/id_secret.jpg"""
    print "URL:" + url
    return recent
  
    
if __name__=='__main__':
    recent = getFlickers()
    print recent
	
