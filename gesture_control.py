import time

import streamlit as st
import subprocess
from djitellopy import Tello
import cv2
from cvzone.HandTrackingModule import HandDetector


def app():
    st.title('Gesture Control for Drone!')
    result = st.button("Click to fly!")
    if result:
        # cmd = 'python /Users/farzanhashmi/PycharmProjects/DroneProject/testcv.py'
        # p = subprocess.Popen(cmd, shell=True)
        # out, err = p.communicate()
        # print(err)
        # print(out)
        FRAME_WINDOW = st.image([])
        me = Tello()

        me.connect()

        # specifications for video streaming
        width = 320;
        height = 240;
        startCounter = 0;
        detector = HandDetector(maxHands=1, detectionCon=0.8)

        print(me.get_battery())

        me.streamon()

        me.takeoff()
        me.move_up(40)
        while True:
            frame_read = me.get_frame_read()
            time.sleep(1)
            myFrame = frame_read.frame
            FRAME_WINDOW.image(myFrame)
            hand = detector.findHands(myFrame, draw=False)
            if hand:
                lmlist = hand[0]
                if lmlist:
                    fingerup = detector.fingersUp(lmlist)
                    if fingerup == [0, 1, 0, 0, 0]:
                        print("forward")
                        me.move_forward(30)
                    if fingerup == [0, 1, 1, 0, 0]:
                        print("cc")
                        me.rotate_counter_clockwise(30)
                    if fingerup == [0, 1, 1, 1, 0]:
                        print("back")
                        me.move_back(30)
                    if fingerup == [0, 1, 1, 1, 1]:
                        print("up")
                        me.move_up(30)
                    if fingerup == [1, 1, 1, 1, 1]:
                        print("down")
                        me.move_down(30)


            if cv2.waitKey(1) & 0xFF == ord('q'):
                me.land()
                me.end()
                break

