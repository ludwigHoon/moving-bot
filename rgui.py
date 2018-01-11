from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
import time

class GUI:
    def __init__(self, obj=None, trained=None):
        self.winName='Robot'
        self.winWid=(400)
        self.winLen=(640)
        self.obj=obj
        self.bot=trained

    def checkM(self, val):
        self.keyboard(self.bot.act(), 0,0)
        glutTimerFunc(100, self.checkM, 0)

    def run(self, control=None):
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB)
        glutInitWindowSize(self.winWid, self.winLen)
        glutCreateWindow(self.winName)
        glViewport(0,0,self.winWid,self.winLen)
        gluOrtho2D(-(self.winWid/2), self.winWid/2, -(self.winLen/2), self.winLen/2)
        glutDisplayFunc(self.display)
        glutKeyboardFunc(self.keyboard)
        glClearColor(0.,0.,0.,1.)
        glutIdleFunc(self.display)
        glutTimerFunc(0, self.checkM, 0)
        glutMainLoop()
        return

    def keyboard(self, key, x, y):
        if key == b'q':
            time.sleep(0.3)
            glutLeaveMainLoop()
        if self.obj is not None:
            self.obj.keyB(key, x, y)

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT)
        if self.obj is not None:
            self.obj.agentDisplay()
        glutSwapBuffers()
        return 

