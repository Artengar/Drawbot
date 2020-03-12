#NOTE: this script is written for Drawbot within Glyphs!
# For questions, contact Maarten Renckens: maarten.renckens@artengar.com

#Define the desired values:
duration = 1/10 #in seconds
pageHeight = 1000
pageWidth = 1000

#Get other information
from GlyphsApp import *
ActiveFont = Glyphs.fonts[0]
ActiveLetters = Glyphs.fonts[0].selectedLayers.copy()


def renderAnimation(letter):
    newDrawing()
    size(pageHeight, pageWidth)
    amountOfMovements = (len(letter.paths)-1)/3
    
    page = 1
    while page <= amountOfMovements:
        print("Creating page %s"%page)
        #place a background
        fill(1)
        rect(0,-300,1500,1500)
        
        #Draw the paths
        fill(0)
        for thisPath in letter.paths:
            print(thisPath)
            path = BezierPath()
            path = thisPath
            drawPath(path)
        
        frameDuration(duration)
        if page < amountOfMovements:
            newPage(pageWidth, pageHeight)
        
        page +=1


for letter in ActiveLetters:
    renderAnimation(letter)
    PathToSaveTo = "~/Desktop/" + ActiveFont.familyName + "_" + letter.parent.name + "_" + ".mp4"
    saveImage(PathToSaveTo)




