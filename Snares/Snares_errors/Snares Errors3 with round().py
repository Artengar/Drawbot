#----
#Maarten Renckens's Snares animation
#Python script for Drawbot
#----

totalPages=30 #More large amount is required in order for the animation to work!
pageWidth=1000
pageHeight=1000
baseShapeWidth=20
baseShapeDistance=30
setpointOfShapes=-100
distanceOfShapes=0
centerPoint=0
actionRange=[]

#Create the pages
for page in range(totalPages):
    print(page)
    newPage(width=pageWidth, height=pageHeight)
    frameDuration(1/20)
    
    #set out the transformations
    #But the first page should remain static.
    stageOfAnimation=page
    #determine the distance between centerpoints:
    distanceCenterPoints = (pageWidth+1000)/(totalPages-2)
    #determine the centerpoint where the animation happens.
    centerPoint = round(-500 + stageOfAnimation*(distanceCenterPoints)-distanceCenterPoints, 2)
    print centerPoint
    
    # create the new  paths
    while distanceOfShapes < pageWidth+200:
        #check if in range of the action
        if centerPoint-300 < setpointOfShapes < centerPoint+300:
            #Set different alternative values
            if centerPoint+250 < setpointOfShapes < centerPoint+300:
                alternativePointOfShapes = setpointOfShapes+20
            if centerPoint+200 < setpointOfShapes < centerPoint+250:
                alternativePointOfShapes = setpointOfShapes+30
            if centerPoint+150 < setpointOfShapes < centerPoint+200:
                alternativePointOfShapes = setpointOfShapes+40
            elif centerPoint+50 < setpointOfShapes < centerPoint+150:
                alternativePointOfShapes = setpointOfShapes+30
            elif centerPoint-0 < setpointOfShapes < centerPoint+50:
                alternativePointOfShapes = setpointOfShapes+20
            elif centerPoint-50 < setpointOfShapes < centerPoint-0:
                alternativePointOfShapes = setpointOfShapes+10
            elif centerPoint-100 < setpointOfShapes < centerPoint-50:
                alternativePointOfShapes = setpointOfShapes-0
            elif centerPoint-200 < setpointOfShapes < centerPoint-100:
                alternativePointOfShapes = setpointOfShapes-10
            elif centerPoint-250 < setpointOfShapes < centerPoint-200:
                alternativePointOfShapes = setpointOfShapes+0
            elif centerPoint-300 < setpointOfShapes < centerPoint-250:
                alternativePointOfShapes = setpointOfShapes+5
            #Draw figure
            newPath()
            #set the first oncurve point
            moveTo((setpointOfShapes, 0))
            curveTo((alternativePointOfShapes, pageHeight/2), (alternativePointOfShapes, pageHeight/2), (setpointOfShapes, pageHeight))
            lineTo((setpointOfShapes+baseShapeWidth, pageHeight))
            curveTo((alternativePointOfShapes+baseShapeWidth, pageHeight/2), (alternativePointOfShapes+baseShapeWidth, pageHeight/2), (setpointOfShapes+baseShapeWidth, 0))
            lineTo((setpointOfShapes, 0))
            closePath()
            drawPath()
        else:
            #Draw figure
            newPath()
            #set the first oncurve point
            moveTo((setpointOfShapes, 0))
            curveTo((setpointOfShapes, pageHeight/2), (setpointOfShapes, pageHeight/2), (setpointOfShapes, pageHeight))
            lineTo((setpointOfShapes+baseShapeWidth, pageHeight))
            curveTo((setpointOfShapes+baseShapeWidth, pageHeight/2), (setpointOfShapes+baseShapeWidth, pageHeight/2), (setpointOfShapes+baseShapeWidth, 0))
            lineTo((setpointOfShapes, 0))
            closePath()
            drawPath()
        #Set the distance for the next shape:
        distanceOfShapes+=baseShapeWidth+baseShapeDistance
        setpointOfShapes+=baseShapeWidth+baseShapeDistance
    #prepare for a new page
    distanceOfShapes = 0
    setpointOfShapes = -100
    page+1

print("\nScript finished")

saveImage("~/Github/Drawbot/Snares.gif")
