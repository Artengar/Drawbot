#stripes
#Free for use and modify, as long as a reference is provided.
#created by Maarten Renckens (maarten.renckens@artengar.com)

amountOfPages = 1
pageWidth = 1000
pageHeight = 1000
widthCorrector = 1
midpointX = 0
midpointY = 0

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
    frameDuration(1/20)
    #set the origin in the middle of the page
    translate(pageWidth/2, pageHeight/2)
    #create a background
    fill(1)
    rect(-pageWidth/2,-pageHeight/2,pageWidth, pageHeight)
    
    #do something on the pages
    amountOfSteps = 20
    progressList = fibonacci(amountOfSteps)
    
    stroke(0)
    path = BezierPath()
    path.moveTo((midpointX,midpointY))
    for item in range(len(progressList)):
        #STRUCTURE:
        #First, detect if the  hor/vert!!!!!!!!!
        #reverse all values, to get a nine:    -
        #the distance in Fibonacci:    progressList[item]
        #the distance for a node:    *0.55229
        ###only if necessary (hor/vert)
        #Getting if positive/negative:    sin(radians(item*90))
        if item ==0:
            print("case0")
            
        elif sin(radians((item-1)*90)) == 0 or cos(radians((item-1)*90)) == 1:
            
            path.curveTo(
                (midpointX+progressList[(item-1)]*0.55229, midpointY+progressList[(item-1)]),
                (midpointX+progressList[(item-1)], midpointY+progressList[(item-1)]*0.55229),
                (midpointX+progressList[(item-1)], midpointY) )
            
        elif sin(radians((item-1)*90)) == 1 or cos(radians((item-1)*90)) == 0:
            path.curveTo(
                (midpointX+progressList[(item-1)], midpointY-progressList[(item-1)]*0.55229),
                (midpointX+progressList[(item-1)]*0.55229, midpointY-progressList[(item-1)]),
                (midpointX, midpointY-progressList[(item-1)]) )
            
        elif sin(radians((item-1)*90)) == 0 or cos(radians((item-1)*90)) == -1:
            path.curveTo(
                (-midpointX-progressList[(item-1)]*0.55229, midpointY-progressList[(item-1)]),
                (-midpointX-progressList[(item-1)], midpointY-progressList[(item-1)]*0.55229),
                (-midpointX-progressList[(item-1)], midpointY) )
            
        elif sin(radians((item-1)*90)) == -1 or cos(radians((item-1)*90)) == 0:
            path.curveTo(
                (midpointX-progressList[(item-1)], midpointY+progressList[(item-1)]*0.55229),
                (midpointX-progressList[(item-1)]*0.55229, midpointY+progressList[(item-1)]),
                (midpointX, midpointY+progressList[(item-1)]) )
            
#path.curveTo( (100*0.55229, 100), (100, 100*0.55229), (100,0) )
#path.curveTo( (100, -100*0.55229), (100*0.55229, -100), (0,-100) )
#path.curveTo( (-100*0.55229, -100), (-100, -100*0.55229), (-100,0) )
#path.curveTo( (-100, 100*0.55229), (-100*0.55229, 100), (0,100) )            
            
    closePath()
    drawPath(path)

saveImage("~/Desktop/Spiral.gif")


