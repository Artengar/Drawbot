#Empty pages template
#Free for use and modify, as long as a reference is provided.
#created by Maarten Renckens (maarten.renckens@artengar.com)

amountOfPages = 5
pageWidth = 1000
pageHeight = 1000


for page in range(amountOfPages):
    print("==================== Starting page %s ====================" %page)
    if page != 0:
        newPage()
    #set the origin in the middle of the page
    translate(500,500)
    #create a background
    fill(1)
    rect(-pageWidth/2,-pageHeight/2,pageWidth, pageHeight)

saveImage("~/Desktop/Empty_pages.gif")


