#----
#Maarten Renckens's Snares animation
#Python script for Drawbot
#For questions, please contact maarten.renckens@artengar.com
#----

totalPages=60 #more pages means a slower, but nicer animation
pageWidth=1000
pageHeight=1000
baseShapeWidth=10
maxMovement = 100
marginX = 100
marginY = 100
extraX = 20
errorMargin = 1

#do some automatic calculations
Xstarting = 0-marginX

Ymiddle = pageHeight/2
Ymin = 0-100
Ymax = pageHeight + marginY
Y1 = Ymin +(Ymiddle+marginY)/3
Y2 = Ymin +(Ymiddle+marginY)/3*2
Y3 = Ymiddle +(Ymiddle+marginY)/3
Y4 = Ymiddle +(Ymiddle+marginY)/3*2

#incorporate how many movements there will be:
#=> four times the maxMovement (which is the total movement), divided by the totalPages:
movementDistance = maxMovement*4/totalPages
CurrentXdeltaCurve = -maxMovement
DeltaIncreasing = True


#Create the pages
for page in range(totalPages):
    print("Creating page %s" %page)
    newPage(width=pageWidth, height=pageHeight)
    frameDuration(1/20)
    #set a background
    fill(1)
    rect(0, 0, width(), height())
    
    #do some calculations before drawing curves in the shapes
    CurrentX = Xstarting
    if CurrentXdeltaCurve >= maxMovement:
        DeltaIncreasing = False
    print(CurrentXdeltaCurve)
    print(DeltaIncreasing)
    
    #draw the shapes
    for x in range(pageWidth+2*marginX+extraX*2):
        #Determine the coordinates of the shape
        fill(0)
        #Draw figure
        newPath()
        #determine and draw the shape
        moveTo((CurrentX, Ymin))
        curveTo((CurrentX-maxMovement+CurrentXdeltaCurve, Y1), (CurrentX-maxMovement+CurrentXdeltaCurve, Y1), (CurrentX, Ymiddle))
        curveTo((CurrentX-maxMovement+CurrentXdeltaCurve, Y3), (CurrentX-maxMovement+CurrentXdeltaCurve, Y4), (CurrentX, Ymax))
        lineTo((CurrentX+errorMargin+baseShapeWidth, Ymax))
        curveTo((CurrentX-maxMovement+CurrentXdeltaCurve+errorMargin+baseShapeWidth, Y4), (CurrentX-maxMovement+CurrentXdeltaCurve+errorMargin+baseShapeWidth, Y3), (CurrentX+errorMargin+baseShapeWidth, Ymax))
        curveTo((CurrentX-maxMovement+CurrentXdeltaCurve+errorMargin+baseShapeWidth, Y2), (CurrentX-maxMovement+CurrentXdeltaCurve+errorMargin+baseShapeWidth, Y1), (CurrentX+errorMargin+baseShapeWidth, Ymiddle))
        lineTo((CurrentX, Ymin))
        closePath()
        drawPath()
        #progress with the next shape
        CurrentX =+ x*baseShapeWidth*4
        
    if DeltaIncreasing == True:
        CurrentXdeltaCurve += movementDistance
    if DeltaIncreasing == False:
        CurrentXdeltaCurve -= movementDistance
    page+1

saveImage("~/Desktop/Snares.gif")
