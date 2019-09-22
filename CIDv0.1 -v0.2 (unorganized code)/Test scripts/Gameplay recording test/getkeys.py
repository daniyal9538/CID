# Citation: Box Of Hats (https://github.com/Box-Of-Hats )
#Auhtor: Sentdex

#program is needed as a backend library to capture keystrokes
#python has an inbuilt library for this purpose (pyautogui), 
# but it is not suitable as it only records keystroke when there is a change in input
#this program continuosly monitors input from the key state, and generates an interupt when it asynchronously detects a key is pressed

import win32api as wapi
import time

keyList = ["\b"]
for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789,.'£$/\\":
    keyList.append(char)

def key_check():
    keys = []
    for key in keyList:
        if wapi.GetAsyncKeyState(ord(key)):
            keys.append(key)
    return keys
 
