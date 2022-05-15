from djitellopy import Tello
import streamlit as st
from multiapp import MultiApp

import command_control
import gesture_control
import keyboard_control

app = MultiApp()
# me = Tello()
# me.connect()
# print(me.get_battery())



st.markdown("""
# Drone Program

### This program allows the pilot to fly their drone using their keyboard, gestures, or inputs

""")

st.write("")

app.add_app("Gesture Control", gesture_control.app)
app.add_app("Keyboard Control", keyboard_control.app)
app.add_app("Command Control", command_control.app)

app.run()

# me = tello.Tello()
# me.connect()
# print(me.get_battery())
#
# me.streamon()
#
#
# st.title("Webcam with drone")
#
# st.write("First step! Click the button to take off the drone")
#
# result = st.button('Click here to take off!')
# st.text("")
# if result:
#     st.write("Taking off!")
#     me.takeoff()
#     me.move_up(40)
#
# run = st.checkbox('Run')
#
# while True:
#     img = me.get_frame_read().frame
#
#
# me.takeoff()
# sleep(1.5)
# me.rotate_counter_clockwise(180)
# sleep(1.5)
# me.rotate_clockwise(180)
# sleep(1)
# me.land()
#
