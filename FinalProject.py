from google.colab import drive

drive.mount('/content/drive')

import numpy as np
import pandas as pd
import os
print(os.listdir("/content/drive/MyDrive/cell_images"))

import cv2
import matplotlib.pyplot as plt 
import seaborn as sns
import os
from PIL import Image
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img
from keras.utils import np_utils

parasitized_data = os.listdir("/content/drive/MyDrive/cell_images/train/Parasitized")
print(parasitized_data[:10])
uninfected_data = os.listdir("/content/drive/MyDrive/cell_images/train/Uninfected")
print('\n')
print(uninfected_data[:10])

plt.figure(figsize = (12,12))
for i in range(4):
    plt.subplot(1, 4, i+1)
    img = cv2.imread("/content/drive/MyDrive/cell_images/train/Parasitized" + "/" + parasitized_data[i])
    plt.imshow(img)
    plt.title('PARASITIZED : 1')
    plt.tight_layout()
plt.show()

plt.figure(figsize = (12,12))
for i in range(4):
    plt.subplot(1, 4, i+1)
    img = cv2.imread("/content/drive/MyDrive/cell_images/train/Uninfected" + "/" + uninfected_data[i+1])
    plt.imshow(img)
    plt.title('UNINFECTED : 0')
    plt.tight_layout()
plt.show()

data = []
labels = []
for img in parasitized_data:
    try:
        img_read = plt.imread("/content/drive/MyDrive/cell_images/train/Parasitized" + "/" + img)
        img_resize = cv2.resize(img_read, (50, 50))
        img_array = img_to_array(img_resize)
        data.append(img_array)
        labels.append(1)
    except:
        None
        
for img in uninfected_data:
    try:
        img_read = plt.imread("/content/drive/MyDrive/cell_images/train/Uninfected" + "/" + img)
        img_resize = cv2.resize(img_read, (50, 50))
        img_array = img_to_array(img_resize)
        data.append(img_array)
        labels.append(0)
    except:
        None
        
"""
https://colab.research.google.com/drive/1va5ELTfA00yE8Q9Gh5DH8GGwIH0kI0d1?usp=sharing
Please check the above link for detailed Outputs!
"""
