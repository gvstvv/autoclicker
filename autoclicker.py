import pyautogui
import time

# automação mouse
pyautogui.keyDown('alt')
pyautogui.press('tab')
pyautogui.keyUp('alt')

# contador de cliques (inicia em 0)
c = 0

while True:
    autoclick_pos = pyautogui.click(x=190, y=345)
    c += 1 # contador de cliques +1 ad infinitum
    if c == 999: # valor em numero de cliques
        pausa = time.sleep(1)
        pyautogui.click(x=1081, y=684)

        pyautogui.click(x=1081, y=593)

        pyautogui.click(x=1081, y=502)

        pyautogui.click(x=1081, y=411)

        pyautogui.click(x=1081, y=320)
        c = 0
