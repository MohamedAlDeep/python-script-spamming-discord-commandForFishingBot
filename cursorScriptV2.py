# You need to run: py -m pip install pyautogui
import pyautogui as pag

# This does not require installation
import time

sl = time.sleep

# Code variables: Substitute the values that work for you
# To know the values that work for you use the tool that prints the position of your mouse Live

# Number of fishing untill selling: SUBSTITUTE VALUES DEPENDING ON YOUR PREFERENCE
repeatTillSell = 3

# Number of selling untill the code stops: SUBSTITUTE VALUES DEPENDING ON YOUR PREFERENCE
numberOfSells = 3

# Discord message input box position: SUBSTITUTE VALUES DEPENDING ON YOUR PREFERENCE
msgBoxPos  = [510, 996]

# Discord fishing bot ==> Fish again button position: SUBSTITUTE VALUES DEPENDING ON YOUR PREFERENCE
fishBtnPos = [922, 922]

# Discord fishing bot ==> Sell button position : SUBSTITUTE VALUES DEPENDING ON YOUR PREFERENCE
sellBtnPos = [537, 924]

# init: This code automatically switches to your next window(Windows Operating System)

def main():
    pag.keyDown('alt')
    pag.press('tab')
    pag.press("enter")
    pag.keyUp('alt')

    for reapeatWholeCodeTimes in range(numberOfSells):
        for nos in range(repeatTillSell):
            pag.moveTo(msgBoxPos[0], msgBoxPos[1])
            pag.click()
            sl(1)
            pag.write('/fish')

            # If your fish command is not on top use this commented code below and comment the code number two
            # untill your fish command stays on top of suggested commands in discord
            # --- Code number 1
            # pag.press('keydown')
            # sl(1) # Network latency delay
            # pag.hotkey('enter', 'enter')
            # --- Code || Dont use the code above if your fish command is not on the top of your suggestions

            # --- Code number 2
            pag.hotkey('enter', 'enter')
            sl(1)
            pag.moveTo(fishBtnPos[0], fishBtnPos[1])
            sl(1)
            pag.click()
            pag.click()
            sl(5)
            # --- Code number 2

        # Selling code
        sl(1)
        pag.moveTo(sellBtnPos[0], sellBtnPos[1])
        sl(1)

# Comment the function call if you want to use the tool
main()

# Tool that prints positions of your mouse on the screen
# Uncomment the code below to use the tool
# Guide of using the tool

# --- Guide
# First: you need to comment the main function call
# Second: You need to uncomment the code in code section bellow
# Third: Run the code then go to the position you want and switch your window using
# the Windows Operating System shortcut: alt+tab
# Fourth: Windows Operating System shortcut: ctrl+c in the terminal and substitute the x, y
# values in the [x,y] arrays variables
# --- Guide

# --- Code
# while(True):
#         pos = pag.position()
#         print('x', pos[0], '- y', pos[1])
# --- Code
