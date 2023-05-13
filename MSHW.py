import serial
import threading
import win32api, win32con
import mouse
import time

mauseX = 450
mauseY = 600

def receiveHandler():
    global counting;
    global mauseX, mauseY
    while(True):
        response = ser.readline()
        if len(response) > 0:
            strResponse = response.decode('utf-8');
            ACC = strResponse.split(",")
            print(ACC)
            ACCX1 = ACC[:1]
            ACCX = ''.join(ACCX1)
            print(ACCX)
            ACCY1 = ACC[:2][1:]
            ACCY = ''.join(ACCY1)
            
            ACCZ1 = ACC[:3][2:]
            ACCZ = ''.join(ACCZ1)

            CLICK1 = ACC[:4][3:]
            CLICK = ''.join(CLICK1)
            
            if(int(ACCX) > 400):
                mauseX = mauseX + 10
            elif(int(ACCX) < -400):
                mauseX = mauseX - 10

            if(int(ACCY) > 400):
                mauseY = mauseY + 10
            elif(int(ACCY) < -400):
                mauseY = mauseY - 10

            if(int(CLICK)):
                mouse.press('left')
            elif(int(CLICK)==0):
                mouse.release('left')
            
            print(mauseX)
            print(CLICK)
            if(strResponse == "B1\r\n"):
                counting = not counting;
            print("response={}".format(strResponse));


def ControlMause():
    counter = 2000
    while(counter > 0):
        win32api.SetCursorPos((mauseX,mauseY))
        counter = counter - 1
        time.sleep(0.01)


ser = serial.Serial('COM5', baudrate=115200,timeout=2)
print(ser.name)
ser.write(b'Hii')

t = threading.Thread(target=receiveHandler)
t1 = threading.Thread(target=ControlMause)
t.start();
t1.start();

