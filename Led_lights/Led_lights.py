#stripes
#Free for use and modify, as long as a reference is provided.
#created by Maarten Renckens (maarten.renckens@artengar.com)

amountOfPages = 16
pageWidth = 1000
pageHeight = 1000

def horStroke(distance):
    rect(800-distance+10, 0+10, 80, 80)
    rect(900-distance+10, 0+10, 80, 80)
    rect(1000-distance+10, 0+10, 80, 80)
    rect(1100-distance+10, 0+10, 80, 80)

def vertStroke1(distance):
    rect(0+10, 700-distance+10, 80, 80)
    rect(0+10, 800-distance+10, 80, 80)
    rect(0+10, 900-distance+10, 80, 80)
    rect(0+10, 1000-distance+10, 80, 80)
def vertStroke2(distance):
    rect(-200+10, -600-distance+10, 80, 80)
    rect(-200+10, -700-distance+10, 80, 80)
    rect(-200+10, -800-distance+10, 80, 80)
    rect(-200+10, -900-distance+10, 80, 80)

for page in range(amountOfPages):
    page +=1
    print("==================== Starting page %s ====================" %page)
    if page != 0:
        newPage(pageWidth, pageHeight)
    elif page ==0:
        size(pageWidth, pageHeight)
    frameDuration(1/3)
    #set the origin in the middle of the page
    translate(pageWidth/2, pageHeight/2)
    #create a background
    fill(1)
    rect(-pageWidth/2,-pageHeight/2,pageWidth, pageHeight)
    
    #Create the background
    fill(0)
    for hor in range(int(pageWidth/100)):
        for vert in range(int(pageHeight/100)):
            rect(-500+hor*100+10, -500+vert*100+10, 80, 80)
    
    #do something on the pages
    fill(1, 0, 0)
    distance = 100*page
    print(distance)
    horStroke(distance)
    vertStroke1(distance)
    vertStroke2(-distance)

saveImage("~/Desktop/Empty_pages.mp4")


