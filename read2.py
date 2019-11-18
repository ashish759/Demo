import pyautogui
screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()
pyautogui.moveTo(100, 150)
pyautogui.click()
pyautogui.moveRel(None, 10) # move mouse 10 pixels down
pyautogui.doubleClick()
pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)
pyautogui.typewrite('Hello world! dfsdfsdgsdfghfjhfgjhfgjfgghjgjgjgjgjghjghjg', interval=0.25) 
pyautogui.FAILSAFE = True


