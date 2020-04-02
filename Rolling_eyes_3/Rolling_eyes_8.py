#Rolling eyes on the number 8.
#Free for use and modify, as long as a reference is provided.
#created by Maarten Renckens (maarten.renckens@artengar.com)

amountOfPages = 16
pageWidth = 1000
pageHeight = 1000
#information for drawing the circle:
midpointX = 0
midpointY = 0
ratio = 1
singleAngle = 360/amountOfPages

#Some default functions
import math

#Create the animation
def drawCircle(page, singleAngle, amountOfCircling, midpointX, midpointY, ratio, color):
    fill(color)
    #Get the amount of movement
    currentAngle = singleAngle*page-90
    if currentAngle == 90:
        correctX=1
        correctY=0
    elif currentAngle == 180:
        correctX=0
        correctY=-1
    elif currentAngle == 270 or currentAngle == -90 :
        correctX=-1
        correctY=0
    elif currentAngle == 0 or currentAngle == 360:
        correctX=0
        correctY=1
    else:
        correctX = (math.sin(math.radians(currentAngle)))
        correctY = (math.cos(math.radians(currentAngle)))
    print("Coordinates for the angle %s: x = %s, y = %s " %(currentAngle, correctX,correctY))
    print(midpointX+correctX-ratio)
    oval(midpointX+(correctX*amountOfCircling)-ratio,midpointY+(correctY*amountOfCircling)-ratio,ratio*2,ratio*2)
    


for page in range(amountOfPages):
    print("==================== Starting page %s ====================" %page)
    if page != 0:
        newPage(pageWidth, pageHeight)
    elif page ==0:
        size(pageWidth, pageHeight)
    #set the origin in the middle of the page
    translate(pageWidth/2, pageHeight/2)
    #create a background
    fill(1)
    rect(-pageWidth/2,-pageHeight/2,pageWidth, pageHeight)
    
    #first circle #black
    midpointY=200
    ratio=160
    drawCircle(page, singleAngle, 0, midpointX, midpointY, ratio, 0)
    #second circle #black
    midpointY=-100
    ratio=230
    drawCircle(page, singleAngle, 0, midpointX, midpointY, ratio, 0)
    #third circle #white
    midpointY=200
    ratio=100
    drawCircle(-page, singleAngle, 60, midpointX, midpointY, ratio, 1)
    #fourth circle #white
    midpointY=-100
    ratio=160
    drawCircle(page, singleAngle, 70, midpointX, midpointY, ratio, 1)
    

saveImage("~/Desktop/Rolling_eyes_8.gif")


