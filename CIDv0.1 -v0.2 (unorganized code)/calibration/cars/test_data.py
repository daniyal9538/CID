#Author: Daniyal Selani

import numpy as np
import cv2

#this program iterates through data files and displays the images and onehot keypress arrays in dataset
#is needed to verify if data collection is working correctly


start_file = 0
end_file = 3
data = []
name = 'cal_data_'
for i in range(start_file, end_file+1):
        fileName =  name + "{}.npy".format(i)
        
        test = np.load(fileName, allow_pickle=True)
        
        for i in range(len(test)):
                data.append(test[i])
                cv2.imshow('w', test[i])
                #print(test[i][1])
                if cv2.waitKey(0) & 0xFF == ord('q'):
                        cv2.destroyAllWindows()
                        #break
# fileName =  name + ".npy"
        
# test = np.load(fileName, allow_pickle=True)
# for i in range(len(test)):
#         cv2.imshow('w', test[i])
#                 #print(test[i][1])
#         if cv2.waitKey(0) & 0xFF == ord('q'):
#                 cv2.destroyAllWindows()
#                 #33reak              
np.save('car_cal', data)    