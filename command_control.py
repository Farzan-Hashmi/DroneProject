import streamlit as st
import subprocess
from djitellopy import Tello
import cv2



class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def app():
    me = Tello()
    me.connect()
    print(me.get_battery())
    st.title('Command Control for Drone')
    st.write('This portion of the progam allows you to preprogam the flight path of the drone')
    st.write(
        'Your available commands are: takeoff, up_30c, down_30c, forward_30c, back_30c, turn_right_90, turn_left_90, land')
    commands = st.text_input("Commands", "")
    split = commands.split(", ")
    command_queue = Queue()

    for command in split:
        command_queue.enqueue(command)

    while command_queue.size() > 0:
        value = command_queue.dequeue()
        if value == 'takeoff':
            me.takeoff()
        elif value == 'up_30c':
            me.move_up(30)
        elif value == 'down_30c':
            me.move_down(70)
        elif value == 'forward_30c':
            me.move_forward(70)
        elif value == 'back_30c':
            me.move_back(70)
        elif value == 'turn_right_90':
            me.rotate_clockwise(90)
        elif value == 'turn_left_90':
            me.rotate_counter_clockwise(90)
        elif value == 'land':
            me.land()
        else:
            st.write('Invalid command: ' + value)
    me.end()
