####################################################
##   Author:     Matt Harrington / Josh Lipps
##   Written:    January 22nd, 2019
##   Updated: January 28th, 2019
##   Library of commands and methods to send the iCreate 2 Robot
##
####################################################


import struct
import serial
import time

class Robot:

        # commands definitions
        startCMD                =  128
        safeCMD                 =  131
        fullCMD                 =  132
        sensorsCMD              =  142
        resetCMD                 =  7
        stopCMD                    =  173
        buttonsCMD                 =  165
        driveDirectCMD             =  145
        driveCMD                   =  137
        ledsCMD                    =  139

        # packet IDs definitions
        wall                    =  8
        bumpsAndWheels          =  7
        cliffLeft               =  9
        cliffFrontLeft          =  10
        cliffFrontRight         =  11
        cliffRight              =  12
        virtualWall             =  13
        buttons                 =  18
        distance                =  19
        angle                   =  20
        chargingState           =  21
        voltage                 =  22
        temperature             =  24
        batteryCharge           =  25
        wallSignal              =  27
        cliffLeftSignal         =  28
        cliffFrontLeftSignal    =  29
        cliffFrontRightSignal   =  30
        cliffRightSignal        =  31

        # connection made
        def __init__(self, port):
                try:
                        self.serial_connection = serial.Serial(port, baudrate=115200,timeout =1)
                        print "Connected!"
                except serial.SerialException:
                        print "Connection failure!"
                time.sleep(1)
                self.serial_connection.close()
                time.sleep(1)
                self.serial_connection.open()

        # sends commands to the robot
        def sendCommand(self, input):
                self.serial_connection.write(input)
        # reads information sent to the computer from the robot/sensors
        def read(self, howManyBytes):
                bytes = self.serial_connection.read()
                #come back here
                if (howManyBytes == 1):
                        return bytes
                return (bytes << 8**(howManyBytes - 1)) + read(howManyBytes - 1)

                time.sleep(1)

        # this starts the robot and puts it in passive mode
        def start(self):
                self.sendCommand(chr(self.startCMD))
                time.sleep(1)

        # this stops the robot
        def stop(self):
                self.sendCommand(chr(stop))
                SystemExit()

        # this does a reset of the robot
        def reset(self):
                self.sendCommand(chr(self.resetCMD))
                time.sleep(1)

        # this puts the robot into safe mode
        def safe(self):
                self.sendCommand(chr(self.safeCMD))
                time.sleep(1)

        # this allows the robot to seek its dock
        def seekDock(self):
                self.sendCommand(chr(self.seekDockCMD))
                time.sleep(1)

        #this sends in the bits to allow the robot to drive using the normal command
        def drive(self, velocityHighByte, velocityLowByte, radiusHighByte, radiushLowByte):
                self.sendCommand(chr(self.driveCMD) + chr(velocityHighByte) + chr(velocityLowByte) + chr(radiusHighByte) + chr(radiushLowByte))
                time.sleep(1)

        # this allows the robot to drive with complete control of the wheels
        def driveDirect(self, rightWheelHighByte, rightWheelLowByte, leftWheelHighByte, leftWheelLowByte):
                self.sendCommand(chr(self.driveDirectCMD), + chr(rightWheelHighByte) + chr(rightWheelLowByte) + chr(leftWheelHighByte) + chr(leftWheelLowByte))
                time.sleep(1)

        # this allows control over the LEDS
        def leds(self, ledBits, powerColor, powerIntensity):
                self.sendCommand(chr(self.ledsCMD) + chr(ledBits) + chr(powerColor) + chr(powerIntensity))
                time.sleep(1)

        # this allows control over the display on the robot with ACSII keys
        def digitLEDsASCII(self, digit3, digit2, digit1, digit0):
                self.sendCommand(chr(self.digitLEDsASCIICMD) + digit3 + digit2 + digit1 + digit0)
                time.sleep(1)
