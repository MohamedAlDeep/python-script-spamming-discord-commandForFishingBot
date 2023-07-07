import pyautogui
import time
sl = time.sleep

# Variables for mouse positions

# This variable holds the number of times the fishing 
# should be done untill selling
numberOftimes = 5

# The position x,y of the message input box
messageInputBoxPos = [1395, 993]

# The position of the fish button
fishAgainInputPos = [1422, 918]

# The position of the sell button 
SellInputPos = [1498, 922]

# -------------------------------------
sl(5)
def loop():
    while(True):
        sl(2)
        breaksForSelling = 2
        for i in range(breaksForSelling):
            for n in range(numberOftimes):
                pyautogui.moveTo(fishAgainInputPos[0], fishAgainInputPos[1])
                pyautogui.click()
                sl(5)
            # Fourth position the position of the sell button x(1498), y(922)
            pyautogui.moveTo(SellInputPos[0], SellInputPos[1])
            pyautogui.click()


# Initial positioning
sl(1)
pyautogui.moveTo(messageInputBoxPos[0], messageInputBoxPos[1])
sl(1)
pyautogui.click()
sl(2)
pyautogui.write('/fish')
sl(2)
pyautogui.press('enter')
sl(1)
pyautogui.press('enter')
sl(5)
loop()


# ---------------------------------------------
# TOOL TO CALCULATE THE X,Y coords of the mouse
# CHANGE THE COORDS VARIABLES ACCORDING TO POSITION OF EACH INPUT
# while(True):
#     x,y = pyautogui.position()

#     print(x,y)
