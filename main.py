#!/usr/bin/env pybricks-micropython

import time 
import multiprocessing

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase


# Initialize a motor(by default this means clockwise, without any gears).
left_Motor = Motor(Port.D)
right_Motor = Motor(Port.C)
pen_Motor = Motor(Port.B)

#rightMotor.run_time(450,10000)

def dualrun_time(lMotor, rMotor, time_s):
    lMotor.run(400)
    rMotor.run(400)
    time.sleep(time_s)
    lMotor.stop()
    rMotor.stop()

def dualrun_angle(lMotor, rMotor, lAngle, rAngle):
    startLAngle = lMotor.angle()
    startRAngle = rMotor.angle() 
    lMotor.run_angle(400, lAngle, Stop.BRAKE, False)
    rMotor.run_angle(400, rAngle, Stop.BRAKE, False)
    sleepTime = lAngle/100
    time.sleep(sleepTime)
    endLAngle = lMotor.angle()
    endRAngle = rMotor.angle()
    leftMotorTurned = endLAngle - startLAngle
    rightMotorTurned = endRAngle - startLAngle
    print ("Left motor turned " + str(leftMotorTurned) + " degrees")
    print ("Right motor turned " + str(rightMotorTurned) + " degrees")
    
def drive_forward(lMotor, rMotor, time_s):
    print("Driving forwards...")
    lMotor = Motor(Port.D, Direction.CLOCKWISE)
    rMotor = Motor(Port.C, Direction.CLOCKWISE)
    dualrun_time(lMotor, rMotor, time_s)
   
def drive_backward(lMotor, rMotor, time_s):
    print("Driving backwards...")
    lMotor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
    rMotor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
    dualrun_time(lMotor, rMotor, time_s)

def turn(lMotor, rMotor, angle, direction):
    if direction == "clockwise":
      lMotor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
      rMotor = Motor(Port.C, Direction.CLOCKWISE)
    elif direction == "counterclockwise":
      lMotor = Motor(Port.D, Direction.CLOCKWISE)
      rMotor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
    else:
      print ("Direction invalid")
      return()
    if type(angle) == int:
      print (type(angle))
    else:
      print ("Angle not of int type")
      return()
    formattedAngle = angle * 2
    dualrun_angle(lMotor, rMotor, formattedAngle, formattedAngle)

def penDown(pMotor):
    pMotor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
    pMotor.run(20)
    time.sleep(2)
    print ("Pen engaged")

def penReset(pMotor):
    pMotor = Motor(Port.B, Direction.CLOCKWISE)
    pMotor.run(400)
    time.sleep(2)
    print ("Pen in rest position")



penReset(pen_Motor)
penDown(pen_Motor)
drive_forward(left_Motor,right_Motor, 1)
penReset(pen_Motor)
turn(left_Motor,right_Motor, 90, "clockwise")
penDown(pen_Motor)
drive_forward(left_Motor,right_Motor, 1)
penReset(pen_Motor)
turn(left_Motor,right_Motor, 90, "clockwise")
penDown(pen_Motor)
drive_forward(left_Motor,right_Motor, 1)
penReset(pen_Motor)
turn(left_Motor,right_Motor, 90, "clockwise")
penDown(pen_Motor)
drive_forward(left_Motor,right_Motor, 1)
penReset(pen_Motor)
#pen_Motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
#pen_Motor.run_angle(100, 180, Stop.BRAKE, False)

#drive_backward(left_Motor, right_Motor, 4)














#drive_forward(left_Motor, right_Motor, 1)
#drive_backward(left_Motor, right_Motor, 1)
#turn(left_Motor, right_Motor, 10, "clockwise")

#

#right_Motor.run_angle(400, 360)
#left_Motor.run_angle(400, 360)
#print (right_Motor.angle())


#left_Motor.run_target(400, 180, Stop.BRAKE, True)


#375 == 180degrees
#750 = 360degrees

#180 degrees = 375
#1 degrees = 2.08

#penDown()
#turn(left_Motor, right_Motor, 360, "counterclockwise")
#time.sleep(3)
#penReset()
#time.sleep(3)

#pen_Motor.stop()

#pen_Motor.run_angle(400, 180, Stop.BRAKE, False)

#drive_forward(left_Motor, right_Motor, 1)
