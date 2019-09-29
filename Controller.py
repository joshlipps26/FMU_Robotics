#import Tkinter module
import Tkinter as tk
import Robot
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
def write_forward():
    print("FORWARD")
    ser.write(chr(137) + chr(0) + chr(146) + chr(0) + chr(0))

def write_reverse():
    print("REVERSE")

def write_left():
    print("LEFT")

def write_right():
    print("RIGHT")

def write_stop():
    print("STOP")
    ser.write(chr(137) + chr(0) + chr(0) + chr(0) + chr(0))

#frame
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

#buttons
#forward
FWD_Input = tk.Button(frame, 
                   text="Forward",
                   command=write_forward)
FWD_Input.pack(side=tk.TOP)

#reverse
RVS_Input = tk.Button(frame,
                   text="Reverse",
                   command=write_reverse)
RVS_Input.pack(side=tk.BOTTOM)

#left
TURN_Left = tk.Button(frame,
                   text="Left",
                   command=write_left)
TURN_Left.pack(side=tk.LEFT)

#right
TURN_Right = tk.Button(frame,
                   text="Right",
                   command=write_right)
TURN_Right.pack(side=tk.RIGHT)

#stop
stop = tk.Button(frame,
                   text="Stop",
                   command=write_stop)
stop.pack(side=tk.RIGHT)

#loop
root.mainloop()
