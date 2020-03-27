#Super Hexagon in Glyphs!

amountOfPages = 240 #360 degrees devided by the variable turnDirections is the minimum (except when only doing square animations)
canvasWidth=1000
canvasheight=1000
baseformRadius=50
baseformScale=[0,1]
turnDirection=-2
previousTurnAngle=0
sides=[True,12,0]#True means fixed, False means in a transition. The first number is the amount of sides, the second the amount of frames for the transition
amountofTransitionPages=20
beginningangle=45#just a random starting angle, to avoid stiffness

#colors
colA1=246/255#brightest, for possible animations
colA2=202/255
colA3=23/255
colB1=246/255#secondary background
colB2=172/255
colB3=23/255
colC1=136/255#First, darkest background
colC2=91/255
colC3=23/255
colD1=217/255#A fourth color is needed when five sides are set.#####This is not implemented yet, as current implementation anticipates on an amount of sides divided by 2
colD2=110/255
colD3=23/255

#Start making an animation
import math
import random

#Define the background
def baseform(sides, baseformScale):
    #Draw the triangular backgrounds (1 side = 1 background)
    for side in range(sides[1]):
        #when not in a transition, do:
        if sides[0] == True:
            singleAngle= 360/sides[1]
            angle = 360/sides[1]*side+beginningangle
        #transition: adjust the angle with 2 smaller shapes in-between
        elif sides[0] == False:
            singleAngle= 360/sides[1]
            #increasing with the angles for the next amount of angles
            increasingAngle = (360/(sides[1]-2)-singleAngle)/amountofTransitionPages*sides[2]
            singleAngle= 360/(sides[1])+increasingAngle
            angle = 360/sides[1]*side+beginningangle+increasingAngle*side
            print("Transition! The baseangle = %s,    while each angle is increased with %s    and has position %s" %(singleAngle, increasingAngle, angle))
        
        if sides[0] == False and side == sides[1]-1:
            angle=singleAngle/amountofTransitionPages*(amountofTransitionPages-sides[2])
            singleAngle= angle
            #work backwards for easy compatibility
            angle = 360+beginningangle-angle
            print("Custom angle! %s %s" %(singleAngle, angle))
        if sides[0] == False and side == sides[1]-2:
            angle=singleAngle/amountofTransitionPages*(amountofTransitionPages-sides[2])
            singleAngle= angle
            #work backwards for easy compatibility
            angle = 360+beginningangle-angle*2
            print("Custom angle! %s %s" %(singleAngle, angle))
        
        #draw
        strokeWidth(10)
        stroke(1)#colA1, colA2, colA3)
        fill(1)#colB1, colB2, colB3)
        #if five angles, then the fourth color is needed #not implemented at this time.
        if sides[1] %2 != 0 and side == sides[1]-1:
            fill(colD1, colD2, colD3)
        
        
        if side %2 == 0:
            newPath()
            moveTo((0,0))
            #First line
            #!!! a tan of 0, 90, 180 or 270 is infinite! counter that.
            if angle == 0 or angle == 360:
                lineTo((0,5000))
            elif 0 < angle < 90 or 360 < angle < 450:
                lineTo(( math.sin(math.radians(angle))*canvasWidth, math.cos(math.radians(angle))*canvasWidth ))
            elif angle == 90:
                lineTo((5000,0))
            elif 90 < angle < 180:
                lineTo(( math.sin(math.radians(angle))*canvasWidth, math.cos(math.radians(angle))*canvasWidth ))
            elif angle == 180:
                lineTo((0,-5000))
            elif 180 < angle < 270:
                lineTo(( math.sin(math.radians(angle))*canvasWidth, math.cos(math.radians(angle))*canvasWidth ))
            elif angle == 270:
                lineTo((-5000,0))
            elif 270 < angle < 360:
                lineTo(( math.sin(math.radians(angle))*canvasWidth, math.cos(math.radians(angle))*canvasWidth ))
            
            angle = angle + singleAngle
            #Second line
            #!!! a tan of 0, 90, 180 or 270 is infinite! counter that.
            if angle == 0 or angle == 360:
                lineTo((0,5000))
            elif 0 < angle < 90 or 360 < angle < 450:
                lineTo(( math.sin(math.radians(angle))*canvasWidth, math.cos(math.radians(angle))*canvasWidth ))
            elif angle == 90:
                lineTo((5000,0))
            elif 90 < angle < 180:
                lineTo(( math.sin(math.radians(angle))*canvasWidth, math.cos(math.radians(angle))*canvasWidth ))
            elif angle == 180:
                lineTo((0,-5000))
            elif 180 < angle < 270:
                lineTo(( math.sin(math.radians(angle))*canvasWidth, math.cos(math.radians(angle))*canvasWidth ))
            elif angle == 270:
                lineTo((-5000,0))
            elif 270 < angle < 360:
                lineTo(( math.sin(math.radians(angle))*canvasWidth, math.cos(math.radians(angle))*canvasWidth ))
            #Third line to close the triangular background
            lineTo((0,0))
            closePath()
            drawPath()

    #Create the center
    fill(0)#colC1, colC2, colC3)
    strokeWidth(10)
    stroke(1)#colA1, colA2, colA3)
    
    #form in the middle
    angle=beginningangle
    newPath()
    moveTo(( math.sin(math.radians(angle))*baseformRadius*baseformScale[1], math.cos(math.radians(angle))*baseformRadius*baseformScale[1] ))
    for side in range(sides[1]-1):
        side+=1
        singleAngle= 360/sides[1]
        angle = 360/sides[1]*side+beginningangle
        lineTo(( math.sin(math.radians(angle))*baseformRadius*baseformScale[1], math.cos(math.radians(angle))*baseformRadius*baseformScale[1] ))
    lineTo(( math.sin(math.radians(angle))*baseformRadius*baseformScale[1], math.cos(math.radians(angle))*baseformRadius*baseformScale[1] ))
    closePath()
    drawPath()





for page in range(amountOfPages):
    print("++++++++++ Starting page %s ++++++++++" %page)
    if page != 0:
        newPage()
    translate(canvasWidth/2, canvasheight/2)
    fill(0)#colC1, colC2, colC3)
    rect(-canvasWidth/2, -canvasheight/2, canvasWidth, canvasheight)
    
    if page !=0:
        previousTurnAngle+=turnDirection
    rotate(previousTurnAngle)
    
    #Possible events after a certain time (read: certain amount of pages)
    
    #scaling
    if page > 30:
        if baseformScale == [3,1]:
            baseformScale = [2,1.10]
        elif baseformScale == [2,1.075]:
            baseformScale = [2,1.20]
        elif baseformScale == [2,1.10]:
            baseformScale = [2,1.20]
        elif baseformScale == [2,1.20]:
            baseformScale = [3,1.10]
        elif baseformScale == [3,1.10]:
            baseformScale = [3,1]
        elif baseformScale == [0,1] or baseformScale == [1,1.05] or baseformScale == [1,1.10]:
            baseformScale = [2,1.075]
    elif page > 10:
        if baseformScale == [0,1]:
            baseformScale = [1,1.05]
        elif baseformScale == [1,1.05]:
            baseformScale = [1,1.10]
        elif baseformScale == [1,1.10]:
            baseformScale = [0,1.05]
        elif baseformScale == [0,1.05]:
            baseformScale = [0,1]
    
    #turning
    if page % 25 == 0 and page !=0:
        temp=random.randint(1,4)
        temp2=random.randint(-1,1)
        while temp2==0:
            temp2=random.randint(-1,1)
        turnDirection=(abs(turnDirection)+temp/3)*temp2
        print("new turnDirection = %s" %turnDirection)
    
    #prepare to lower the amount of sizes at a certain point
    if page % 50 == 0 and page !=0:
        print("!!!!!Allow change in angles!")
        if sides[1] > 4:
            sides=[False,sides[1],0]
    
    
    baseform(sides, baseformScale)
    
    
    #count the lowering of the amount of sizes
    if sides[0]==False:
        sides[2]=sides[2]+1
        if sides[2]==amountofTransitionPages:
            sides[0]=True
            sides[1]=sides[1]-2












#count how many steps would be necessary to turn the animation upright
if previousTurnAngle > 0:
    while previousTurnAngle > 359:
        previousTurnAngle-=360
if previousTurnAngle < 0:
    while previousTurnAngle < -359:
        previousTurnAngle+=360
if 0<= previousTurnAngle <=180 or -180>= previousTurnAngle>=-360:
    latestRotate=-2
    print("rotation = %s" %(previousTurnAngle))
    if previousTurnAngle > 0:
        page = int(previousTurnAngle/2)+1
    if previousTurnAngle < 0:
        page = abs(int( (-360-previousTurnAngle)/2))
if 180< previousTurnAngle <=360 or -180> previousTurnAngle >=0:
    latestRotate=2
    print("rotation = %s" %(previousTurnAngle))
    if previousTurnAngle > 0:
        page = int(previousTurnAngle/2)+1
    if previousTurnAngle < 0:
        page = abs(int( (-360-previousTurnAngle)/2))
    
    
print("amount of pages to finish: %s" %page)
#perform steps to set the animation upright
while page >= 0:
    print("++++++++++ Starting correcting page %s ++++++++++" %page)
    newPage()
    translate(canvasWidth/2, canvasheight/2)
    fill(0)#colC1, colC2, colC3)
    rect(-canvasWidth/2, -canvasheight/2, canvasWidth, canvasheight)
    
    if page !=0:
        previousTurnAngle+=latestRotate
    print(previousTurnAngle)
    rotate(previousTurnAngle)
    
    #scaling
    if baseformScale == [3,1]:
        baseformScale = [2,1.10]
    elif baseformScale == [2,1.075]:
        baseformScale = [2,1.20]
    elif baseformScale == [2,1.10]:
        baseformScale = [2,1.20]
    elif baseformScale == [2,1.20]:
        baseformScale = [3,1.10]
    elif baseformScale == [3,1.10]:
        baseformScale = [3,1]
    elif baseformScale == [0,1] or baseformScale == [1,1.05] or baseformScale == [1,1.10]:
        baseformScale = [2,1.075]
    
    baseform(sides, baseformScale)
    page -= 1






#Create some empty black pages
for page in range(30):
    print("++++++++++ Starting black page %s ++++++++++" %page)
    newPage()
    translate(canvasWidth/2, canvasheight/2)
    fill(0)#colC1, colC2, colC3)
    rect(-canvasWidth/2, -canvasheight/2, canvasWidth, canvasheight)


saveImage("~/Desktop/Super_Hexagon.gif")




