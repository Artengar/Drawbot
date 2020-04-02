#Rolling eyes on the number 3.
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
import random

#Create the animation
def drawCircle(page, singleAngle, amountOfCircling, midpointX, midpointY, ratio, color):
    fill(color)
    #Get the amount of movement
    currentAngle = singleAngle*page-90
    correctX=random.randint(0,30)
    correctY=random.randint(0,30)
    oval(midpointX+(correctX)-ratio,midpointY+(correctY)-ratio,ratio*2,ratio*2)
    


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
    midpointX=0
    midpointY=200
    ratio=160
    drawCircle(page, singleAngle, 0, midpointX, midpointY, ratio, 0)
    #second circle #black
    midpointX=0
    midpointY=-100
    ratio=230
    drawCircle(page, singleAngle, 0, midpointX, midpointY, ratio, 0)
    #third circle #white
    midpointY=200
    midpointX=-50
    ratio=150
    drawCircle(page, singleAngle, 40, midpointX, midpointY, ratio, 1)
    #fourth circle #white
    midpointY=-100
    midpointX=-60
    ratio=230
    drawCircle(page, singleAngle, 50, midpointX, midpointY, ratio, 1)
    

saveImage("~/Desktop/Rolling_eyes_3.gif")


