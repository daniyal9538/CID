import time
import socket
import random
import numpy as np
import sys
import cv2
from screen_capture import grab_screen
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

t_time = 0.25

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

input_width = 1280
input_height = 720
# while(True):
#     x = grab_screen(region=(0,40,input_width,input_height))
    
#     x=cv2.resize(x, (160, 120))
#     x=cv2.cvtColor(x, cv2.COLOR_BGR2GRAY)
#     print(x.shape)
#     cv2.imshow('w', x)
#     if cv2.waitKey(25) & 0xFF == ord('q'):
#                 cv2.destroyAllWindows()
#                 break

while(True):
    now = time.time()
    x = grab_screen(region=(0,40,input_width,input_height))
    
    x=cv2.resize(x, (340, 191))
    x=cv2.cvtColor(x, cv2.COLOR_BGR2GRAY)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(1.0)
    
    # cv2.imshow('w', cv2.resize(x, (480, 270)))
    # if cv2.waitKey(0) & 0xFF == ord('q'):
    #     cv2.destroyAllWindows()
        
    arrMessage = x
    
    #print(arrMessage.shape, len(arrMessage), type(arrMessage), arrMessage.dtype.name)
    arrMessage = arrMessage.tobytes()
    #print(sys.getsizeof(arrMessage))
    addr = ("10.144.93.112", 12000)
    choice_picked = ''
    start = time.time()
    client_socket.sendto(arrMessage, addr)
    try:
        data, server = client_socket.recvfrom(64000)
        mode_choice = np.argmax(np.frombuffer(data, dtype = np.uint8))
        if mode_choice == 0:
                straight()
                choice_picked = 'straight'
                
        elif mode_choice == 1:
                reverse()
                choice_picked = 'reverse'
                
        elif mode_choice == 2:
                left()
                choice_picked = 'left'
        elif mode_choice == 3:
                right()
                choice_picked = 'right'
        elif mode_choice == 4:
                forward_left()
                choice_picked = 'forward+left'
        elif mode_choice == 5:
                forward_right()
                choice_picked = 'forward+right'
        elif mode_choice == 6:
                reverse_left()
                choice_picked = 'reverse+left'
        elif mode_choice == 7:
                reverse_right()
                choice_picked = 'reverse+right'
        elif mode_choice == 8:
                no_keys()
                choice_picked = 'nokeys'
        time1 = time.time()-now
        print(choice_picked, end=" ")      
        print("{0:.4f}".format(time1))
    except socket.timeout:
        print('REQUEST TIMED OUT')
    except  ConnectionResetError:
        print('connection was closed/reset')
        