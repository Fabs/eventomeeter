#!/usr/bin/env python
# coding: utf8
import sys
import os
import random
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
#sys.path.insert(0, '/opt/local/lib/python2.5/site-packages/PIL-1.1.6-py2.5-macosx-10.3-i386.egg')

import cocos
from cocos.actions import *
from pyglet.window import key
import pyglet
import pickle

import urllib
#import urlparse
#from PIL import Image

width = 800
height = 600
slowness= 128.0 / 50
last_file = 0
buffer = []
taxa_flickr = 0
taxa_twitter = 0

def file_name():
    return '%s_out.pickle' % last_file
	#return '%s.pickle' % last_file

def fake_buffer():
    global buffer
    items = [{'type': 'twitter', 'text': 'asfasdasd', 'user': 'rbp'},
                   {'type': 'twitter', 'text': 'sdga;lgpsdF', 'user': 'rbp'},
                   {'type': 'twitter', 'text': 'wep3-0wf-0', 'user': ''},
                   {'type': 'twitter', 'text': 'sdfsdfsdfsasfasdasd', 'user': 'lucmult'},
                   {'type': 'twitter', 'text': 'asfasdasd as df dsf ', 'user': 'lucmult'},
                   ]
    #for i in [it for it in items if it['type'] == 'flickr']:
    #    img = Image.open(i['url'])
    #    img.resize(160, 120)
    #    img.save()

    random.shuffle(items)
    buffer.extend(items)

def start_pos():
    candidates = [(0, 0), (0, height), (width, 0), (width, height)]
    return random.choice(candidates)

def text_colour():
    candidates = ["#FF0000", "#00FF00", "#0000FF"]
    return random.choice(candidates)

def fill_buffer():
    global buffer, taxa_flickr, taxa_twitter, last_file
    if os.path.exists(file_name()):
        try:
            data = pickle.load(file(file_name()))
        except:
            return
        #buffer.extend([i for i in data['items'] if i['type'] == 'twitter'])
        buffer.extend([i for i in data['items']])
        taxa_flickr = data.get('taxa_flickr', 250)
        taxa_twitter= data.get('taxa_twitter', 0)
        last_file += 1
    # DEBUG
    #fake_buffer()
    #taxa_twitter = random.randint(0, 5)

def float_rate():
    #rate = 1.0 / (taxa_twitter + 1)
    rate = 1.0 / 2**((taxa_twitter + 1)/2.0)
    print rate
    return rate

def callData(dt, *args, **kwargs):
    global buffer
    print kwargs
    print buffer
    panel = kwargs['panel']
    if not buffer:
        fill_buffer()
        if buffer:
            panel.unschedule(callData)
            panel.schedule_interval(callData, float_rate(), panel=panel)
        else:
            panel.schedule_interval(callData, 1, panel=panel)
        return
    item = buffer.pop(0)
    cl = Cluster(100, start_pos())
    panel.add(cl)
    if item['type'] == 'twitter':
        cl.add_text(item['text'], item['user'])
    elif item['type'] == 'flickr':
        cl.add_img(item['url'], item['user'])
    cl.moveTo()
    #if len(buffer) == 0:
    #    # Mostra que estah atualizando...


class Panel(cocos.layer.ColorLayer):
    is_event_handler = True
    
    def __init__(self):
        super(Panel, self).__init__(64, 64, 64, 64)

    def on_key_press( self, k , m ):
        global buffer, taxa_twitter
        if k == key.ENTER:
            fill_buffer()
            panel.schedule_interval(callData, float_rate(), panel=self)
        elif k == key.ESCAPE:
            #self.parent.on_exit()
            pyglet.app.exit()

class User(cocos.sprite.Sprite):
    def __init__(self, name, posts):
        self.name = name
        self.posts = posts

        texto = cocos.text.Label(name)
        super(User, self).__init__(image='space.jpg', position=(150, 150))
        self.add(texto)


class Cluster(cocos.sprite.Sprite):
    lastImg = '0'
    def __init__(self, scale, position):
        #img = 'cloud' + self.lastImg + '.gif'
        img = 'fundo.gif'
        #self.lastImg+=1
        #self.lastImg%=10
        scale = 0.01*scale
        super(Cluster, self).__init__(image=img, scale=scale, opacity=180, position=position)

    def add_text(self, text, user):
        colour = text_colour()
        name_colour = "#FFFFFF"
        html = '<font size="%s" color="%s">%s</font><br><b><font color="%s">%s</size></b> ' % (
                "+3", colour, text, name_colour, user)
        formatted = cocos.text.HTMLLabel(html,
                x=-self.width/2+30, width=self.width-60, multiline=True)
        self.add(formatted)

    def add_img(self, url, user):
        try:
            sp_img = cocos.sprite.Sprite(image=url, opacity=200, scale=0.3) 
        except:
            return
        self.add(sp_img)

    def moveTo(self):
        newW = width/2  - self.position[0]
        newH = height/2 - self.position[1]
            
        ju_right = JumpBy( (newW,newH), height=100, jumps=1, duration=slowness)
        self.do(ju_right)


if __name__ == '__main__':
    cocos.director.director.init(resizable=True, width=width, height=height)

    panel = Panel()
    panel.add(cocos.sprite.Sprite('layout/layouts/layout_em_3.gif',
                                  position=(width/2, height/2),
                                  ),
              -1)
    scene = cocos.scene.Scene(panel)
    cocos.director.director.run(scene)

