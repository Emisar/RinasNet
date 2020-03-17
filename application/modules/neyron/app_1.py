from __future__ import absolute_import, division, print_function, unicode_literals

import numpy as np
import matplotlib.pyplot as plt
import os
import cv2

# TensorFlow и tf.keras
import tensorflow as tf
from tensorflow import keras

DATADIR = "D:/RinasNET/dataset"
TESTDATADIR = "D:/RinasNET/testdataset"
CATEGORIES = ["Rinas", "People"]
class_names = CATEGORIES
IMG_SIZE = 128

def create_training_data(DATADIR):
    training_data = []
    for category in CATEGORIES:
        path = os.path.join(DATADIR, category)
        class_num = CATEGORIES.index(category)
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
                new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
                training_data.append([new_array, class_num])
            except Exception as e:
                pass
    return training_data

train_images = []
train_labels = []
test_images = []
test_labels = []

trdata = create_training_data(DATADIR)
for data in trdata:
    train_images.append(data[0])
    train_labels.append(data[1])

trdata = create_training_data(TESTDATADIR)
for data in trdata:
    test_images.append(data[0])
    test_labels.append(data[1])

train_images = np.array(train_images)
train_images.shape
train_images = train_images / 255.0
train_labels = np.array(train_labels)
test_images = np.array(test_images)
test_images.shape
test_images = test_images / 255.0

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(128, 128)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(2, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=10)

predictions = model.predict(test_images)
print(np.argmax(predictions[0]))
print(test_labels[0])


def plot_image(i, predictions_array, true_label, img):
    predictions_array, true_label, img = predictions_array[i], true_label[i], img[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])

    plt.imshow(img, cmap=plt.cm.binary)

    predicted_label = np.argmax(predictions_array)
    if predicted_label == true_label:
        color = 'blue'
    else:
        color = 'red'

    plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                100*np.max(predictions_array),
                                class_names[true_label]),
                                color=color)


num_rows = 4
num_cols = 2
num_images = num_rows*num_cols
plt.figure(figsize=(2*2*num_cols, 2*num_rows))
for i in range(num_images):
    plt.subplot(num_rows, 2*num_cols, 2*i+1)
    plot_image(i, predictions, test_labels, test_images)
plt.show()


