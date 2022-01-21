# DeepFake-Videos-Detection
![This is an image](https://images.theconversation.com/files/280814/original/file-20190622-61756-1xr6291.jpg?ixlib=rb-1.1.0&q=45&auto=format&w=1000&fit=clip)
## Describtion
This work was developed using the Google Colab environment, so, you may change the format of the commands depending on where you're going to run it! 
## Getting Started
### A flow chart illustrating the whole process
![image](https://user-images.githubusercontent.com/52065067/150020271-eb74d75c-4310-4129-930b-ce34c15653d8.png)
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
To start the training process, you will need the splitted dataset from the previous steps, once you have it you may go through these steps respectively and run each block in its own cell in colab, to be easier to trace.<br/>
▶️ [Open in Colab](https://drive.google.com/file/d/1D-Mej3S_1MDT-uYWttLb7Xj42RzgAe5x/view?usp=sharing)

### Step 5 - Test the model
To test your trained model, you will need to go through the above steps and split the dataset. **_Important Note_: in step number 3, you may pay attention to the split ratio and make sure that the train and the validation ratio specified to .0 and the test for 1, since you only want to do a sample test!** <br/>
To start testing you may run this command:
```
!python ./Only_for_Testing.py
```
## Credits
```
Aaron Chong, Hugo Ng, "DeepFake-Detect," 2021
```
Enjoy!😊

