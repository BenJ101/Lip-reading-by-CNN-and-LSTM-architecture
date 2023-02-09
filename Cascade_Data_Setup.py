import os
path = 'C:\Intro to AI\LipReading\lipread_mp4'
# list of all labels
labels = [f.name for f in os.scandir(path) if f.is_dir()]

# list of all paths from labels
paths = [os.path.join(path, label) for label in labels]
print(paths)

for path in paths:
    for folder in os.listdir(path):
        root = os.path.join(path, folder)
        # list of all files in folder
        files = os.listdir(root)
        #if mp4 and txt in folder
        if any(f.endswith('.mp4') for f in files) and any(f.endswith('.txt') for f in files):
            # filter by mp4 and txt in current path
            files = [f for f in files if f.endswith('.mp4') or f.endswith('.txt')]
            files.sort()
            #create folder with every two of the filtered files
            for i in range(0, len(files), 2):
                folder = os.path.join(root, files[i][:-4])
                os.mkdir(folder)
                os.rename(os.path.join(root, files[i]), os.path.join(folder, files[i]))
                os.rename(os.path.join(root, files[i+1]), os.path.join(folder, files[i+1]))


# use cv2 to extract frames from videos and save them in the same folder as jpgs
import cv2 
import os
import numpy as np
import matplotlib.pyplot as plt

for path in paths:
    for folder in os.listdir(path):
        root = os.path.join(path, folder)    # path to folder
        files = os.listdir(root)         # list of all utterances in folder
        for file in files:
            sub_folder = os.path.join(root, file)   # path to utterance
            # if no jpgs in utterance folder
            if not any(f.endswith('.jpg') for f in os.listdir(sub_folder)):
                # video of utterance
                vidcap = cv2.VideoCapture(os.path.join(sub_folder, file+'.mp4'))
                success, image = vidcap.read()
                count = 0
                success = True
                while success:
                    success, image = vidcap.read()
                    if success:
                        # save with file name and frame number
                        cv2.imwrite(os.path.join(sub_folder, file+'_%d.jpg') % count, image)
                        count += 1
            

