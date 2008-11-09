#!/usr/bin/env python
# coding: utf8
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import cocos
from cocos.actions import *


class Panel(cocos.layer.ColorLayer):
    def __init__(self):
        super(Panel, self).__init__(255, 255, 255, 255)

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
        position = 30,30

if __name__ == '__main__':
    cocos.director.director.init()
    panel = Panel()
    cl = Cluster(100, (320, 240))
    panel.add(cl)
    tags = [('teste1',30),('teste2',30),('teste3',30),('teste4',30),('teste5',30)]
    cl.addTags(tags)
    cl.moveTo(0)

    main_scene = cocos.scene.Scene(panel)

    cocos.director.director.run(main_scene)
