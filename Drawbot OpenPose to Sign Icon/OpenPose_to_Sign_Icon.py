#OpenPose to Sign Icon
#Script by Maarten Renckens (Artengar.com)
#Creative Commons Licence: feel free to share as long as a reference to the original work is made. Thanks for appreciating others' work :)

#Notes: at this moment, the script starts from a non-moving body.
#Notes: the exact proportion of the belly button needs to be determined by images, it is estimated now

#PREPARATIONS: fill in the next variables:
#The path with the OpenPose files. If subfolders are present, this script will handle them accroding to folder name.
inputFolder = "~/Desktop/JSON input"

################################# Script data
import json
import os
fill(0, 0, 0) #everything is black
firstPage = True

#import the data
#print(currentFile.get("people")) #A check to see if the file is loaded correctly
#!!!!!!!!!!!!!!!!!!!







#Draw one page
def drawPage(currentName):
    if firstPage == False: newPage(width=1000, height=1000)
    translate(500, 350)
    
    rect(-5, -100, 10, 450) #body
    rect(-5, 375, 10, 125) #head
    
    text("This script is in beta version. Please do not distribute yet, but contact Maarten Renckens in stead.", (0, -325), align="center")
    fontSize(24)
    text(currentName, (0, -300), align="center")







#delete invisible Mac files from the list
def removeMacFiles(list):
    if firstLevel[0][0] == ".":
        firstLevel.pop(0)





#Create Sign Icons
def createOneSignIcon(inputDirectory):
    print("\nLOG: One Sign Icon started for folder", inputDirectory)
    headTop = []
    neck = []
    pelvis = []
    lefthand = []
    righthand = []
    
    #read every file
    folderContents = os.listdir(os.path.expanduser(inputDirectory))
    removeMacFiles(folderContents.sort())
    #import json data
    for DataFile in folderContents:
        #information about how to extract data from OpenPose: https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/output.md#keypoint-ordering
        currentDataFile = json.loads(open(os.path.expanduser(inputDirectory + DataFile), "r").read())
        headTop += [[currentDataFile["people"][0]["pose_keypoints_2d"][0], currentDataFile["people"][0]["pose_keypoints_2d"][1]]]
        neck += [[currentDataFile["people"][0]["pose_keypoints_2d"][3], currentDataFile["people"][0]["pose_keypoints_2d"][4]]]
        pelvis += [[currentDataFile["people"][0]["pose_keypoints_2d"][24], currentDataFile["people"][0]["pose_keypoints_2d"][25]]]
        
        lefthand += [[currentDataFile["people"][0]["pose_keypoints_2d"][9], currentDataFile["people"][0]["pose_keypoints_2d"][10]]]
        righthand += [[currentDataFile["people"][0]["pose_keypoints_2d"][21], currentDataFile["people"][0]["pose_keypoints_2d"][22]]]
        
    #####Filter if zero!!!!!!!!!!!!!
    
    #get the name of this sign (assumed the files are named well)
    currentName = os.path.basename(os.path.normpath(inputDirectory))
    #Send the data to be drawn
    drawPage(currentName)
    
    #info for drawing
    fill(0, 0, 0, 0)
    stroke(0)
    strokeWidth(1)
    #Finish the lefthand
    print("lefthand:", lefthand)
    path = BezierPath()
    path.moveTo((lefthand[0][0]*13-2000,lefthand[0][1]*13-2000))
    for coordinate in lefthand[1:]:
        print(coordinate)
        path.lineTo((coordinate[0]*13-2000,coordinate[1]*13-2000))
    drawPath(path)






#RUN the script
#Get what is in the input folder
if inputFolder[len(inputFolder)-1] != "/": inputFolder += ("/")
firstLevel = os.listdir(os.path.expanduser(inputFolder))
removeMacFiles(firstLevel.sort())
#Check if the folder contains subfolders
##handle subfolders
if os.path.isdir(os.path.expanduser(inputFolder + firstLevel[0])) == True:
    for item in firstLevel:
        #Create the subdirectory
        inputDirectory = inputFolder + item + "/"
        createOneSignIcon(inputDirectory)#Create SignIcons with EACH folder from the inputPath
##or handle no subfolders
        firstPage = False
else:
    inputDirectory = inputFolder
    createOneSignIcon(inputDirectory)#Create SignIcons with the inputPath






