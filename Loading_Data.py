# 0. Load keras package needed
import numpy as np
import tensorflow as tf
import keras
import os # drectory library
import cv2 # image processing library
from keras.layers import Activation
from keras.layers import Dropout
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Input
from keras.layers import Flatten
from keras.layers import Input
from keras.layers import TimeDistributed
from keras import applications
from keras import optimizers
from keras.models import Model
from keras.models import load_model
# Fix random seed
np.random.seed(3)


timesteps = 27 # input frame numbers for LSTM
n_labels = 4 # Number of Dataset Labels
Learning_rate = 0.0001 # Oprimizers lr, in this case, for adam
batch_size = 32
validation_ratio = 0.2 
num_epochs = 50
img_col = 128 # Transfer model input size ( MobileNet )
img_row = 128 # Transfer model input size ( MobileNet )
img_channel = 3 # RGB


# 1. Creating Datasets
# define temporary empty list for load
data = []
label = []
Totalnb = 0

# loop through each label (i)
    # each label look at train folder
    # in train folder loop through mp4 files (j) file
    # create a folder and add that mp4 and metadata to a folder
            # create jpg files from mp4 (k) frame in the folder
            
# Load Dataset
path = 'C:\Intro to AI\LipReading\lipread_mp4'
# Loop through all labels
for i, ind_label in enumerate(os.listdir(path)):
    # go through train folder
    for j, file in enumerate(os.listdir(os.path.join(path, ind_label, 'test'))):
        # loop through all jpgs in folder
        temp = []
        jpgs = os.listdir(os.path.join(path, ind_label, 'test', file))
        jpgs = [f for f in jpgs if f.endswith('.jpg')]
        for k, frame in enumerate(jpgs):
            name = os.path.join(path, ind_label, 'test', file, frame)
            img = cv2.imread(name)
            res = cv2.resize(img, dsize=(img_col, img_row), interpolation=cv2.INTER_CUBIC)
            temp.append(res)
        label.append(i)        
        data.append(temp)
        Totalnb += 1
print("Total Number of Data is: ", Totalnb)

# Convert List to numpy array, for Keras use
Train_label = np.eye(n_labels)[label] # One-hot encoding by np array function
Train_data = np.array(data)
print("Dataset shape is",Train_data.shape, "(size, timestep, column, row, channel)")
print("Label shape is",Train_label.shape,"(size, label onehot vector)")