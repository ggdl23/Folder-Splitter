import os
from random import sample
import shutil
import sys


def folder_splitter(path, split_pct, verbose=1):
    
    #make validation directory
    try:
        valid_path = os.path.join(path, 'validation')
        os.makedirs(valid_path)
        if verbose:
            print("New directory created")
    except FileExistsError:
        if verbose:
            print("Directory already exists")
    
    #iterate through each folder
    train_path = os.path.join(path, 'train')
    for class_dir in os.listdir(train_path):
        
        #check for and create a new path for each class for validation data
        oldTrainDir = os.path.join(train_path, class_dir)
        newValidDir = os.path.join(valid_path, class_dir)
        
        if os.path.isdir(newValidDir):
            pass
        else:
            if verbose:
                print("Creating validation directory for class " + class_dir)
            os.mkdir(newValidDir)
        
        data_list = os.listdir(oldTrainDir)
        
        sampleFiles = sample(data_list, int((1-split_pct)* len(data_list)))
        
        #iterate through sampleFiles and cut and paste them into newValidDir
        
        for imgFile in sampleFiles:
            shutil.move(os.path.join(oldTrainDir, imgFile), os.path.join(newValidDir, imgFile))
        
        if verbose:
            print("Class " + class_dir + "split complete.")
    print("Process Complete")


invalid = False

data_path = os.path.abspath('')

try:
    split = sys.argv[1]
except IndexError:
    print("Please enter valid arguments.")
    sys.exit()

try:
    verbose = sys.argv[2]
except IndexError:
    verbose = 1

try:
    split = float(split)
    verbose = int(verbose)
    if (split < 1 and split > 0) and verbose in [0,1]:
        folder_splitter(data_path, split, verbose)
    else:
        invalid = True
except ValueError:
    invalid = True
    
if invalid:
    print("Invalid Argument. Enter arg1 between 0 and 1 and arg2 as either 0 or 1.")

