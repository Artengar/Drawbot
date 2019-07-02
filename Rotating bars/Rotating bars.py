#----
#Maarten Renckens's Snares animation
#Python script for Drawbot
#For questions, please contact maarten.renckens@artengar.com
#----
import math
import numpy
#from fractions import Fraction
#Good explanation about sine, cosine and tangent: https://www.youtube.com/watch?v=VBygj7p0HKc

#Input that can be changed:
pageWidth=1000
pageHeight=1000
desiredAmountOfFrames=36
desiredAmountOfVisibleBars=20#With an amount to high, colors will not work well.
halfStrokeLength=600
#fixed variables;
if desiredAmountOfVisibleBars==0:
    desiredAmountOfVisibleBars=1
stepsInDegrees=360/desiredAmountOfFrames
frameNumber=0
barNumber=0
#frameDuration(1/60)

while frameNumber < desiredAmountOfFrames:
    newPage(pageWidth,pageHeight)
    translate(pageWidth/2,pageHeight/2)
    fill(1)
    rect(-pageWidth/2, -pageHeight/2, width(), height())
    
    #calculate corners and distances
    #the first bar is straight, but the possible other bars are not.
    thisStepInDegrees=stepsInDegrees*frameNumber-(desiredAmountOfVisibleBars-1)*stepsInDegrees
    print("degree:", thisStepInDegrees)
    #Draw all bars
    while barNumber < desiredAmountOfVisibleBars:
        inBetweenStep=thisStepInDegrees+barNumber*stepsInDegrees
        if inBetweenStep != 90:
            xDistance = (math.tan(math.radians(inBetweenStep)))
        else:
            xDistance = -halfStrokeLength
        print(barNumber, inBetweenStep)
        #THERE IS A MISTAKE IN CALCULATING THE LINE LENGTH.
        #WHEN HALFSTROKELENGTH IS SMALL, THIS IS VISIBLE…    
        yDistance = (math.sin(math.radians(inBetweenStep)*xDistance))
        #Draw the line
        visibility=1-((barNumber+1)*(1/desiredAmountOfVisibleBars))
        print(visibility)
        stroke(visibility, visibility, visibility)
        strokeWidth(125)
        #deterime the angle of the bar
        line((xDistance*halfStrokeLength,-halfStrokeLength), (-xDistance*halfStrokeLength,halfStrokeLength))
        #finish the loop
        barNumber+=1
    #finish the loop
    barNumber=0
    inBetweenStep=0
    frameNumber+=1

#saveImage("~/Github/Drawbot/Rotating_bars.gif")
saveImage("~/Desktop/Rotating_bars.gif")