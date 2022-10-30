#사진에서 좌표 추출하는 코드 만들기
from traceback import print_tb
import pyautogui
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

picPostion = pyautogui.locateOnScreen('pic1.png')
print(picPostion)

if picPostion is None:
    picPostion = pyautogui.locateOnScreen('pic2.png')
    print(picPostion)

if picPostion is None:
    picPostion = pyautogui.locateOnScreen('pic3.png')
    print(picPostion)

    