# DeepFake-Videos-Detection
## Describtion
This work was developed using the Google Colab environment, so, you may change the commands depending on where you're going to run it! 
## Getting Started
### Preparing your dataset
Before you can preprocess your dataset (converting/cropping), you need first to rename the videos in your dataset and create a metadata file for it, so each video is labeled with either "REAL/FAKE" for further processing. To do so you need to run the following command.
```
!python ../00-Prepare_the_Dataset.py
```
