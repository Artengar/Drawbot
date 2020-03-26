#Letter Disco!

import random

def drawform(x):
    fill(0)
    rect(0,0,1000,1000)
    path=BezierPath()
    fontList = ["Georgia", "Verdana", "Trebuchet MS"]
    path.text("V", font=fontList[random.randint(0, 2)],  fontSize=750, offset=(500,200), align="center")
    for contour in path:
        for node in contour:
            fill(random.randint(0, 10)/10, random.randint(0, 10)/10, random.randint(0, 10)/10, random.randint(0, 10)/10)
            x=random.randint(0, 50)
            y=random.randint(0, 50)
            oval((node[0][0]-x/2), (node[0][1]-y/2), x, y)

drawform(0)
for i in range(40):
    newPage()
    frameDuration(1/10)
    drawform(i*10+1)

saveImage("~/Desktop/Letter_Disco.mp4")