#OpenPose to Sign Icon
#Script by Maarten Renckens (Artengar.com)
#Creative Commons Licence: feel free to share as long as a reference to the original work is made. Thanks for appreciating others' work :)

#Notes: at this moment, the script starts from a non-moving body.

#PREPARATIONS: fill in the next variables:
#The path with the OpenPose files. If subfolders are present, this script will handle them accroding to folder name.
filePath = "~/Desktop/train_00000/image_00001_keypoints.json"

import json
import os

#import the data
currentFile = json.loads(open(os.path.expanduser(filePath), "r").read())
print(currentFile)
print(currentFile.get("people")) #A check to see if the file is loaded correctly
#!!!!!!!!!!!!!!!!!!!

#Draw the results:
newPage(width=1000, height=1000)
translate(500, 350)

fill(0, 0, 0) #black
rect(-5, -100, 10, 450) #body
rect(-5, 375, 10, 125) #head

fontSize(24)
text("Name", (0, -300), align="center")
