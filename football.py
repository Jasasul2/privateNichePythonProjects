# Author : Ondřej Maceška 
# Date : 8.12.2019
# Description : Some random code used to automate a random football messenger game on mobile 
# Language : random 
# DEPRECATED 

import keyboard
import pyautogui
import time

class SoccerBot:

    def __init__(self):
        self.x = 0
        self.y = 650
        for i in range(3):
            pyautogui.click(280,self.y)
            time.sleep(0.5)
        for i in range(3):
            pyautogui.click(520,self.y)
            time.sleep(0.5)
        self.pixels = [280, 295, 310, 325, 340, 355, 370, 385, 400, 415, 430, 445, 460, 475, 490, 505, 520, 535]#pozice které checkuje
        while True:
            for i in self.pixels:
                self.pixelCheck(i, self.y) # checkne víc řádků
            for i in self.pixels:
                self.pixelCheck(i, self.y - 85)
                """
            for i in self.pixels:
                self.pixelCheck(i, self.y - 150)
            for i in self.pixels:
                self.pixelCheck(i, self.y - 225)
            for i in self.pixels:
                self.pixelCheck(i, self.y - 300)
                """
            if keyboard.is_pressed('q'):  # if key 'q' is pressed
                break  # finishing the loop
        print("whileBroken")

    def pixelCheck(self, xx, yy): #funkce která checkne jestli je na zadané pozici tmavý pixel a není okolo něj žlutý
        if pyautogui.pixelMatchesColor(xx,yy,(254, 255, 254), tolerance = 3) == False:
            #if (pyautogui.pixelMatchesColor(xx,yy,(65,65,65), tolerance = 25) == True) or (pyautogui.pixelMatchesColor(xx,yy,(25,25,25), tolerance = 25) == True) or (pyautogui.pixelMatchesColor(xx,yy,(85,85,85), tolerance = 15) == True) or (pyautogui.pixelMatchesColor(xx,yy,(245,245,245), tolerance = 12) == True):
            for i in range(-4, 4):
                if self.checkSmajlik(xx + i, yy + i) == False:
                    return
            self.x = xx
            pyautogui.click(self.x,yy)

    def checkSmajlik(self, xxx, yyy):
        if pyautogui.pixelMatchesColor(xxx,yyy,(243,174,68), tolerance = 25) == True:
            return False

pyautogui.PAUSE = 0.01
time.sleep(2.5)
soc = SoccerBot()
