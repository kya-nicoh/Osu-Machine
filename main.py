from pyautogui import *
import pyautogui
import time
import keyboard
import numpy as np
import random
import win32api, win32con


# First key D:  X:  340 Y:  916
# Second Key F: X:  406 Y:  916
# Third Key J:  X:  474 Y:  916
# Fourth Key K: X:  537 Y:  916
# RGB: (252, 167, 206)
# RGB: (237, 233, 233)
# KeyDown of R: 235, 260 then
# KeyUp R: 0 - 85

def press():
    if pyautogui.pixel(340,880)[0] == 252:
        pyautogui.keyDown('d')
        if pyautogui.pixel (340, 916) [0] == 0:
            time.sleep(np.random.uniform(0.5, 0.7))
            pyautogui.keyUp('d')



time.sleep(2)

while keyboard.is_pressed('q') == False:
    press()
