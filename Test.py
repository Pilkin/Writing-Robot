

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
leftMotor = Motor(Port.D)
rightMotor = Motor(Port.C)

#rightMotor.run_time(450,10000)

#brick.display.clear()
brick.display.text("Hello", (60, 50))
time.sleep(2)
def left_Motor():
  print("Running left Motor")
  leftMotor.run_time(450,5000)
def right_Motor():
  print("Running right Motor")
  rightMotor.run_time(450,5000)
	

p1 = multiprocessing.Process(target=left_Motor)
p2 = multiprocessing.Process(target=right_Motor)

p1.start()
p2.start()

p1.join()
p2.join()

