from PIL import Image
import time
import numpy as np
import pyautogui

screenWidth, screenHeight = pyautogui.size()
screenWidth, screenHeight
 
time.sleep(5)
pyautogui.press('space')

while True:
   img = pyautogui.screenshot(region=(500, 247, 90, 22))
   gray = img.convert("L")
   bw = gray.point(lambda p: 0 if p < 100 else 255)
   arr = np.array(bw)
   white_pixels = np.sum(arr != 0)
  
   if white_pixels > 250:
      pyautogui.press('space')