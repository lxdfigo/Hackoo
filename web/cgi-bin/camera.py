from VideoCapture import Device
import time
import string
import Image
import cmath
import win32api
import win32con
import os
import pythoncom
import pyHook
import threading

def updata():
    #os.popen("updata.py hackoo")
	return 0


def mouselistener():
    hm = pyHook.HookManager()
    hm.MouseMiddleUp = OnMouseEvent
    hm.HookMouse()
    pythoncom.PumpMessages()
	
	
def keyboardlistener():
    hm = pyHook.HookManager()
    hm.KeyDown = OnKeyboardEvent
    hm.HookKeyboard()
    pythoncom.PumpMessages()
	

def OnMouseEvent(event):
    global midup
    midup = (midup + 1) % 2
    #print midup
    return True

def OnKeyboardEvent(event):
    global rejust
    if event.KeyID == 123:
	    rejust = 1
    return True
	

def writeup(opt):
    print >>fout,opt
	

def press(dir,midup):
    if midup == 0:
        if dir == 0:
            win32api.keybd_event(8,0,0,0) #press backspace
            win32api.keybd_event(8,0,win32con.KEYEVENTF_KEYUP,0) #release
        if dir == 1:
            win32api.keybd_event(16,0,0,0) #press shift
            win32api.keybd_event(8,0,0,0) #press backspace
            win32api.keybd_event(8,0,win32con.KEYEVENTF_KEYUP,0) #release
            win32api.keybd_event(16,0,win32con.KEYEVENTF_KEYUP,0) #release
    elif midup == 1:
        if dir == 0:
            win32api.keybd_event(33,0,0,0) #press pageup
            win32api.keybd_event(33,0,win32con.KEYEVENTF_KEYUP,0)
        if dir == 1:
            win32api.keybd_event(34,0,0,0) #press pagedown
            win32api.keybd_event(34,0,win32con.KEYEVENTF_KEYUP,0) #release

def cal(data):
    return data[0]*data[0]+data[1]*data[1]+data[2]*data[2]

def smooth(x):
    if x.real>200:
        return 200
    if x.real<-200:
        return -200
    return 0
	
def analysis(s):
    imnow = Image.open(s)
    limnow = imnow.load()
    nx = ny =0
    #print limnow[1,1][0]-limbase[1,1][0],limnow[1,1][1]-limbase[1,1][1],limnow[1,1][2]-limbase[1,1][2]
    for i in range(int(0.2 * size[0]),int(0.8 * size[0])):
        #print nx
        for j in range(int(0.2 * size[1]),int(0.8 * size[1])):
            nx += (i - size[0] / 2) * smooth((cmath.sqrt(cal(limnow[i,j])) - cmath.sqrt(cal(limbase[i,j]))))
    return nx.real

	
	
def adjust():
    global size
    global leftbound
    global rightbound
    global limbase
    print "sit to the middle then press enter"
    hehe = raw_input()
    hehe = raw_input()
    cam.saveSnapshot('pic\\base.jpg', timestamp=3, boldfont=1, quality=75)
    imbase = Image.open("pic\\base.jpg")
    size = imbase.size
    limbase = imbase.load()

    print "sit to the left then press enter"
    hehe = raw_input()
    cam.saveSnapshot('pic\\left.jpg', timestamp=3, boldfont=1, quality=75)
    imleft = Image.open("pic\\left.jpg")
    limleft = imleft.load()

    print "sit to the right then press enter"
    hehe = raw_input()
    cam.saveSnapshot('pic\\right.jpg', timestamp=3, boldfont=1, quality=75)
    imright = Image.open("pic\\right.jpg")
    limright = imright.load()

    leftbound = analysis("pic\\left.jpg")
    rightbound = analysis("pic\\right.jpg")
    
    global rejust
    rejust = 0


interval = 0.3 #this is the interval time between two captures
opinterval = 0.6 #this is the interval time between two operate
rejust = 0
ratio = 0.95
midup = 0
size = []
leftbound = 0
rightbound = 0
fulltime = time.localtime(time.time())
year = fulltime.tm_year
mon = fulltime.tm_mon
day = fulltime.tm_mday

updata()
if os.path.exists(".\\log") == False:
    os.mkdir("log")
fout = open("log\\%d_%d_%d.log" % (year,mon,day),"a+")
cam = Device(devnum=0, showVideoWindow=0)
cam.saveSnapshot('pic\\base.jpg', timestamp=3, boldfont=1, quality=75)
imbase = Image.open("pic\\base.jpg")


adjust()

t = threading.Thread(target = mouselistener , args = ())
t.start()
t2 = threading.Thread(target = keyboardlistener , args = ())
t2.start()

i = 0
quant = interval * .1
starttime = optime =time.time()
while 1:
    lasttime = now = int((time.time() - starttime) / interval)
    #print "% seconds passed...\n",(i)
    if rejust == 1:
        adjust()
    cam.saveSnapshot('pic\\now.jpg', timestamp=3, boldfont=1)
    if time.time()-optime>opinterval:
        ret = analysis("pic\\now.jpg")
        if leftbound>rightbound:
            if ret > ratio * leftbound:
                print "Left!!!"
                optime=time.time()
                press(0,midup)
                writeup(0)
            elif ret < ratio * rightbound:
                print "Right!!!"
                optime=time.time()
                press(1,midup)
                writeup(1)

        if leftbound<rightbound:
            if ret < ratio * leftbound:
                print "Left!!!"
                optime=time.time()
                press(0,midup)
                writeup(0)
				
            elif ret > ratio * rightbound:
                print "Right!!!"
                optime=time.time()
                press(1,midup)
                writeup(1)
    i += 1
    while now == lasttime:
        now = int((time.time() - starttime) / interval)
        time.sleep(quant)
