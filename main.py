import agent as ag
from threading import Thread
from rgui import *
from bot import *
import time


def printTime():
    while True:
        print(time.ctime(time.time()))

if __name__ == '__main__':
    ob=ag.agent()
    bb=bot()
    #bb.ru()
    Thread(target=bb.ru).start()
    a=GUI(ob, bb)
    Thread(target=a.run).start()
    #thread.start_new_thread(bb.ru)
    #thread.start_new_thread(a.run)
    #bb.ru()
    #a.run()

