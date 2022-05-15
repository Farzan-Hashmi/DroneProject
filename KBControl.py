import sys

import keyPressModule as kp
from djitellopy import Tello

kp.init()
me = Tello()
me.connect()
print(me.get_battery())


def getKeyBoardInput():
    if kp.getKey("LEFT"):
        me.rotate_counter_clockwise(50)
    if kp.getKey("RIGHT"):
        me.rotate_clockwise(50)
    if kp.getKey("UP"):
        me.move_up(50)
    if kp.getKey("DOWN"):
        me.move_down(50)
    if kp.getKey("w"):
        me.move_forward(80)
    if kp.getKey("s"):
        me.move_back(80)
    if kp.getKey("f"):
        me.flip_right()
    if kp.getKey("l"):
        me.land()
        sys.exit()



me.takeoff()
me.move_up(40)

while True:
    getKeyBoardInput()
