import pyautogui as pgui
import time

def gui():
    for i in range(10000):
        print(str(i) + '分経過')
        pgui.click(15, 15)
        time.sleep(100)
gui()