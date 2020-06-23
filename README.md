# Folder-Splitter

## Summary

In image classification, datasets can be provided as a large folder with each training class divided into its own folder. 
This script splits each class up by a set split and creates a separate directory for validation, generating a train test split
while maintaining the classes. In addition each class is split by the same percentage so that the 
class distribution for training and validation is the same.

## Illustration

. <------ PUT YOUR SCRIPT HERE <br>
├── train <---- RENAME the main training folder to 'train' <br>
│---├── class1<br>
|-------├── img1.jpg<br>
|-------├── img2.jpg<br>
│---└── class2<br>
|<br>
├── validation<br>
|---├── class1<br>
|-------├── img1.jpg<br>
│---└── class2<br>
The script generates the validation folder

## Instructions for running
As per the illustration, put your script in the directory before the main directory that holds the class directories <br>
Rename this main directory 'train' as illustrated.

<strong>Arguments</strong>: <br>

<strong>python dir_splitter.py {split_percentage} {verbose}</strong> <br>

<strong>Split percentage </strong> refers to the training and validation split. Enter a float value between 0 and 1. Enter 0.8 if you want 20% of the images to be split into the validation, leaving 80% in the training folder. <br>
<strong>Verbose</strong> refers to the text printed when the script is run. Enter 1 for more text and 0 for none. Leave blank for a default of 1. <br>

<strong>ONLY RUN THIS SCRIPT ONCE! BACKUP YOUR DATASET BEFORE USING!</strong>
