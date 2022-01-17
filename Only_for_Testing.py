import json
import os
from distutils.dir_util import copy_tree
import shutil
import pandas as pd
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import load_model

# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow.keras import backend as K
print('TensorFlow version: ', tf.__version__)

input_size = 128
batch_size_num = 32

# Path to the splitted dataset that containes only your test samples without training/validation samples
dataset_path = 'path to your dataset'

# Path to save the temporery debug outputs
tmp_debug_path = 'path to save debug outputs'
print('Creating Directory: ' + tmp_debug_path)
os.makedirs(tmp_debug_path, exist_ok=True)

# Saving the test folder out from the dataset
test_path = os.path.join(dataset_path, 'test')

# Initialize the test data generator
test_datagen = ImageDataGenerator(
    rescale = 1/255    #rescale the tensor values to [0,1]
)

# Filling the test generator 
test_generator = test_datagen.flow_from_directory(
    directory = test_path,
    classes=['real', 'fake'],
    target_size = (input_size, input_size),
    color_mode = "rgb",
    class_mode = None,
    batch_size = 1,
    shuffle = False
)

# Path to saved weights file
checkpoint_filepath = 'path to the weights will be used for the testing process'
print('Creating Directory: ' + checkpoint_filepath)
os.makedirs(checkpoint_filepath, exist_ok=True)

# load the saved model that is considered the best to help generate best predictions
best_model = load_model(os.path.join(checkpoint_filepath, 'best_model.h5'))

# Generate predictions
test_generator.reset()

preds = best_model.predict(
    test_generator,
    verbose = 1
)

test_results = pd.DataFrame({
    "Filename": test_generator.filenames,
    "Prediction": preds.flatten()
})

# Generate predictions for each video 
l = test_results["Filename"]
new_list = []
for i in l:
    head, sep, tail = i.partition('-')
    new_list.append(head)

new = pd.DataFrame(new_list, columns = ['Filename'])
test_results["Filename"] = new
result = test_results.groupby('Filename').agg({'Prediction': ['mean', 'min', 'max']})

# Print the whole dataframe
print(result.to_string())

