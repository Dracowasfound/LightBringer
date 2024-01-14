import time
import threading

import mouse
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode


inp = input("Choose 1 or 2, 1 is left click; 2 is for right click. ")
if inp == "1":
    print("You picked left click")
elif inp == "2":
    print("You picked right click")
else:
    print("You must choose between 1 or 2")

    if input == "1":
        mouse.click = Button.right()
        if inp == "2":
            mouse.click = Button.left()

TOGGLE_KEY = KeyCode(char="`")
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


