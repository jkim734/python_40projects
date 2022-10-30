# 일정시간마다 동작하는 코드 만들기
import pyautogui
import pyperclip
import time
import threading
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def send_message():
    threading.Timer(10, send_message).start()
    picPostion = pyautogui.locateOnScreen('pic1.png')
    print(picPostion)

    if picPostion is None:
        picPostion = pyautogui.locateOnScreen('pic2.png')
    print(picPostion)

    if picPostion is None:
        picPostion = pyautogui.locateOnScreen('pic3.png')
    print(picPostion)

    clickPosition = pyautogui.locateCenterOnScreen(picPostion)
    pyautogui.doubleClick(clickPosition)

    pyperclip.copy("이 메세지는 자동으로 보내는 메세지입니다.~~")
    pyautogui.hotkey("ctrl", "v")
    time.sleep(1.0)

    pyautogui.write(["enter"])
    time.sleep(1.0)

    pyautogui.write(["escape"])
    time.sleep(1.0)

send_message()