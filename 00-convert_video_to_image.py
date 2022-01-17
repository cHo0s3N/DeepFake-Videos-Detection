import json
import os
import cv2
import math

# The path of the prepared dataset contains all the renamed videos with their metadata file
base_path = 'path to your dataset'

# This function is used to get the name of the videos only 
def get_filename_only(file_path):
    file_basename = os.path.basename(file_path) 
    filename_only = file_basename.split('.')[0] 
    return filename_only

# Open the metadata.json file, takes a file object & returns the json object then print the length of the metadata
with open(os.path.join(base_path, 'metadata.json')) as metadata_json:
    metadata = json.load(metadata_json)
    print(len(metadata))


for filename in metadata.keys():

    # Print the name of the file and check if it ends with '.mp4' & create a new folder for it
    # to save the frames extracted from the video into it, and if not continue
    print(filename) 
    if (filename.endswith(".mp4")):
        tmp_path = os.path.join(base_path, get_filename_only(filename))
        print('Creating Directory: ' + tmp_path)
        os.makedirs(tmp_path, exist_ok=True)
                
        # Here we define some important variables to convert the video to images
        print('Converting Video to Images...')
        count = 0
        video_file = os.path.join(base_path, filename) # To get the path to access the video to convert it to images
        cap = cv2.VideoCapture(video_file) # Define a video capture object to read a video
        frame_rate = cap.get(5) #frame rate
                
        # To initialize the capture
        while(cap.isOpened()):
            frame_id = cap.get(1) # Current frame number
            ret, frame = cap.read() # Returns True if the frame is read correctly
            
            # If the frame is not read correctly break the loop
            if (ret != True):
                break                          
            if (frame_id % math.floor(frame_rate) == 0):
                print('Original Dimensions: ', frame.shape)
                if frame.shape[1] < 300:
                    scale_ratio = 2
                elif frame.shape[1] > 1900:
                    scale_ratio = 0.33
                elif frame.shape[1] > 1000 and frame.shape[1] <= 1900 :
                    scale_ratio = 0.5
                else:
                    scale_ratio = 1
                print('Scale Ratio: ', scale_ratio)

                width = int(frame.shape[1] * scale_ratio)
                height = int(frame.shape[0] * scale_ratio)
                dim = (width, height)
                new_frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
                print('Resized Dimensions: ', new_frame.shape)

                new_filename = '{}-{:03d}.png'.format(os.path.join(tmp_path, get_filename_only(filename)), count)
                count = count + 1
                cv2.imwrite(new_filename, new_frame)
        cap.release()
        print("Done!")
    else:
        continue