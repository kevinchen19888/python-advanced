import pyautogui,time


def move_house():
    while True:
        time.sleep(1)

        pyautogui.moveRel(0, -100, duration=1)

        time.sleep(1)

        pyautogui.moveRel(0, 100, duration=1)

        time.sleep(1)


move_house()
