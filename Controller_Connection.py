#import Tkinter module
from Tkinter import *
# from PIL import Image, ImageTk, ImageFilter, ImageEnhance

import serial
import time
import traceback
import struct
import Robot

# class Robot:

# START UP COMMANDS
reset = 7
start = 128
safe  = 131
full  = 132
# LED COMMANDS
LED       = 139
HomeLED   = 4
Intensity = 0    #0 - 255
Color     = 255  #0 - 255 (green - red)

# DRIVE commands
try:
    ser = serial.Serial("COM3", baudrate=115200, timeout =1)
    print "Connected"
except serial.SerialException:
    print "Connection failure!"

time.sleep(0.01)
ser.close()
time.sleep(0.01)
ser.open()

ser.write(chr(128))
time.sleep(0.01)
ser.write(chr(131))
time.sleep(0.01)

#print out method
def write_forward(x):
    print("FORWARD")
    ser.write(chr(137) + chr(0) + chr(146) + chr(0) + chr(0))
    
def write_stop(x):
    print("STOP")
    ser.write(chr(137) + chr(0) + chr(0) + chr(0) + chr(0))

#frame
root = Tk()
frame = Frame(root)
frame.pack()

#forward
FWD_Input = Button(frame,
                   text="Forward",
                   command=write_forward)
FWD_Input.pack(side=TOP)

root.bind('w', write_forward)

root.bind('<KeyRelease>', write_stop)

#loop
root.mainloop()
