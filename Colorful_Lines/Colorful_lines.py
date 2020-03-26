#Colorful lines

#User Parameters
pageHeight=1000.0
pageWidth=1000.0
strokeWidth=100.0
spaceBetweenStrokes = 10
Margin = 500 #go slightly off the canvas to avoid white spaces
Range = pageWidth+Margin*2 #the total width over which the animation will go
XDistance = Range/7
strokeDelta = 250 #How much the strokes will rise
AmountofPages = 50

for page in range(AmountofPages):
    frameDuration(1/10)
    if page != 0:
        newPage()
    
    fill(0.5)
    rect(0,0,1000,1000)
    
    #Get everything for the colors
    colorlocation=pageWidth/AmountofPages*page
    print(colorlocation)
    #(237/255, 164/255, 175/255), (235/255, 228/255, 160/255), (235/255, 228/255, 160/255)

    #Draw the strokes (not with a line but with a shape!)
    for y in range(int(Range*2/(strokeWidth+spaceBetweenStrokes)+4)):
        delta = y*(strokeWidth+spaceBetweenStrokes)
        
        #set color
        if y % 2 == 0:
            #Black and white settings
            linearGradient(startPoint=(-1000+colorlocation,0), endPoint=(pageWidth+colorlocation,0), colors=[(1, 1, 1), (0, 0, 0), (1, 1, 1), (1, 1, 1), (0, 0, 0), (1, 1, 1), (1, 1, 1)], locations=[0, 0.1667, 0.3334, 0.5, 0.6667, 0.8334, 1])
            #Color settings
            #linearGradient(startPoint=(-1000+colorlocation,0), endPoint=(pageWidth+colorlocation,0), colors=[ (235/255, 228/255, 160/255), (237/255, 164/255, 175/255), (235/255, 228/255, 160/255),  (235/255, 228/255, 160/255), (237/255, 164/255, 175/255), (235/255, 228/255, 160/255),  (235/255, 228/255, 160/255)], locations=[0, 0.1667, 0.3334, 0.5, 0.6667, 0.8334, 1])
        else:
            #Black and white settings
            linearGradient(startPoint=(-1000+colorlocation,0), endPoint=(pageWidth+colorlocation,0), colors=[(0, 0, 0), (1, 1, 1), (1, 1, 1), (0, 0, 0), (1, 1, 1), (1, 1, 1), (0, 0, 0)], locations=[0, 0.1667, 0.3334, 0.5, 0.6667, 0.8334, 1])
            #Color settings
            #linearGradient(startPoint=(-1000+colorlocation,0), endPoint=(pageWidth+colorlocation,0), colors=[(237/255, 164/255, 175/255), (235/255, 228/255, 160/255),  (235/255, 228/255, 160/255), (237/255, 164/255, 175/255), (235/255, 228/255, 160/255),  (235/255, 228/255, 160/255), (237/255, 164/255, 175/255)], locations=[0, 0.1667, 0.3334, 0.5, 0.6667, 0.8334, 1])
        
        #Draw figure
        newPath()
        #determine and draw the shape
        moveTo((-Margin+XDistance*0, -Margin+delta))
        #lower part
        lineTo((-Margin+XDistance*1, -Margin+delta+strokeDelta))
        lineTo((-Margin+XDistance*2, -Margin+delta))
        lineTo((-Margin+XDistance*3, -Margin+delta+strokeDelta))
        lineTo((-Margin+XDistance*4, -Margin+delta))
        lineTo((-Margin+XDistance*5, -Margin+delta+strokeDelta))
        lineTo((-Margin+XDistance*6, -Margin+delta))
        lineTo((-Margin+XDistance*7, -Margin+delta+strokeDelta))
        #straight line up
        lineTo((-Margin+XDistance*7, -Margin+delta+strokeWidth))
        #upper part
        lineTo((-Margin+XDistance*6, -Margin+delta+strokeWidth))
        lineTo((-Margin+XDistance*5, -Margin+delta+strokeWidth+strokeDelta))
        lineTo((-Margin+XDistance*4, -Margin+delta+strokeWidth))
        lineTo((-Margin+XDistance*3, -Margin+delta+strokeWidth+strokeDelta))
        lineTo((-Margin+XDistance*2, -Margin+delta+strokeWidth))
        lineTo((-Margin+XDistance*1, -Margin+delta+strokeWidth+strokeDelta))
        lineTo((-Margin+XDistance*0, -Margin+delta+strokeWidth))
        #straight line down
        lineTo((-Margin+XDistance*0, -Margin+delta))
        #close
        closePath()
        drawPath()

saveImage("~/Desktop/colorful_lines.gif")

