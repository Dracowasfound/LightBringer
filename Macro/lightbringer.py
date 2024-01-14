import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

TOGGLE_KEY = KeyCode(char="``")
clicking = False
mouse = Controller()

def clicker():
    while True:
        if clicking:
            mouse.click(Button.right, 1)
        time.sleep(0.0001)

def toggle_event(key):
    if key == TOGGLE_KEY:
        global clicking
        clicking = not clicking

click_thread = threading.Thread(target=clicker)
click_thread.start()

with Listener(on_press=toggle_event) as listener:
    listener.join()

inp = int(input())
while inp != 1 or inp != 2:
    print("1 is for left click, 2 is for right click")
    inp = int(input())
if inp == 1:
    print("You have chosen leftclick!")
if inp == 2:
    print("You have chosen right click!")
    quit()

if chosen_input == 1:
    mouse.click = Button.right()
    if input == 2:
        mouse.click = Button.left()

