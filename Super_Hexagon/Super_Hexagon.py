#Super Hexagon in Glyphs!

amountOfPages = 90 #360 degrees devided by the variable turnDirections is the minimum (except when only doing square animations)
canvasWidth=1000
canvasheight=1000
baseformRadius=40
baseformScale=[0,1]
turnDirection=-2
previousTurnAngle=0
sides=6

#colors
colA1=246/255#brightest
colA2=202/255
colA3=23/255
colB1=246/255#secondary background
colB2=172/255
colB3=23/255
colC1=136/255#First, darkest background
colC2=91/255
colC3=23/255
#A fourth color is needed when five sides are set.


#Start making an animation
import math
import random

#Define the background
def baseform(sides, baseformScale):
    #Draw the triangular backgrounds (1 side = 1 background)
    for side in range(sides):
        singleAngle= 360/sides
        angle = 360/sides*side+45 
        print("angle = %s" %angle)
        fill(colB1, colB2, colB3)
        if side %2 != 0:
            newPath()
            moveTo((0,0))
            #First line
            #!!! a tan of 0, 90, 180 or 270 is infinite! counter that.
            if angle == 0 or angle == 360:
                print("Infinite! 0degrees. Countering.")
                lineTo((0,5000))
            elif 0 < angle < 90 or 360 < angle < 450:
                lineTo(( math.sin(math.radians(angle))*canvasWidth, math.cos(math.radians(angle))*canvasWidth ))
            elif angle == 90:
                print("Infinite! 90degrees. Countering.")
                lineTo((5000,0))
            elif 90 < angle < 180:
                lineTo(( math.sin(math.radians(angle))*canvasWidth, math.cos(math.radians(angle))*canvasWidth ))
            elif angle == 180:
                print("Infinite! 180degrees. Countering.")
                lineTo((0,-5000))
            elif 180 < angle < 270:
                lineTo(( math.sin(math.radians(angle))*canvasWidth, math.cos(math.radians(angle))*canvasWidth ))
            elif angle == 270:
                print("Infinite! 270degrees. Countering.")
                lineTo((-5000,0))
            elif 270 < angle < 360:
                lineTo(( math.sin(math.radians(angle))*canvasWidth, math.cos(math.radians(angle))*canvasWidth ))
            
            angle = angle + singleAngle
            print("Second Angle = %s" %angle)
            #Second line
            #!!! a tan of 0, 90, 180 or 270 is infinite! counter that.
            if angle == 0 or angle == 360:
                print("Infinite! 0degrees. Countering.")
                lineTo((0,5000))
            elif 0 < angle < 90 or 360 < angle < 450:
                lineTo(( math.sin(math.radians(angle))*canvasWidth, math.cos(math.radians(angle))*canvasWidth ))
            elif angle == 90:
                print("Infinite! 90degrees. Countering.")
                lineTo((5000,0))
            elif 90 < angle < 180:
                lineTo(( math.sin(math.radians(angle))*canvasWidth, math.cos(math.radians(angle))*canvasWidth ))
            elif angle == 180:
                print("Infinite! 180degrees. Countering.")
                lineTo((0,-5000))
            elif 180 < angle < 270:
                lineTo(( math.sin(math.radians(angle))*canvasWidth, math.cos(math.radians(angle))*canvasWidth ))
            elif angle == 270:
                print("Infinite! 270degrees. Countering.")
                lineTo((-5000,0))
            elif 270 < angle < 360:
                lineTo(( math.sin(math.radians(angle))*canvasWidth, math.cos(math.radians(angle))*canvasWidth ))
            #Third line to close the triangular background
            lineTo((0,0))
            closePath()
            drawPath()

    fill(colC1, colC2, colC3)
    strokeWidth(10)
    stroke(colA1, colA2, colA3)
    
    #form in the middle
    newPath()
    moveTo(( math.sin(math.radians(angle))*baseformRadius*baseformScale[1], math.cos(math.radians(angle))*baseformRadius*baseformScale[1] ))
    for side in range(sides-1):
        side+=1
        singleAngle= 360/sides
        angle = 360/sides*side+0+45
        lineTo(( math.sin(math.radians(angle))*baseformRadius*baseformScale[1], math.cos(math.radians(angle))*baseformRadius*baseformScale[1] ))
    #rect(-baseformRadius, -baseformRadius, baseformRadius*2, baseformRadius*2)
    lineTo(( math.sin(math.radians(angle))*baseformRadius*baseformScale[1], math.cos(math.radians(angle))*baseformRadius*baseformScale[1] ))
    closePath()
    drawPath()





for page in range(amountOfPages):
    print("+++++ Starting page %s +++++" %page)
    if page != 0:
        newPage()
    translate(canvasWidth/2, canvasheight/2)
    fill(colC1, colC2, colC3)
    rect(-canvasWidth/2, -canvasheight/2, canvasWidth, canvasheight)
    
    if page !=0:
        previousTurnAngle+=turnDirection
    rotate(previousTurnAngle)
    #Events after a certain time (read: certain amount of pages)
    #scaling
    if page > 10:
        if baseformScale == [0,1]:
            baseformScale = [1,1.05]
        if baseformScale == [1,1.05]:
            baseformScale = [1,1.10]
        if baseformScale == [1,1.10]:
            baseformScale = [0,1.05]
        if baseformScale == [0,1.05]:
            baseformScale = [0,1]
    if page % 30 == 0:
        print("Rotating change!")
        turnDirection=random.randint(-3,3)
        while turnDirection==0:
            turnDirection=random.randint(-3,3)
    
    baseform(sides, baseformScale)




saveImage("~/Desktop/Super_Hexagon.gif")




