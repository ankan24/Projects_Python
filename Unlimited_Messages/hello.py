import pyautogui
import time
time.sleep(5)
count=0
while count<=1000:
    pyautogui.typewrite("hello world")
    pyautogui.press("enter")
    count=count+1
    