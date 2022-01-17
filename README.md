# DeepFake-Videos-Detection
## Describtion
This work was developed using the Google Colab environment, so, you may change the format of the commands depending on where you're going to run it! 
## Getting Started

### Step 0 - Preparing your dataset
Before you can preprocess your dataset (do converting/cropping), you need first to rename the videos in your dataset and create a metadata file for it, so each video is labeled with either "REAL/FAKE" for further processing. To do so you need to run the following command:
```
!python ./00-Prepare_the_Dataset.py
```
### Step 1 - Converting the videos into frames
After your dataset being renamed and labeled, the first step to go through is to convert each video into frames, using the command below: 
```
!python ./01-Convert_Videos_to_Frames.py
```
### Step 2 - Cropping the faces from each frame 
Whenever the frames are extracted, we need to extract the face region in each frame, using MTCNN by run the following command:
```
!python ./02-Crop_Faces_Using_MTCNN.py
```
### Step 3 - Split the dataset
After converting the frames and do the cropping, the dataset will be ready for the splitting process. From this step, two directories will be created, one contain two sub folders named "real" & "fake", and the second one will contain three sub folders named "train", "val", "test", that will be used in the training process. Use this command to split your dataset:
```
!python ./03-Split_the_Dataset.py
```
### Step 4 - Train the model
```
# To deal with json data
import json
# To deal with OS folders and directories
import os
# To help us copying files efficiently
from distutils.dir_util import copy_tree
# Used also to dela with files (copying/replicating)
import shutil
# To deal with pandas dataframes
import pandas as pd
# To output a smart progress bar by wrapping around any iterable
from tqdm import tqdm
# To deal with plots 
import matplotlib.pyplot as plt
# Classification Evaluation metrics to calculate the efficiency of the model
from sklearn.metrics import classification_report, accuracy_score, precision_score, recall_score, f1_score
# Normalize function to normalize given data
from sklearn.preprocessing import normalize
# Sklearn metrics to implement scores, losses, and utility functions for evaluating classification performance.
import sklearn.metrics as metrics
# To ignore generated warnings 
import warnings
warnings.filterwarnings('ignore')
# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow.keras import backend as K
print('TensorFlow version: ', tf.__version__) # print the version of the TensorFlow
# ImageDataGenerator to generate batches of tensor image data with real-time data augmentation
from tensorflow.keras.preprocessing.image import ImageDataGenerator
# Importing keras apllications/models that can be used for prediction, feature extraction, and fine-tuning
from tensorflow.keras import applications
# Importing our model (EfficientNetB4)
from efficientnet.tfkeras import EfficientNetB4 #EfficientNetB1, EfficientNetB2, EfficientNetB3, EfficientNetB4, EfficientNetB5, EfficientNetB6, EfficientNetB7
# Sequentail model importing 
from tensorflow.keras.models import Sequential
# Importing Dense and Dropout layers from Keras
from tensorflow.keras.layers import Dense, Dropout
# Importing the Adam as our optimizer
from tensorflow.keras.optimizers import Adam
# Importing EarlyStopping, ModelCheckpoint as aour callbacks function
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
# Import the load_model function to load our saved model
from tensorflow.keras.models import load_model
# import the numpy to deal with arrays 
import numpy as np
```
