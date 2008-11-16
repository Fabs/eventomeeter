#!/usr/bin/env python
# coding: utf8
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import pickle
import time
import urllib

def get_img(url):
    #img_url = 'http://farm2.static.flickr.com/1020/1397356537_b10c59211d.jpg?v=0'
    img_name = url.split('/')[-1]
    if not os.path.exists(img_name):
        img = urllib.urlretrieve(url, img_name)
    return img_name

last_file = 0
def file_name():
    return '%s.pickle' % last_file

while True:
    if os.path.exists(file_name()):
        data = pickle.load(file(file_name()))
        for item in data['items']:
             print item
             if item['type'] == 'flickr':
                try:
                    item['url'] = get_img(item['url'])
                except Exception, e:
                    #print 'url'
                    #print e
                    #print item['url']
                    item['url'] = None
        pickle.dump(data, file(('%d_out.pickle' % last_file), 'w'))
        last_file += 1
    time.sleep(1)


