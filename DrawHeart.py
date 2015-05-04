# -*- coding: gbk -*-
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

def DrawRotateEllipse(x, y, r1, r2, ll, rl, a, starta, enda):
	sina = math.sin(a);
	cosa = math.cos(a);
	nx,ny = 0,0
	ox,oy = 0,0
	for i in range(starta, enda+1):
		xorig =  r1 * math.cos((i) * (math.pi/180));
		yorig =  r2 * math.sin((i) * (math.pi/180));
		if nx != 0 and ny != 0:
			ox = nx
			oy = ny
		nx = x + xorig * cosa + yorig * sina;
		ny = y + yorig * cosa - xorig * sina;
		if(0==i) or (nx<ll) or (nx>rl):
			MoveTo(nx, ny)
		else:
			DrawTo(ox, oy, nx, ny)
			

os.startfile("mspaint")
sleep(0.5)
user32.ShowWindow(user32.GetForegroundWindow(), 3)
sleep(0.5)

x = 300.0
y = 200.0
DrawRotateEllipse(x, y+160, y/3, y*2/3, 0, x, math.pi/4, 0, 360);
DrawRotateEllipse(x, y+160, y/3, y*2/3, x, x*2 , -math.pi/4, 91, 360);
DrawRotateEllipse(x, y+160, y/3, y*2/3, x, x*2 , -math.pi/4, 0, 90);#因为在WIN7以上系统画图框更高，加个偏移
