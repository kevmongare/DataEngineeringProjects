import os
import time
import pyautogui

# Open app
os.system("open -a terminal")
time.sleep(3)  # Wait for app to launch

# Example: press Command+T to open new tab
# pyautogui.hotkey('command', 't')
pyautogui.write('mkdir Hacked && cd Hacked', interval=0.25)
pyautogui.press('enter') 
pyautogui.write('vi save.py')
pyautogui.write('i')
pyautogui.write("print('Hi the work has been executed successfully')", interval=0.25)
pyautogui.press('esc')
pyautogui.write(':wq!')
pyautogui.press('enter') 
pyautogui.write('python3 save.py')