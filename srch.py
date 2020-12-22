from pynput.keyboard import Key, Controller
import main
import time
import pyautogui 
keyboard = Controller()
def srch(query):
    keyboard.press(Key.cmd)
    keyboard.release(Key.cmd)

    time.sleep(1)


    for char in query:
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.11)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(3)