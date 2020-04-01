#Empty pages template
#Free for use and modify, as long as a reference is provided.
#created by Maarten Renckens (maarten.renckens@artengar.com)

amountOfPages = 5
pageWidth = 1000
pageHeight = 1000
radius = 10
distance = 50
scale = [1, 1.5, 2, 1.5, 1]
specialScale = [1, 2, 3, 2, 1]


for page in range(amountOfPages-1):
    print("==================== Starting page %s ====================" %page)
    if page != 0:
        newPage(pageWidth, pageHeight)
    #set the origin in the middle of the page
    translate(500,500)
    #create a background
    fill(1)
    rect(-pageWidth/2,-pageHeight/2,pageWidth, pageHeight)
    
    usedScale = scale[page]
    usedSpecialScale = specialScale[page]
    
    fill(0)
    for x in range(int(pageWidth/distance)+1):
        for y in range(int(pageHeight/distance)+1):
            oval(-500+x*distance-(radius*usedScale), -500+y*distance-(radius*usedScale), (radius*usedScale)*2, (radius*usedScale)*2)

    for special in [[10,5], [10,6], [10,7], [10,8], [10,9], [10,10], [10,11], [10,12], [10,13], [10,14], [10,15], [9,14]]:
        oval(-500+special[0]*distance-(radius*usedSpecialScale), -500+special[1]*distance-(radius*usedSpecialScale), (radius*usedSpecialScale)*2, (radius*usedSpecialScale)*2)

saveImage("~/Desktop/bulbs.gif")



