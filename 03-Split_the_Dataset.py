import json
import os
from distutils.dir_util import copy_tree
import shutil
import numpy as np
from split import *
import splitfolders

# The path of the dataset contains all the cropped faces 
# Note: All the previous steps modify the same folder so the base path is the same for the three processes
base_path = 'path to your dataset'

# The real and the fake folders here are created under the same directory, so be sure to put the same path for both!
# Create a new directory to store all the real cropped faces
dataset_path = 'path to save the REAL samples of faces under a folder named ../real'  
print('Creating Directory: ' + dataset_path)
os.makedirs(dataset_path, exist_ok=True)

# Create a new directory to store all the fake cropped faces
tmp_fake_path = 'path to save the FAKE samples of faces under a folder named ../fake'
print('Creating Directory: ' + tmp_fake_path)
os.makedirs(tmp_fake_path, exist_ok=True)

# This function is used to get the name of the videos only 
def get_filename_only(file_path):
    file_basename = os.path.basename(file_path)
    filename_only = file_basename.split('.')[0]
    return filename_only

# Open the metadata.json file, takes a file object & returns the json object then print the length of the metadata
with open(os.path.join(base_path, 'metadata.json')) as metadata_json:
    metadata = json.load(metadata_json)
    print(len(metadata))

# Create a folder under the specified path to store the REAL cropped faces in it
real_path = os.path.join(dataset_path, 'real')
print('Creating Directory: ' + real_path)
os.makedirs(real_path, exist_ok=True)

# Create a folder under the specified path to store the FAKE cropped faces in it
fake_path = os.path.join(dataset_path, 'fake')
print('Creating Directory: ' + fake_path)
os.makedirs(fake_path, exist_ok=True)

# Processing Directory: Seperate all the samples depending on their labels 
for filename in metadata.keys():
    print(filename)
    print(metadata[filename]['label'])
    tmp_path = os.path.join(os.path.join(base_path, get_filename_only(filename)), 'faces')
    print(tmp_path)
    if os.path.exists(tmp_path):
        if metadata[filename]['label'] == 'REAL':    
            print('Copying to :' + real_path)
            copy_tree(tmp_path, real_path)
        elif metadata[filename]['label'] == 'FAKE':
            print('Copying to :' + tmp_fake_path)
            copy_tree(tmp_path, tmp_fake_path)
        else:
            print('Ignored..')
            
# Print the total number of real faces
all_real_faces = [f for f in os.listdir(real_path) if os.path.isfile(os.path.join(real_path, f))]
print('Total Number of Real faces: ', len(all_real_faces))

# Print the total number of fake faces
all_fake_faces = [f for f in os.listdir(tmp_fake_path) if os.path.isfile(os.path.join(tmp_fake_path, f))]
print('Total Number of Fake faces: ', len(all_fake_faces))

# Do the replacing
random_faces = np.random.choice(all_fake_faces, len(all_real_faces), replace=False)
for fname in random_faces:
    src = os.path.join(tmp_fake_path, fname)
    dst = os.path.join(fake_path, fname)
    shutil.copyfile(src, dst)

print('Down-sampling Done!') 

# Split into Train/ Val/ Test folders based on a given ratio
splitfolders.ratio(dataset_path, output='/content/drive/MyDrive/final_training_split', seed=1377, ratio=(.8, .1, .1)) # default values
print('Train/ Val/ Test Split Done!')