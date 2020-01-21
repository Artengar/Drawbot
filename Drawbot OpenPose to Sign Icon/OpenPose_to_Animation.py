#OpenPose Visualiser
#Script by Maarten Renckens (Artengar.com)
#Creative Commons Licence: feel free to share as long as a reference to the original work is made. Thanks for appreciating others' work :)

#YOUR INPUT: fill in the next information:
#The path with the OpenPose files. If subfolders are present, this script will handle them according to folder name.
inputFolder = "~/Desktop/JSON input"
exportFolder = "~/Desktop/"

# Script data ################################ Do not change!
import json
import os
fill(0, 0, 0) #everything is black
isFirstPage = True



#Draw one page
def drawPage(currentName, isFirstPage):
    frameDuration(0.5)
    if isFirstPage == False: newPage(width=1000, height=1000)
    frameDuration(0.5)
    fill(1)
    rect(0, 0, 1000, 1000)
    translate(500, 350)
    fontSize(24)
    fill(0)
    strokeWidth(0)
    text("Sign for ''" + currentName + "': animation", (0, -300), align="center")







#delete invisible Mac files from the list
def removeMacFiles(list):
    if firstLevel[0][0] == ".":
        firstLevel.pop(0)





#Create Animation
def createAnimation(inputDirectory, isFirstPage):
    print("\nLOG: Animation started for folder ''", inputDirectory, "'")
    
    key0headTop = []
    key1neck = []
    key2ShoulderRight = []
    key3 = []
    key4WrightRight = []
    key5ShoulderLeft = []
    key6 = []
    key7WrightLeft = []
    key8pelvis = []
    
    #read every file
    folderContents = os.listdir(os.path.expanduser(inputDirectory))
    if folderContents == []:
        print("LOG: This folder seems to be empty")
        return;
    removeMacFiles(folderContents.sort())
    
    #import json data
    for DataFile in folderContents:
        #information about how to extract data from OpenPose: https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/output.md#keypoint-ordering
        currentDataFile = json.loads(open(os.path.expanduser(inputDirectory + DataFile), "r").read())
        key0headTop += [[currentDataFile["people"][0]["pose_keypoints_2d"][0], currentDataFile["people"][0]["pose_keypoints_2d"][1]]]
        key1neck += [[currentDataFile["people"][0]["pose_keypoints_2d"][3], currentDataFile["people"][0]["pose_keypoints_2d"][4]]]
        key2ShoulderRight += [[currentDataFile["people"][0]["pose_keypoints_2d"][6], currentDataFile["people"][0]["pose_keypoints_2d"][7]]]
        key3 += [[currentDataFile["people"][0]["pose_keypoints_2d"][9], currentDataFile["people"][0]["pose_keypoints_2d"][10]]]
        key4WrightRight += [[currentDataFile["people"][0]["pose_keypoints_2d"][12], currentDataFile["people"][0]["pose_keypoints_2d"][13]]]
        key5ShoulderLeft += [[currentDataFile["people"][0]["pose_keypoints_2d"][15], currentDataFile["people"][0]["pose_keypoints_2d"][16]]]
        key6 += [[currentDataFile["people"][0]["pose_keypoints_2d"][18], currentDataFile["people"][0]["pose_keypoints_2d"][19]]]
        key7WrightLeft += [[currentDataFile["people"][0]["pose_keypoints_2d"][21], currentDataFile["people"][0]["pose_keypoints_2d"][22]]]
        key8pelvis += [[currentDataFile["people"][0]["pose_keypoints_2d"][24], currentDataFile["people"][0]["pose_keypoints_2d"][25]]]

    
    #get the name of this sign (assumed the files are named well)
    currentName = os.path.basename(os.path.normpath(inputDirectory))
    #Determine how much the image needs to be scaled and moved
    scaleX = 4
    scaleY = scaleX
    MoveX = -(key1neck[0][0]*scaleX) #The neck will be on x=0
    MoveY = -(key1neck[0][1]*scaleY+400) #The neck will be on y=400
    #Draw path by path
    frameNr=0
    while frameNr < len(folderContents):
        #Send the data to be drawn
        drawPage(currentName, isFirstPage)
        isFirstPage = False
    
        #info for drawing (needed to be reset after creating the pages)
        fill(0, 0, 0, 0)
        stroke(0)
        strokeWidth(2)
        ##Head
        path = BezierPath()
        path.moveTo(( (key0headTop[frameNr][0])*scaleX+MoveX, -(key0headTop[frameNr][1]*scaleY+MoveY) ))
        path.lineTo(( (key1neck[frameNr][0])*scaleX+MoveX, -(key1neck[frameNr][1]*scaleY+MoveY) ))
        drawPath(path)
        ##Spine
        path = BezierPath()
        path.moveTo(( (key1neck[frameNr][0])*scaleX+MoveX, -(key1neck[frameNr][1]*scaleY+MoveY) ))
        path.lineTo(( (key8pelvis[frameNr][0])*scaleX+MoveX, -(key8pelvis[frameNr][1]*scaleY+MoveY) ))
        drawPath(path)
        
        path = BezierPath()
        path.moveTo(( (key1neck[frameNr][0])*scaleX+MoveX, -(key1neck[frameNr][1]*scaleY+MoveY) ))
        path.lineTo(( (key2ShoulderRight[frameNr][0])*scaleX+MoveX, -(key2ShoulderRight[frameNr][1]*scaleY+MoveY) ))
        drawPath(path)
        
        path = BezierPath()
        path.moveTo(( (key2ShoulderRight[frameNr][0])*scaleX+MoveX, -(key2ShoulderRight[frameNr][1]*scaleY+MoveY) ))
        path.lineTo(( (key3[frameNr][0])*scaleX+MoveX, -(key3[frameNr][1]*scaleY+MoveY) ))
        drawPath(path)
        
        path = BezierPath()
        path.moveTo(( (key3[frameNr][0])*scaleX+MoveX, -(key3[frameNr][1]*scaleY+MoveY) ))
        path.lineTo(( (key4WrightRight[frameNr][0])*scaleX+MoveX, -(key4WrightRight[frameNr][1]*scaleY+MoveY) ))
        drawPath(path)
        
        path = BezierPath()
        path.moveTo(( (key1neck[frameNr][0])*scaleX+MoveX, -(key1neck[frameNr][1]*scaleY+MoveY) ))
        path.lineTo(( (key5ShoulderLeft[frameNr][0])*scaleX+MoveX, -(key5ShoulderLeft[frameNr][1]*scaleY+MoveY) ))
        drawPath(path)
        
        path = BezierPath()
        path.moveTo(( (key5ShoulderLeft[frameNr][0])*scaleX+MoveX, -(key5ShoulderLeft[frameNr][1]*scaleY+MoveY) ))
        path.lineTo(( (key6[frameNr][0])*scaleX+MoveX, -(key6[frameNr][1]*scaleY+MoveY) ))
        drawPath(path)
        
        path = BezierPath()
        path.moveTo(( (key6[frameNr][0])*scaleX+MoveX, -(key6[frameNr][1]*scaleY+MoveY) ))
        path.lineTo(( (key7WrightLeft[frameNr][0])*scaleX+MoveX, -(key7WrightLeft[frameNr][1]*scaleY+MoveY) ))
        drawPath(path)
    
        frameNr+=1
    #Add one empty page to the animation, to indicate when it is done.
    drawPage(currentName, isFirstPage)
    #Export all
    saveImage(exportFolder + currentName + ".mp4")



#RUN the script
#Get what is in the input folder
if inputFolder[len(inputFolder)-1] != "/": inputFolder += "/"
if exportFolder[len(exportFolder)-1] != "/": exportFolder += "/"


firstLevel = os.listdir(os.path.expanduser(inputFolder))
removeMacFiles(firstLevel.sort())
#Check if the folder contains subfolders
##handle subfolders
if os.path.isdir(os.path.expanduser(inputFolder + firstLevel[0])) == True:
    for item in firstLevel:
        #Create the subdirectory
        inputDirectory = inputFolder + item + "/"
        createAnimation(inputDirectory, isFirstPage)#Create files with EACH folder from the inputDirectory
        newDrawing()
##or handle no subfolders
else:
    inputDirectory = inputFolder
    createAnimation(inputDirectory)#create one file






