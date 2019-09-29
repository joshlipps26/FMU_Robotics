###############################################################
##   Author:     Matt Harrington / Josh Lipps                ##
##   Written:    January 22nd, 2019                          ##
##                                                           ##
##  Identify pitch and tune to make the robot sing the song  ##
##                     TOTO by AFRICA                        ##
###############################################################

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
# DRIVE COMMANDS
drive = 137

try:
    ser = serial.Serial("COM3", baudrate=115200, timeout =1)
    print "Connected"
except serial.SerialException:
    print "Connection failure!"

#Open/Close Port
time.sleep(0.01)
ser.close()
time.sleep(0.01)
ser.open()

#Start Up
ser.write(chr(128))
time.sleep(0.1)
ser.write(chr(131))
time.sleep(0.1)

#MIDDLE C
# C# C# C# C# C# B E

# C# Note & Half
# C# Half
# 1/8th rest
# C# 8th
# 1/8th rest
# C# 8th
# C# 8th
# 8th rest
# B 8th
# 8th rest
# E half note

#C# = 61
#B  = 59
#E  = 64

#notes
# PART 1
C_SHARP = 61
B = 59
E = 64
# PART 2
F_SHARP = 66
G_SHARP = 68
A_SHARP = 70
B_HIGH = 71
# PART 3
F_SHARP_HIGH = 78 
E_HIGH = 76
C_SHARP_HIGH = 73
# PART 4
D_SHARP = 63

# REST
REST = 200

#timing
DOT_WHOLE = 96
WHOLE = 64
HALF = 32
EIGHTH = 8
QUARTER = 16

#NOTE 1 # OP CODE 140 # SONG NUM 0 #SONG LENGTH
ser.write(chr(140) + chr(0) + chr(9)
                + chr(C_SHARP) + chr(HALF)
                + chr(C_SHARP) + chr(EIGHTH)#C #1/2
                + chr(REST) + chr(EIGHTH) #REST 1/8
                + chr(C_SHARP) + chr(EIGHTH)#C 1/8
                + chr(REST) + chr(EIGHTH) #REST 1/8
                + chr(C_SHARP) + chr(EIGHTH)#C 1/8
                + chr(C_SHARP) + chr(QUARTER)#C 1/8
                + chr(B) + chr(QUARTER)#B 1/8
                + chr(E) + chr(WHOLE))#E 1/2


ser.write(chr(140) + chr(1) + chr(16)
              + chr(F_SHARP_HIGH) + chr(EIGHTH)
              + chr(E_HIGH) + chr(EIGHTH)
              + chr(C_SHARP_HIGH) + chr(EIGHTH)
              + chr(E_HIGH) + chr(EIGHTH)
              + chr(F_SHARP_HIGH) + chr(EIGHTH)
              + chr(E_HIGH) + chr(EIGHTH)
              + chr(C_SHARP_HIGH) + chr(EIGHTH)
              + chr(E_HIGH) + chr(EIGHTH)
              + chr(F_SHARP_HIGH) + chr(EIGHTH)
              + chr(E_HIGH) + chr(EIGHTH)
              + chr(C_SHARP_HIGH) + chr(EIGHTH)
              + chr(B_HIGH) + chr(EIGHTH)
              + chr(C_SHARP_HIGH) + chr(EIGHTH)
              + chr(B_HIGH) + chr(EIGHTH)
              + chr(C_SHARP_HIGH) + chr(EIGHTH)
              + chr(F_SHARP_HIGH) + chr(EIGHTH))


ser.write(chr(140) + chr(2) + chr(9)
             + chr(F_SHARP) + chr(EIGHTH)
             + chr(F_SHARP) + chr(EIGHTH)
             + chr(F_SHARP) + chr(EIGHTH)
             + chr(F_SHARP) + chr(HALF)
             + chr(F_SHARP) + chr(EIGHTH)
             + chr(F_SHARP) + chr(HALF)
             + chr(G_SHARP) + chr(QUARTER)
             + chr(A_SHARP) + chr(EIGHTH)
             + chr(B_HIGH) + chr(WHOLE))


ser.write(chr(140) + chr(3) + chr(15)
            + chr(D_SHARP) + chr(EIGHTH)
            + chr(D_SHARP) + chr(QUARTER)
            + chr(E) + chr(QUARTER)
            + chr(F_SHARP) + chr(QUARTER)
            + chr(F_SHARP) + chr(QUARTER)
            + chr(E) + chr(EIGHTH)
            + chr(E) + chr(EIGHTH)
            + chr(D_SHARP) + chr(QUARTER)
            + chr(C_SHARP) + chr(WHOLE)
            + chr(C_SHARP) + chr(QUARTER)
            + chr(B) + chr(QUARTER)
            + chr(D_SHARP) + chr(WHOLE)
            + chr(C_SHARP) + chr(EIGHTH)
            + chr(B) + chr(QUARTER)
            + chr(C_SHARP) + chr(WHOLE)) 


#SONG 1 (FIRST HALF)

ser.write(chr(141) + chr(0)) # PART 1
time.sleep(2.8)
ser.write(chr(141) + chr(1)) # PART 2
time.sleep(2.4)
ser.write(chr(141) + chr(0)) # PART 1
time.sleep(2.8)
ser.write(chr(141) + chr(1)) # PART 2
time.sleep(2.4)
ser.write(chr(141) + chr(2)) # PART 3
time.sleep(3)
ser.write(chr(141) + chr(3)) # PART 4


#SONG 2 (SECOND HALF)


