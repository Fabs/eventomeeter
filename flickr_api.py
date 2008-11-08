import flickrapi
from flickr_keys import *
from xml.etree import ElementTree
import sys

def auth_flickr(format='etree'):
    """login no flickr"""
    f = flickrapi.FlickrAPI(webapi,secret=websecret,format=format)
    return f

def get_recents(xml='etree'):
    """retorna o XML das fotos"""
    flickr = auth_flickr()
    recentes = flickr.photos_getrecent(user_id=userid, per_page='100',format=xml)
    return recentes

    
if __name__=='__main__':
    get_recents()
    
