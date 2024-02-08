import pyautogui as pag
import time as t
import threading as th


def searchAndClick(image, confidanceValue=0.8, isLeftClick=True, countMax = 30, sleepTime = 1):
    x = 0
    count = 0
    while count < countMax:
        try:
            x, y = pag.locateCenterOnScreen(image, confidence=confidanceValue)
        except TypeError:
            x = 0
            continue
        t.sleep(sleepTime)
        if x != 0:
            pag.moveTo(x, y)
            pag.leftClick() if isLeftClick else pag.rightClick()
            break
        else:
            count += 1 


def threadMaker(func):
        thread = th.Thread(target=func, daemon=True)
        thread.start()
