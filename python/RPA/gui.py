import pyautogui as pgui
import time

def gui():
    for _ in range(10000):
        pgui.click(10, 10)
        time.sleep(100)
gui()