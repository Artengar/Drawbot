#This script creates a tunnel vision

centerX = 500
centerY = 500
startingDiameter = 10
DistanceBetweenCircles = 30
amountOfFrames = 10
fill(1)
rect(0,0,1000,1000)
fill(None)
strokeWidth(1)
stroke(0)

for x in range(amountOfFrames):
    currentDiameter = startingDiameter + (DistanceBetweenCircles/amountOfFrames*x)
    while currentDiameter < startingDiameter + DistanceBetweenCircles:
        activeDiameter = currentDiameter
        #draw several circles with different diameters
        while activeDiameter < 1500:
            oval(centerX-activeDiameter/2, centerY-activeDiameter/2, activeDiameter, activeDiameter)
            activeDiameter += DistanceBetweenCircles
        currentDiameter+=(DistanceBetweenCircles/amountOfFrames)
        print(currentDiameter)
    if x in range(amountOfFrames-1):
        newPage()
        fill(1)
        rect(0,0,1000,1000)
        fill(None)
        strokeWidth(1)
        stroke(0)

saveImage("~/Desktop/Tunnel_Vision.gif")
