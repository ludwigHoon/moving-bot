#!/bin/python3
'''
The agent needs to be able to give meaningful visual outputs.
Personality class is to be expended for the usage of machine learning.
'''

from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math as m


class agent(object):
    def __init__(self, winLen=640, winWid=400, personality=None):
        self.person=personality
        self.cx=0
        self.cy=0
        self.winLen=winLen
        self.winWid=winWid
        self.scaleFac=1.0
        self.angle=.0

    def agentDisplay(self):
        self.confine()
        glPushMatrix()
        glTranslate(self.cx,self.cy,0)
        glScalef(self.scaleFac, self.scaleFac, 1)
        #Circle
        c=[100,200,255]
        glColor3ubv(c)
        glBegin(GL_LINE_LOOP)
        for a in range(720):
            step=2*m.pi*a/720
            glVertex2f(80*m.cos(step), 80*m.sin(step))
        glEnd()
        
        #Triangle
        glColor3ub(255,200,255)
        
        glRotatef(self.angle, 0, 0, 1)
        glBegin(GL_LINE_LOOP)
        for a in [90, 210, 330]:
            glVertex2f(80*m.cos(m.radians(a)), 80*m.sin(m.radians(a)))
        glEnd()
        
        glPopMatrix()

    def confine(self):
        if self.cx >=(self.winWid/2):
            self.cx=(self.winWid/2)
        if self.cx <=-(self.winWid/2):
            self.cx=-(self.winWid/2)
        if self.cy >=(self.winLen/2):
            self.cy=(self.winLen/2)
        if self.cy <=-(self.winLen/2):
            self.cy=-(self.winLen/2)
        if self.scaleFac<=0.2:
            self.scaleFac=0.2
        if self.scaleFac>=2:
            self.scaleFac=2

    def keyB(self, key, x, y):
        def moveUp():
            self.cy+=10
        def moveDown():
            self.cy-=10
        def moveLeft():
            self.cx-=5
        def moveRight():
            self.cx+=5
        def scaleUp():
            self.scaleFac+=0.2
        def scaleDown():
            self.scaleFac-=0.2
        def rotateC():
            self.angle+=10.0
        def rotateCC():
            self.angle-=10.0
        action={b'w':moveUp, b'a':moveLeft, b's':moveDown, b'd':moveRight, b'i':scaleUp, b'o':scaleDown, b'c':rotateC, b'v':rotateCC}
        if key in action.keys():
            action[key]()
        return
