#----
#Maarten Renckens's Snares animation
#Python script for Drawbot
#For questions, please contact maarten.renckens@artengar.com
#----

#User settings
#DO NOTE that not all of them are tested nor work perfect yet.
totalPages=200 #more pages means a slower, but nicer animation
pageWidth=1000
pageHeight=1000
baseShapeWidth=10
maxMovement = 100
marginX = 200
marginY = 100
extraX = 40
errorMargin = 1

#do some automatic calculations
Xstarting = -marginX

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
    translate(-100,0)#EMERGENCY SOLUTION TO Xstarting that is not working for some reason
    frameDuration(1/15)
    #set a background
    fill(1)
    rect(0, 0, width(), height())
    
    #do some calculations before drawing curves in the shapes
    CurrentX = Xstarting #Xstarting that is not working for some reason
    if CurrentXdeltaCurve >= maxMovement:
        DeltaIncreasing = False
    print(CurrentX)
    print(CurrentXdeltaCurve)
    
    #draw the shapes
    currentColor=0
    for x in range(int((pageWidth+2*(marginX+extraX))/baseShapeWidth)+1):
        #Draw figure
        newPath()
        #determine and draw the shape
        moveTo((CurrentX, Ymin))
        curveTo((CurrentX+maxMovement/2-CurrentXdeltaCurve, Y1), (CurrentX+maxMovement/2-CurrentXdeltaCurve, Y2), (CurrentX, Ymiddle))
        curveTo((CurrentX-maxMovement/2+CurrentXdeltaCurve, Y3), (CurrentX-maxMovement/2+CurrentXdeltaCurve, Y4), (CurrentX, Ymax))
        lineTo((CurrentX+errorMargin+baseShapeWidth, Ymax))
        curveTo((CurrentX-maxMovement/2+CurrentXdeltaCurve+errorMargin+baseShapeWidth, Y4), (CurrentX-maxMovement/2+CurrentXdeltaCurve+errorMargin+baseShapeWidth, Y3), (CurrentX+errorMargin+baseShapeWidth, Ymiddle))
        curveTo((CurrentX+maxMovement/2-CurrentXdeltaCurve+errorMargin+baseShapeWidth, Y2), (CurrentX+maxMovement/2-CurrentXdeltaCurve+errorMargin+baseShapeWidth, Y1), (CurrentX+errorMargin+baseShapeWidth, Ymin))
        lineTo((CurrentX, Ymin))
        closePath()
        drawPath()
        #progress with the next shape
        CurrentX =+ x*(baseShapeWidth)
        if currentColor == 0:
            fill(1)
            currentColor=1
        elif currentColor == 1:
            fill(51/255, 246/255, 255/255)
            currentColor=2
        elif currentColor == 2:
            fill(0)
            currentColor=0
            
        
    if DeltaIncreasing == True:
        CurrentXdeltaCurve += movementDistance
    if DeltaIncreasing == False:
        CurrentXdeltaCurve -= movementDistance
    page+1

saveImage("~/Desktop/Snares_continuous.gif")
