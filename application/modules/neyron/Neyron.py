from __future__ import absolute_import, division, print_function, unicode_literals

import numpy as np
import matplotlib.pyplot as plt
import os
import cv2

import tensorflow as tf
from tensorflow import keras

class Neyron():
    def __init__(self, options):
        super().__init__()
        self.DATA_DIR = options['DATA_SET']
        self.TEST_DATA_DIR = options['TEST_DATA_SET']
        self.CATEGORIES = ["Rinas", "People"]
        self.CLASS_NAMES = self.CATEGORIES
        self.IMG_SIZE = 128

        trainImages = []
        trainLabels = []
        testImages = []
        testLabels = []

        trData = self.createTrainingData(self.DATA_DIR)
        for data in trData:
            trainImages.append(data[0])
            trainLabels.append(data[1])

        trainImages = np.array(trainImages)
        trainImages.shape
        trainImages = trainImages / 255.0
        trainLabels = np.array(trainLabels)

        self.model = keras.Sequential([
            keras.layers.Flatten(input_shape=(128, 128)),
            keras.layers.Dense(128, activation='relu'),
            keras.layers.Dense(2, activation='softmax')
        ])

        self.model.compile(optimizer='adam',
                    loss='sparse_categorical_crossentropy',
                    metrics=['accuracy'])

        self.model.fit(trainImages, trainLabels, epochs=10)
            
    def createTrainingData(self, dataDir):
        trainingData = []
        for category in self.CATEGORIES:
            path = os.path.join(dataDir, category)
            classNum = self.CATEGORIES.index(category)
            for img in os.listdir(path):
                try:
                    imgArray = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
                    newArray = cv2.resize(imgArray, (self.IMG_SIZE, self.IMG_SIZE))
                    trainingData.append([newArray, classNum])
                except Exception as e:
                    pass
        return trainingData

    def toPrediction(self, img):
        print(img)
        
            
        
