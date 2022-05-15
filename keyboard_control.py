import streamlit as st
from pynput.keyboard import Key, Listener
from djitellopy import Tello
import keyboard


def app():
    me = Tello()
    me.connect()
    st.title('Keyboard Control for Drone!')
    result = st.button("Click to fly!")
    if result:
        # cmd = 'python /Users/farzanhashmi/PycharmProjects/DroneProject/KBControl.py'
        # p = subprocess.Popen(cmd, shell=True)
        # out, err = p.communicate()
        # print(err)
        # print(out)
        me.takeoff()
        me.move_up(40)

        def on_press(key):
            print('{0} pressed'.format(key))

        def on_release(key):
            if key == Key.up:
                me.move_up(40)
            if key == Key.down:
                me.move_down(40)
            if key == Key.w:
                me.move_down(70)
            if key == Key.s:
                me.move_back(70)
            if key == Key.left:
                me.rotate_counter_clockwise(90)
            if key == Key.right:
                me.rotate_clockwise(90)
            if key == Key.l:
                me.land()
                return False

        with Listener(
                on_press=on_press,
                on_release=on_release) as listener:
            listener.join()
