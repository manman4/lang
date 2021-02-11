import pyautogui as pgui
import time
import sys

def gui():
    for i in range(10000):
        sys.stdout.write("\r{}分経過".format(i))
        sys.stdout.flush()

        pgui.click(15, 15)
        time.sleep(100)
gui()