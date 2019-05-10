import random
import socket
import numpy as np
import sys
import cv2
from getkeys import key_check

w = [1,0,0,0,0,0,0,0,0]
s = [0,1,0,0,0,0,0,0,0]
a = [0,0,1,0,0,0,0,0,0]
d = [0,0,0,1,0,0,0,0,0]
wa = [0,0,0,0,1,0,0,0,0]
wd = [0,0,0,0,0,1,0,0,0]
sa = [0,0,0,0,0,0,1,0,0]
sd = [0,0,0,0,0,0,0,1,0]
nk = [0,0,0,0,0,0,0,0,1]

def keys_to_output(keys):
    '''
    Convert keys to a ...multi-hot... array
     0  1  2  3  4   5   6   7    8
    [W, S, A, D, WA, WD, SA, SD, NOKEY] boolean values.
    '''
    output = [0,0,0,0,0,0,0,0,0]

    if 'W' in keys and 'A' in keys:
        output = wa
    elif 'W' in keys and 'D' in keys:
        output = wd
    elif 'S' in keys and 'A' in keys:
        output = sa
    elif 'S' in keys and 'D' in keys:
        output = sd
    elif 'W' in keys:
        output = w
    elif 'S' in keys:
        output = s
    elif 'A' in keys:
        output = a
    elif 'D' in keys:
        output = d
    else:
        output = nk
    return output


server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#print('flag1')
server_socket.bind(('', 12000))
#print('flag2')
l = 0
while True:
    l+=1
    rand = random.randint(0, 10)
    message, address = server_socket.recvfrom(66000)
    #print(sys.getsizeof(message), address)
    decoded = np.frombuffer(message, dtype=np.uint8).reshape(191, 340)
    #decoded = np.reshape(decoded, (10, 10))
    #print(decoded.shape, type(decoded), len(decoded), sys.getsizeof(decoded))
    x=decoded
    
    
    cv2.imshow('w', cv2.resize(decoded, (480, 270)))
    if cv2.waitKey(10)&0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
    #message = np.array([1, 0, 0, l], dtype=np.uint8)
    #print(message)

    keys = key_check()
    output = keys_to_output(keys)
    message = np.array(output, dtype=np.uint8)
    print(message)
    message = message.tobytes()
    #message = message.upper()
    
    server_socket.sendto(message, address)
        