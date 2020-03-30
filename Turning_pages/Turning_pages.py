#Turning pages animation
#Created by Maarten Renckens (maarten.renckens@artengar.com)

amountOfPages = 31#At this moment, changing this number requires some re-programming
amountOfPagesToSkip = 5#At this moment, changing this number requires some re-programming
pageWidth = 1000
pageHeight = 1000
maxYMovement = 130#This is not implemented yet

for page in range(amountOfPages):
    print("==================== Starting page %s ====================" %page)
    if page != 0:
        newPage()
    #set the origin in the middle of the page
    translate(500,500)
    #create a white background
    fill(0)
    rect(-pageWidth/2,-pageHeight/2,pageWidth, pageHeight)

    #create the paths with other colors
    fill(1, 0.5, 0.5)
    strokeWidth(3)
    stroke(0)
    #fixed path 1
    shape1fixed = BezierPath()
    shape1fixed.moveTo((-50, -250))
    shape1fixed.lineTo((-50, 0))
    shape1fixed.lineTo((-300, 340))
    shape1fixed.lineTo((-180, 340))
    shape1fixed.lineTo((50, 20))
    shape1fixed.lineTo((50, -250))
    #close the path
    shape1fixed.closePath()
    #draw the path
    drawPath(shape1fixed)

    #fixed path 2
    shape2fixed = BezierPath()
    shape2fixed.moveTo((8, 79))
    shape2fixed.lineTo((220, 340))
    shape2fixed.lineTo((300, 340))
    shape2fixed.lineTo((50, 22))
    #close the path
    shape2fixed.closePath()
    #draw the path
    drawPath(shape2fixed)
    
    #the first pages should not animate
    if page not in range(0,amountOfPagesToSkip):
        #animate the page of the 'book', on top of the fixed paths
        #Node1 should remain at the same position
        #Node2 should go from ((220, 340) to (-180, 340))
        Node2Movement = [[220,340], [-180,340]]
        #Node3 should go from ((300, 340) to (-300, 340))
        Node3Movement = [[300,340], [-300,340]]
        #Node4 should go from ((50, 22) to (-50, 0))
        Node4Movement = [[50,22], [-50,0]]
        
        #calculate movement Y #!!!!!!!!!!!!! should be more refined, but that is up to you ;)
        if page == 5 or page == 31:
            deltaY = 4
            print(deltaY)
        if page == 6 or page == 30:
            deltaY = 9
            print(deltaY)
        if page == 7 or page == 29:
            deltaY = 15
            print(deltaY)
        if page == 8 or page == 28:
            deltaY = 25
            print(deltaY)
        if page == 9 or page == 27:
            deltaY = 40
            print(deltaY)
        if page == 10 or page == 26:
            deltaY = 55
            print(deltaY)
        if page == 11 or page == 25:
            deltaY = 63
            print(deltaY)
        if page == 12 or page == 24:
            deltaY = 70
            print(deltaY)
        if page == 13 or page == 23:
            deltaY = 78
            print(deltaY)
        if page == 14 or page == 22:
            deltaY = 85
            print(deltaY)
        if page == 15 or page == 21:
            deltaY = 90
            print(deltaY)
        if page == 16 or page == 20:
            deltaY = 94
            print(deltaY)
        if page == 17 or page == 19:
            deltaY = 97
            print(deltaY)
        if page == 18:
            deltaY = 98
            print(deltaY)
        #modifyer
        deltaY = deltaY/4*3
        
        #PageShape
        PageShape = BezierPath()
        PageShape.moveTo(( 8, 79 ))#keep the beginning point
        PageShape.lineTo(( (Node2Movement[0][0]-((abs(Node2Movement[0][0])+abs(Node2Movement[1][0]))/(amountOfPages-amountOfPagesToSkip)*(page-amountOfPagesToSkip))), (Node2Movement[0][1])+deltaY ))
        PageShape.lineTo(( (Node3Movement[0][0]-((abs(Node3Movement[0][0])+abs(Node3Movement[1][0]))/(amountOfPages-amountOfPagesToSkip)*(page-amountOfPagesToSkip))), (Node3Movement[0][1])+deltaY ))
        PageShape.lineTo(( (Node4Movement[0][0]-((abs(Node4Movement[0][0])+abs(Node4Movement[1][0]))/(amountOfPages-amountOfPagesToSkip)*(page-amountOfPagesToSkip))), (Node4Movement[0][1])+deltaY/2 ))
        #close the path
        PageShape.closePath()
        #draw the path
        drawPath(PageShape)

saveImage("~/Desktop/Turning_pages.gif")







