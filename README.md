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
To start the training process, you will need to the splitted dataset from the previous step, once you have it you may go through these steps respectively and run each block in its own cell in colab, to be easier to trace.
1. You may copy & paste the content of this file on a cell and run it as the imported libraries used in the training process:
```
List of imported libraries.txt
```
🥇
