#stripes
#Free for use and modify, as long as a reference is provided.
#created by Maarten Renckens (maarten.renckens@artengar.com)

amountOfPages = 10
pageWidth = 1000
pageHeight = 1000
correctorWidth = -0.4
correctorHeight = -1
midpointX = 0
midpointY = 100
scaleList = [1-0.06, 1-0.12, 1-0.18, 1-0.24, 1-0.30, 1-0.24, 1-0.34, 1-0.44, 1-0.54, 1-0.64] #Only added for this specific animation

def fibonacci(amountOfSteps):
    currentNumber = 1
    previousNumber = 1
    olderNumber = 1
    progressList = []
    for step in range(amountOfSteps):
        if step != 0 and step != 1:
            olderNumber = previousNumber
            previousNumber = currentNumber
            currentNumber += olderNumber
        progressList.append(currentNumber)
    return progressList

#Start the code
for page in range(amountOfPages):
    print("==================== Starting page %s ====================" %page)
    if page != 0:
        newPage(pageWidth, pageHeight)
    elif page ==0:
        size(pageWidth, pageHeight)
    #Set the time of each page (frame)
    frameDuration(1/10)
    #set the origin in the middle of the page
    translate(pageWidth/2, pageHeight/2)
    #create a background
    radialGradient(startPoint=(0,100), endPoint=(0,400), colors=[(0.05, 0.05, 0.05), (1, 0, 0.8)], locations=[0,0.5], startRadius=0, endRadius=1720)
    rect(-pageWidth,-pageHeight,pageWidth*2, pageHeight*2)
    
    #do something on the pages
    amountOfSteps = 60
    progressList = fibonacci(amountOfSteps)
    
    #Draw Fibonacci
    stroke(0)
    strokeWidth(10)
    path = BezierPath()
    path.moveTo((midpointX,midpointY))
    #reset the default values for each page
    midpointX = 0
    midpointY = 100
    segmentStartPointX = midpointX
    segmentStartPointY = midpointY
    correctorWidth = -0.4
    correctorHeight = -1
    #Calculate the actual form
    #scale = 1-0.021*page #######THIS WOULD BE THE NORMAL CODE FOR 25 PAGES
    scale = scaleList[page] ########CUSTOM ADDED FOR THIS SPECIFIC ANIMATION
    for item in range(len(progressList)):
        if item !=0:
            correctorWidth = correctorWidth/1.35
            correctorHeight = correctorHeight/1.35
        #STRUCTURE:
        #Getting if positive/negative:    via sin(radians(item*90))
        #reverse all values, to get a nine:    negative correctors
        #the distance in Fibonacci:    progressList[item]
        #the distance for a node:    *0.55229
        ###only if necessary (hor/vert)
        if item ==0:
            print()
            
        elif sin(radians(item*90)) == 0 or cos(radians(item*90)) == 1:
            
            path.curveTo(
                (segmentStartPointX+progressList[item]*0.55229*correctorWidth*scale, segmentStartPointY),
                (segmentStartPointX+progressList[item]*correctorWidth*scale, segmentStartPointY-progressList[item]*0.44771*correctorHeight*scale),
                (segmentStartPointX+progressList[item]*correctorWidth*scale, segmentStartPointY-progressList[item]*correctorHeight*scale) )
            
            segmentStartPointX=segmentStartPointX+progressList[item]*correctorWidth*scale
            segmentStartPointY=segmentStartPointY-progressList[item]*correctorHeight*scale
            
        elif sin(radians(item*90)) == 1 or cos(radians(item*90)) == 0:
            path.curveTo(
                (segmentStartPointX, segmentStartPointY-progressList[item]*0.55229*correctorHeight*scale),
                (segmentStartPointX-progressList[item]*0.44771*correctorWidth*scale, segmentStartPointY-progressList[item]*correctorHeight*scale),
                (segmentStartPointX-progressList[item]*correctorWidth*scale, segmentStartPointY-progressList[item]*correctorHeight*scale) )
            
            segmentStartPointX=segmentStartPointX-progressList[item]*correctorWidth*scale
            segmentStartPointY=segmentStartPointY-progressList[item]*correctorHeight*scale
            
        elif sin(radians(item*90)) == 0 or cos(radians(item*90)) == -1:
            path.curveTo(
                (segmentStartPointX-progressList[item]*0.55229*correctorWidth*scale, segmentStartPointY),
                (segmentStartPointX-progressList[item]*correctorWidth*scale, segmentStartPointY+progressList[item]*0.44771*correctorHeight*scale),
                (segmentStartPointX-progressList[item]*correctorWidth*scale, segmentStartPointY+progressList[item]*correctorHeight*scale) )
            
            segmentStartPointX=segmentStartPointX-progressList[item]*correctorWidth*scale
            segmentStartPointY=segmentStartPointY+progressList[item]*correctorHeight*scale
            
        elif sin(radians(item*90)) == -1 or cos(radians(item*90)) == 0:
            path.curveTo(
                (segmentStartPointX, segmentStartPointY+progressList[item]*0.55229*correctorHeight*scale),
                (segmentStartPointX+progressList[item]*0.44771*correctorWidth*scale, segmentStartPointY+progressList[item]*correctorHeight*scale),
                (segmentStartPointX+progressList[item]*correctorWidth*scale, segmentStartPointY+progressList[item]*correctorHeight*scale) )
            
            segmentStartPointX=segmentStartPointX+progressList[item]*correctorWidth*scale
            segmentStartPointY=segmentStartPointY+progressList[item]*correctorHeight*scale       
    closePath()
    drawPath(path)

saveImage("~/Desktop/Spiral.gif")


