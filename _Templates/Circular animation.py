#This script prepares an animation in a circle by providing x & y values for a certain angle
#Free for use and modify, as long as a reference is provided.
#created by Maarten Renckens (maarten.renckens@artengar.com)

import math

#information for drawing the circle:
midpointX = 0
midpointY = 0
ratio = 1
amountOfFragments = 8
singleAngle = 360/amountOfFragments #If the amount of fragments is known, an angle can be calculated.

for fragmentNR in range(amountOfFragments):
    currentAngle = singleAngle*fragmentNR
    if currentAngle == 90:
        x=1
        y=0
    elif currentAngle == 180:
        x=0
        y=-1
    elif currentAngle == 270:
        x=-1
        y=0
    elif currentAngle == 0 or currentAngle == 360:
        x=0
        y=1
    else:
        x = (math.sin(math.radians(currentAngle)))
        y = (math.cos(math.radians(currentAngle)))
    print("Coordinates for the angle %s: x = %s, y = %s " %(currentAngle, x,y))



