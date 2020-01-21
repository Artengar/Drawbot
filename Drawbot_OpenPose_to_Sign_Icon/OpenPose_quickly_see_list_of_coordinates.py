import json
import os
inputFolder = "~/Desktop/JSON input test/"
lefthand = []

firstLevel = os.listdir(os.path.expanduser(inputFolder))
if firstLevel[0][0] == ".":
    firstLevel.pop(0)#remove Mac files from the list
firstLevel.sort()

for DataFile in firstLevel:
    currentDataFile = json.loads(open(os.path.expanduser(inputFolder + DataFile), "r").read())
    print("reading info from:", DataFile)

    lefthand += [[currentDataFile["people"][0]["pose_keypoints_2d"][9], currentDataFile["people"][0]["pose_keypoints_2d"][10]]]

print("lefthand x;y coordinates:", lefthand)