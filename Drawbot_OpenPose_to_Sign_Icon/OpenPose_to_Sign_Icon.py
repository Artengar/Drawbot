#OpenPose to Sign Icon
#Script by Maarten Renckens (Artengar.com)
#Creative Commons Licence: feel free to share as long as a reference to the original work is made. Thanks for appreciating others' work :)

#Notes: at this moment, the script starts from a non-moving body.
#Notes: the exact proportion of the belly button needs to be determined by images, it is estimated now

#YOUR INPUT: fill in the next information:
#The path with the OpenPose files. If subfolders are present, this script will handle them according to folder name.
inputFolder = "~/Desktop/JSON input"


# Script data ################################ Do not change!
import json
import os
fill(0, 0, 0) #everything is black
isFirstPage = True



def superimposeOrigins(DataFile, throwback):
    print("superimposing")
    neck = []
    pelvis = []
    
    currentDataFile = json.loads(open(os.path.expanduser(inputDirectory + DataFile), "r").read())
    #find the torso in the original data
    neck += [[currentDataFile["people"][0]["pose_keypoints_2d"][3], currentDataFile["people"][0]["pose_keypoints_2d"][4]]]
    pelvis += [[currentDataFile["people"][0]["pose_keypoints_2d"][24], currentDataFile["people"][0]["pose_keypoints_2d"][25]]]
    #convert this torso to the torso of the Sign Icons
    #208, 110 > 0, -100
    #212, 189 > 0, 375
    
    # how much should the image move over the x-axis to be positioned on the Sign Icon
    ##the smallest of the two, plus the average of the two
    if neck[0][0] < pelvis[0][0]:
        smallest = neck[0][0]
        difference = pelvis[0][0]-neck[0][0]
    else:
        smallest = pelvis[0][0]
        difference = neck[0][0]-pelvis[0][0]
    movementX = (smallest + difference)
    print("movementX:", movementX)
    #how much should the image move over the y-axis to be positioned on the Sign Icon
    ##the pelvis should be at y=-100
    movementY = -(pelvis[0][1] + abs(-100))
    print("movementY:", movementY)
    #delta y should be 475
    OpenPoseSpine = neck[0][1] - pelvis[0][1]
    desiredSpine = 450
    factorY = desiredSpine/-OpenPoseSpine
    print("factorY:", factorY)
    if throwback == "movementX":
        return movementX
        print("factorX:", factorY)
    if throwback == "movementY":
        return movementY
        print("movementY:", movementY)
    if throwback == "factorY":
        return factorY
        print("factorY:", factorY)





#Draw one page
def drawPage(currentName):
    if isFirstPage == False: newPage(width=1000, height=1000)
    translate(500, 350)
    
    rect(-2, -100, 4, 450) #body
    rect(-2, 375, 4, 125) #head
    
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
    #determine how to superimpose the OpenPose data on Sign Icons, based on the first file
    movementX = superimposeOrigins(folderContents[0], "movementX")
    movementY = superimposeOrigins(folderContents[0], "movementY")
    factorY = superimposeOrigins(folderContents[0], "factorY")
    
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
    #finish the spine (corrected around the centerpoint 0,-100)
    path = BezierPath()
    path.moveTo((-(neck[0][0]*factorY-(movementX*factorY)),-(neck[0][1]*factorY+(movementY*factorY))-100*factorY-100))
    print("DEBUG:", neck[0][1]*factorY+(movementY*factorY))
    path.lineTo((-(pelvis[0][0]*factorY-(movementX*factorY)),-(pelvis[0][1]*factorY+(movementY*factorY))-100*factorY-100))
    drawPath(path)
    #Finish the lefthand
    path = BezierPath()
    path.moveTo((-(lefthand[0][0]*factorY-(movementX*factorY)),-(lefthand[0][1]*factorY+(movementY*factorY))-100*factorY-100))
    for coordinate in lefthand[1:]:
        path.lineTo((-(coordinate[0]*factorY-(movementX*factorY)),-(coordinate[1]*factorY+(movementY*factorY))-100*factorY-100))
    drawPath(path)
    #Finish the righthand
    path = BezierPath()
    path.moveTo((-(righthand[0][0]*factorY-(movementX*factorY)),-(righthand[0][1]*factorY+(movementY*factorY))-100*factorY-100))
    for coordinate in righthand[1:]:
        path.lineTo((-(coordinate[0]*factorY-(movementX*factorY)),-(coordinate[1]*factorY+(movementY*factorY))-100*factorY-100))
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
        isFirstPage = False
else:
    inputDirectory = inputFolder
    createOneSignIcon(inputDirectory)#Create SignIcons with the inputPath






