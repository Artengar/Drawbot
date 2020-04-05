#stripes
#Free for use and modify, as long as a reference is provided.
#created by Maarten Renckens (maarten.renckens@artengar.com)

amountOfPages = 5
pageWidth = 1000
pageHeight = 1000
widthCorrector = 0.5

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
    path.moveTo((0,0))
    for item in range(len(progressList)):
        #progressList[item]*0.55229*sin(radians(item*90))
        path.curveTo( (1*progressList[item]*sin(radians(item*90))*widthCorrector, 1*progressList[item]*cos(radians(item*90)) ), (1*progressList[item]*sin(radians(item*90))*widthCorrector, 1*progressList[item]*cos(radians(item*90)) ), (1*progressList[item]*sin(radians(item*90))*widthCorrector, 1*progressList[item]*cos(radians(item*90)) ) )
    closePath()
    drawPath(path)

saveImage("~/Desktop/Spiral.gif")


