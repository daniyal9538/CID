#Author: Sentdex
#Edited and Updated: Daniyal Selani

import socket

import sys



from grabscreen import grab_screen
import cv2
import time
from directkeys import PressKey,ReleaseKey, W, A, S, D, noKey

from models import *
from getkeys import key_check
from collections import deque, Counter
import random
from statistics import mode,mean
import numpy as np
import keras


#from motion import motion_detection

#Program runs indefinitely
#A trained model is loaded into the program
#THe program captures screen window as defined below
#The image is processed and compressed and sent to model to get prediction for corrosponding answer
#The program interprets the prediction result from model and performs the required action


GAME_WIDTH = 1280
GAME_HEIGHT = 720



# how_far_remove = 800
# rs = (20,15)
# log_len = 25

#motion_req = 800#number of frames passed without detecting motion
#motion_log = deque(maxlen=log_len)#log of every frame's motion (if car was stuck or not)

# WIDTH = 480
# HEIGHT = 270
# LR = 1e-3
# EPOCHS = 10

choices = deque([], maxlen=5)#log of all choices
hl_hist = 250#max lenght of log
choice_hist = deque([], maxlen=hl_hist) #most recent log

w = [1,0,0,0,0,0,0,0,0]
s = [0,1,0,0,0,0,0,0,0]
a = [0,0,1,0,0,0,0,0,0]
d = [0,0,0,1,0,0,0,0,0]
wa = [0,0,0,0,1,0,0,0,0]
wd = [0,0,0,0,0,1,0,0,0]
sa = [0,0,0,0,0,0,1,0,0]
sd = [0,0,0,0,0,0,0,1,0]
nk = [0,0,0,0,0,0,0,0,1]

w = [1,0,0,0,0,0,0,0,0]
s = [0,1,0,0,0,0,0,0,0]
a = [0,0,1,0,0,0,0,0,0]
d = [0,0,0,1,0,0,0,0,0]

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#print('flag1')
server_socket.bind(('', 12000))
#print('flag2')

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
    noKey()


model = model_1(120, 160, 1, 5)
MODEL_NAME = 'models_my_model.h5'
model = keras.models.load_model(MODEL_NAME)

print('We have loaded a previous model!!!!')

def main():
    last_time = time.time()
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

    paused = False
    mode_choice = 0

    screen = grab_screen(region=(0,40,GAME_WIDTH,GAME_HEIGHT+40))
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    prev = cv2.resize(screen, (160,120))

    t_minus = prev
    t_now = prev
    t_plus = prev

    while(True):
        
        
        if not paused:
            #message, address = server_socket.recvfrom(66000)
        #print(sys.getsizeof(message), address)
            #decoded = np.frombuffer(message, dtype=np.uint8).reshape(191, 340)
            #screen = decoded
            
            screen = grab_screen(region=(0,40,GAME_WIDTH,GAME_HEIGHT+40))
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            last_time = time.time()
            screen = cv2.resize(screen, (160,120))
            cv2.imshow('w', screen)
            if cv2.waitKey(1)&0xFF == ord('q'):
                cv2.destroyAllWindows()
                
            #delta_count_last = motion_detection(t_minus, t_now, t_plus)

            t_minus = t_now
            t_now = t_plus
            t_plus = screen
            t_plus = cv2.blur(t_plus,(4,4))

            prediction = model.predict([screen.reshape(-1,120,160,1)])[0]
            prediction = np.array(prediction) 
            print(prediction)
            mode_choice = np.argmax(prediction)
            #print(prediction, mode_choice)
            #message = mode_choice
    
            #message = message.tobytes()
            #message = message.upper()
            
            #server_socket.sendto(message, address)
            if mode_choice == 0:
                straight()
                choice_picked = 'straight'
                
            elif mode_choice == 1:
                reverse()
                choice_picked = 'reverse'
                
            elif mode_choice == 2:
                forward_left()
                choice_picked = 'left'
            elif mode_choice == 3:
                forward_right()
                choice_picked = 'right'
            elif mode_choice == 4:
                no_keys()
                choice_picked = 'nokeys'


            #elif mode_choice == 4:
            #    forward_left()
            #     choice_picked = 'forward+left'

            # elif mode_choice == 5:
            #     forward_right()
            #     choice_picked = 'forward+right'
            # elif mode_choice == 6:
            #     reverse_left()
            #     choice_picked = 'reverse+left'
            # elif mode_choice == 7:
            #     reverse_right()
            #     choice_picked = 'reverse+right'
            

            # #logging capabilities were added but not used or tested till now
            # motion_log.append(delta_count)
            # motion_avg = round(mean(motion_log),3)
            # print('loop took {} seconds. Motion: {}. Choice: {}'.format( round(time.time()-last_time, 3) , motion_avg, choice_picked))
            # #If program detects a lack of motion, it randomly choses some evasive manuevers
            # #Feature not tested as of yet
            # if motion_avg < motion_req and len(motion_log) >= log_len:
            #     print('WERE PROBABLY STUCK FFS, initiating some evasive maneuvers.')

            #     # 0 = reverse straight, turn left out
            #     # 1 = reverse straight, turn right out
            #     # 2 = reverse left, turn right out
            #     # 3 = reverse right, turn left out

            #     quick_choice = random.randrange(0,4)
                
            #     if quick_choice == 0:
            #         reverse()
            #         time.sleep(random.uniform(1,2))
            #         forward_left()
            #         time.sleep(random.uniform(1,2))

            #     elif quick_choice == 1:
            #         reverse()
            #         time.sleep(random.uniform(1,2))
            #         forward_right()
            #         time.sleep(random.uniform(1,2))

            #     elif quick_choice == 2:
            #         reverse_left()
            #         time.sleep(random.uniform(1,2))
            #         forward_right()
            #         time.sleep(random.uniform(1,2))

            #     elif quick_choice == 3:
            #         reverse_right()
            #         time.sleep(random.uniform(1,2))
            #         forward_left()
            #         time.sleep(random.uniform(1,2))

            #     for i in range(log_len-2):
            #         del motion_log[0]
    
        keys = key_check()

        # p pauses game and can get annoying.
        if 'T' in keys:
            if paused:
                paused = False
                time.sleep(1)
            else:
                paused = True
                ReleaseKey(A)
                ReleaseKey(W)
                ReleaseKey(D)
                time.sleep(1)

main()       
