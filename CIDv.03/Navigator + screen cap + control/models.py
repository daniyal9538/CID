
import tensorflow as tf
import keras
from keras.layers import Dense, Conv2D
from keras.layers import Flatten
from keras.layers import MaxPooling2D, GlobalAveragePooling2D
from keras.layers import Activation
from keras.layers import BatchNormalization
from keras.layers import Dropout
from keras.models import Sequential
from keras import backend as K

from keras import optimizers
import cv2
import matplotlib.pyplot as plt 

from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img
from keras.utils import np_utils
import numpy as np 

def model_1(height, width, channels, classes):
  model = Sequential()
    
  inputShape = (height, width, 1)
  chanDim = -1

  model.add(Conv2D(32, (3,3), activation = 'relu', input_shape = inputShape))
  model.add(MaxPooling2D(2,2))
  model.add(BatchNormalization(axis = chanDim))
  model.add(Dropout(0.2))

  model.add(Conv2D(32, (3,3), activation = 'relu'))
  model.add(MaxPooling2D(2,2))
  model.add(BatchNormalization(axis = chanDim))
  model.add(Dropout(0.2))

  model.add(Conv2D(32, (3,3), activation = 'relu'))
  model.add(MaxPooling2D(2,2))
  model.add(BatchNormalization(axis = chanDim))
  model.add(Dropout(0.2))
  model.add(Flatten())

  model.add(Dense(512, activation = 'relu'))
  model.add(BatchNormalization(axis = chanDim))
  model.add(Dropout(0.5))
  model.add(Dense(classes, activation = 'softmax'))
  
  return (model)