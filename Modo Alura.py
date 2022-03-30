import pyautogui


pyautogui.alert("Clique em OK para iniciar o modo Alura!")
pyautogui.PAUSE = 0.2
pyautogui.press('winleft')
pyautogui.write('cmd')
pyautogui.press('enter')
pyautogui.write('cd .\OneDrive\Desktop\ADS\Automacao Python\Alura')
pyautogui.press('enter')
pyautogui.write('start StudioCode.lnk')
pyautogui.press('enter')
pyautogui.press('winleft')
pyautogui.write('cmd')
pyautogui.press('enter')
pyautogui.write('cd .\OneDrive\Desktop\ADS\Automacao Python\Alura')
pyautogui.press('enter')
pyautogui.write('start Cursos.html')
pyautogui.press('enter')
pyautogui.write('exit')
pyautogui.press('enter')