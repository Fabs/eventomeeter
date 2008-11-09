#!/usr/bin/env python
# coding: utf8
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import cocos
from cocos.actions import *
from pyglet.window import key

width = 800
height = 600

class Panel(cocos.layer.ColorLayer):
    is_event_handler = True
    
    def __init__(self):
        super(Panel, self).__init__(255, 255, 255, 255)

    def on_key_press( self, k , m ):
        if k == key.ENTER:
            cl.moveTo(1)
            cocos.director.director.replace(cocos.scene.Scene(self))
            
class Cluster(cocos.sprite.Sprite):
    lastImg = '0'
    def __init__(self, scale, position):
        img = 'cloud' + self.lastImg + '.gif'
        #self.lastImg+=1
        #self.lastImg%=10
        scale = 0.01*scale
        super(Cluster, self).__init__(image=img, scale=scale, opacity=180, position=position)

    def addTags(self, tags):
        html = ''
        for i,tag in enumerate(tags):
            html+='<font size=%d>%s</font> ' % ((5-i)*20,tag[0])
        tagFormatted = cocos.text.HTMLLabel(html,
                x=-self.width/2+30, width=self.width-60, multiline=True)

        self.add(tagFormatted)

    def moveTo(self, position):
        if position==1:
            newW = width - width/6
            newH = height - height/6
        elif position==2:
            newW = width - width/6
            newH = height/6
        elif position==3:
            newW = width/6
            newH = height/6
        elif position==4:
            newW = width/6
            newH = height - height/6
            
        ju_right = JumpBy( (newW,newH), height=100, jumps=4, duration=5 )
        self.do(ju_right)

def callData(dt, *args, **kwargs):
    # aqui vai o que hoje esta no key_press
    print dt

if __name__ == '__main__':
    cocos.director.director.init(resizable=True, width=width, height=height)

    panel = Panel()
    panel.schedule_interval(callData, 3)
    cl = Cluster(100, (320, 240))
    panel.add(cl)
    tags = [('teste1',30),('teste2',30),('teste3',30),('teste4',30),('teste5',30)]
    cl.addTags(tags)
    scene = cocos.scene.Scene(panel)

    cocos.director.director.run(scene)
    
    

