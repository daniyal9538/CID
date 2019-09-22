import time
import socket
import random
import numpy as np
import sys
import cv2

from getkeys import key_check
from directkeys import PressKey,ReleaseKey, W, A, S, D
import time


w = [1,0,0,0,0,0,0,0,0]
s = [0,1,0,0,0,0,0,0,0]
a = [0,0,1,0,0,0,0,0,0]
d = [0,0,0,1,0,0,0,0,0]
wa = [0,0,0,0,1,0,0,0,0]
wd = [0,0,0,0,0,1,0,0,0]
sa = [0,0,0,0,0,0,1,0,0]
sd = [0,0,0,0,0,0,0,1,0]
nk = [0,0,0,0,0,0,0,0,1]

def straight():
    PressKey(W)
    ReleaseKey(A)
    ReleaseKey(D)
    ReleaseKey(S)

def left():
    ReleaseKey(W)
    PressKey(A)
    ReleaseKey(S)
    ReleaseKey(D)
    #ReleaseKey(S)

def right():
    ReleaseKey(W)
    PressKey(D)
    ReleaseKey(A)
    ReleaseKey(S)
    
def reverse():
    PressKey(S)
    ReleaseKey(A)
    ReleaseKey(W)
    ReleaseKey(D)


def forward_left():
    PressKey(W)
    PressKey(A)
    ReleaseKey(D)
    ReleaseKey(S)
    
    
def forward_right():
    PressKey(W)
    PressKey(D)
    ReleaseKey(A)
    ReleaseKey(S)

    
def reverse_left():
    PressKey(S)
    PressKey(A)
    ReleaseKey(W)
    ReleaseKey(D)

    
def reverse_right():
    PressKey(S)
    PressKey(D)
    ReleaseKey(W)
    ReleaseKey(A)

def no_keys():

    ReleaseKey(W)
    ReleaseKey(A)
    ReleaseKey(S)
    ReleaseKey(D)

fileName = "demo-data-3.npy"

test = np.load(fileName, allow_pickle=True)

for i in range(len(test)):
    choice_picked=""
    control = test[i][1]

    control = np.argmax(control)
    if control == 0:
        straight()
        choice_picked = 'straight'
                    
    elif control == 1:
        reverse()
        choice_picked = 'reverse'
                    
    elif control == 2:
        left()
        choice_picked = 'left'

    elif control == 3:
        right()
        choice_picked = 'right'

    elif control == 4:
        forward_left()
        choice_picked = 'forward+left'

    elif control == 5:
        forward_right()
        choice_picked = 'forward+right'
   
    elif control == 6:
        reverse_left()
        choice_picked = 'reverse+left'
            
    elif control == 7:
        reverse_right()
        choice_picked = 'reverse+right'
           
    elif control == 8:
        no_keys()
        choice_picked = 'nokeys'
    time.sleep(0.5)
    print(choice_picked)