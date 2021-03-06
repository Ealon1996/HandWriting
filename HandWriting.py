# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 02:41:11 2018

@author: s7856
"""

import numpy as np 
from keras.utils import np_utils
from keras.datasets import mnist 
(X_train, y_train), (X_test, y_test) = mnist.load_data()
X_train = X_train.reshape(-1, 1,28, 28)/255.
X_test = X_test.reshape(-1, 1,28, 28)/255.
y_train = np_utils.to_categorical(y_train, num_classes=10)
y_test = np_utils.to_categorical(y_test, num_classes=10)

print (X_test.shape)
model = Sequential()

# Conv layer 1 output shape (32, 28, 28)
model.add(Convolution2D(
    batch_input_shape=(None, 1, 28, 28),
    filters=32,
    kernel_size=5,
    strides=1,
    padding='same',    
    data_format='channels_first',
))

model.add(MaxPooling2D(2, 2, 'same', data_format='channels_first'))
model.add(Convolution2D(64, 5, strides=1, padding='same', data_format='channels_first'))
model.add(MaxPooling2D(2, 2, 'same', data_format='channels_first'))
model.add(Flatten())
model.add(Dense(10,activation='softmax'))
adam = Adam(lr=1e-3)

# show model

model.summary()

model.compile(optimizer=adam,
              loss='categorical_crossentropy',
              metrics=['accuracy'])

print('Training ------------')
# Another way to train the model
model.fit(X_train, y_train, epochs=5, batch_size=64)
model.save('HW.py')
