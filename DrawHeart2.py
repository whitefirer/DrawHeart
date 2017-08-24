# -*- coding: utf8 -*-
from ctypes import *
from time import sleep
import os, math
advapi32 = windll.LoadLibrary('advapi32.dll')
user32 = windll.LoadLibrary('user32.dll')

def DrawTo(x1, y1, x2, y2):
    user32.SetCursorPos(int(x1), int(y1))
    user32.mouse_event(0x0002, 0, 0, 0, 0)
    user32.SetCursorPos(int(x2), int(y2))
    user32.mouse_event(0x0004, 0, 0, 0, 0)
    sleep(0.01)
    
def MoveTo(x, y):
    user32.SetCursorPos(int(x), int(y))

def DrawHeart(startx, starty, w, h):
    t = 0
    x,y = 0,0
    ox,oy = 0,0
    while t < 2*math.pi:
        if x != 0 and y != 0:
            ox = x
            oy = y
        x = (1 + math.pow(math.sin(t), 3))*w + startx
        y = (1 - 1*math.cos(t) + 5/13.0*math.cos(2*t) + 2/13.0*math.cos(3*t) + 1/13.0*math.cos(4*t))*h + starty
        if(0==t):
            MoveTo(x, y)
        else:
            DrawTo(ox, oy, x, y)
        t += 0.01

os.startfile("mspaint")
sleep(0.5)
user32.ShowWindow(user32.GetForegroundWindow(), 3)
sleep(0.5)

DrawHeart(20, 200, 160, 130)
