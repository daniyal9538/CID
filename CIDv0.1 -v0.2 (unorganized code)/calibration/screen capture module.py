from screen_capture import grab_screen
import cv2
import time
import numpy as np
import keyboard
import sys
inputX = 1280
inputY = 720

# while(True):
#     temp = time.time()
#     output = grab_screen(region=(0,40,inputX,inputY+40))
#     output1 = cv2.resize(output, (480, 270))
#     now = time.time()-temp
#     print("output 1 {0} {1:.2f}".format( output1.shape, 1/now), end = "||")

    
#     output1 = cv2.cvtColor(output1, cv2.COLOR_BGR2RGB)
#     output2 = cv2.resize(output, (340, 191))
#     output2 = cv2.cvtColor(output2, cv2.COLOR_BGR2GRAY)
#     now1 = time.time()-temp
#     print("output 2 {0} {1:.2f}".format( output2.shape, 1/now1), end = "||")

    
#     output3 = cv2.resize(output, (160, 120))
#     output3 = cv2.cvtColor(output3, cv2.COLOR_BGR2GRAY)
#     now2 = time.time()-temp
#     print("output 3 {0} {1:.2f}".format( output3.shape, 1/now2))

#     cv2.imshow('output 1', output1)
#     cv2.imshow('output 2', output2)
#     cv2.imshow('output 3', output3)
#     if cv2.waitKey(25) & 0xFF == ord('q'):
#                 cv2.destroyAllWindows()
#                 break
i=0
f = False
data = []
while(True):
    
    
    if keyboard.is_pressed('c'):
        if (f == False):
            f = True
            i+=1
            print(i)
            output = grab_screen(region=(0,40,inputX,inputY+40))
            output = cv2.resize(output, (480, 270))
            data.append(output)
    if keyboard.is_pressed('s'):
        if(f==False):
            f=True
            np.save('cal_data', data)
            data.clear()
            print('data saved')

    if keyboard.is_pressed('r'):
        f=False
        print('Input Reset')
    if keyboard.is_pressed('q'):
        if(f==False):
            sys.exit(0)