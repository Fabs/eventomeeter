import flickrapi
from flickr_keys import *
import sys

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
    recent = getFlickers()
    print recent
