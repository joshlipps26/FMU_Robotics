###############################################################
##   Author:     Matt Harrington / Josh Lipps                ##
##   Written:    April 3rd, 2019                             ##
##                                                           ##
##  P-Controller : Navigate Obstacles using only P-Control   ##
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

#Boot Robot
try:
    ser = serial.Serial("COM6", baudrate=115200, timeout =1)
    print "Connected"
except serial.SerialException:
    print "Connection failure!"

wallFound = False
setPoint = 60
gain = .92

#open/close ports
time.sleep(0.01)
ser.close()
time.sleep(0.01)
ser.open()

ser.write(chr(128))
time.sleep(0.01)
ser.write(chr(131))
time.sleep(0.01)

#move forward
ser.write(chr(145) + chr(0) + chr(50) + chr(0) + chr(50))

while(True):
    #read bumper
    ser.write(chr(142) + chr(7))
    time.sleep(0.1)

    #byte = ser.read()
    buttonState = ser.read()
    # just get the binary and do the and oeprator
    byte = struct.unpack('B', buttonState)[0]
    binary = '{0:08b}'.format(byte)

    #check bumpers
    if((int(binary) & 3) > 0):

        #stop
        ser.write(chr(145) + chr(0) + chr(0) + chr(0) + chr(0))
        time.sleep(0.1)

        #reverse
        ser.write(chr(145) + chr(255) + chr(1) + chr(255) + chr(1))
        time.sleep(.3)
     
        #stop
        ser.write(chr(145) + chr(0) + chr(0) + chr(0) + chr(0))
        time.sleep(0.1)

        #spin
        ser.write(chr(137) + chr(255) + chr(0) + chr(0) + chr(1))
        time.sleep(1.2)

        while(wallFound == False):
            #detect wall
            ser.write(chr(142) + chr(27))
            time.sleep(0.01)
            
            buttonState = ser.read()
            buttonState2 = ser.read()
            byte = struct.unpack('B', buttonState)[0]
            binary = '{0:08b}'.format(byte)
            byte2 = struct.unpack('B', buttonState2)[0]
            binary2 = '{0:08b}'.format(byte2)

            ser.write(chr(137) + chr(255) + chr(0) + chr(0) + chr(1))
            time.sleep(0.1)
            
            wallDistance = byte2 + (byte << 8)    
            if(int(wallDistance) > 0):
                wallFound = True
                ser.write(chr(137) + chr(0) + chr(0) + chr(0) + chr(0))
                print("WALL FOUND")


        #Read Wall Distance
        while(True):

            rightWheel = 100
            leftWheel = 100
            
            ser.write(chr(142) + chr(27))
            time.sleep(0.01)
            
            buttonState = ser.read()
            buttonState2 = ser.read()
            byte = struct.unpack('B', buttonState)[0]
            binary = '{0:08b}'.format(byte)
            byte2 = struct.unpack('B', buttonState2)[0]
            binary2 = '{0:08b}'.format(byte2)
            wallDistance = byte2 + (byte << 8)

            error = setPoint - wallDistance
            p = gain * error

            rightWheel -= p
            leftWheel += p

            highByteRight = 0
            highByteLeft = 0
            
            if(rightWheel > 255):
                rightWheel = rightWheel - 255
                highByteRight = 1
            elif(rightWheel < 1):
                rightWheel = 1
                highByteRight = 0
            if(leftWheel > 255):
                leftWheel = 255
                highByteLeft = highByteLeft - 255
            elif(leftWheel < 1):
                leftWheel = 1
                highByteLeft = 0

            ser.write(chr(145) + chr(highByteRight) + chr(int(rightWheel)) + chr(highByteLeft) + chr(int(leftWheel)))

            #read bumper
            ser.write(chr(142) + chr(7))
            time.sleep(0.1)

            #byte = ser.read()
            buttonState = ser.read()
            #just get the binary and do the and oeprator
            byte = struct.unpack('B', buttonState)[0]
            binary = '{0:08b}'.format(byte)

    #check bumpers
            if((int(binary) & 3) > 0):

                wallFound = False
                #stop
                ser.write(chr(145) + chr(0) + chr(0) + chr(0) + chr(0))
                time.sleep(0.1)

                #reverse
                ser.write(chr(145) + chr(255) + chr(1) + chr(255) + chr(1))
                time.sleep(.3)

                #stop
                ser.write(chr(145) + chr(0) + chr(0) + chr(0) + chr(0))
                time.sleep(0.1)

                #spin
                ser.write(chr(137) + chr(255) + chr(0) + chr(0) + chr(1))
                time.sleep(1.2)

                while(wallFound == False):
                    #detect wall
                    ser.write(chr(142) + chr(27))
                    time.sleep(0.01)
            
                    buttonState = ser.read()
                    buttonState2 = ser.read()
                    byte = struct.unpack('B', buttonState)[0]
                    binary = '{0:08b}'.format(byte)
                    byte2 = struct.unpack('B', buttonState2)[0]
                    binary2 = '{0:08b}'.format(byte2)

                    ser.write(chr(137) + chr(255) + chr(0) + chr(0) + chr(1))
                    time.sleep(0.1)
            
                    wallDistance = byte2 + (byte << 8)    
                    if(int(wallDistance) > 0):
                        wallFound = True
                        ser.write(chr(137) + chr(0) + chr(0) + chr(0) + chr(0))
                        print("WALL FOUND")
