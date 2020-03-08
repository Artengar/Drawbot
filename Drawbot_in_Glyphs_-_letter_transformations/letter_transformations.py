#NOTE: this script is written for Drawbot within Glyphs!
# For questions, contact Maarten Renckens: maarten.renckens@artengar.com

#Define the desired values:


amountOfMovements = 40
duration = 1/10 #in seconds
pageHeight = 1000
pageWidth = 1000
canvasWidth = 0
canvasHeight = 0
diameterNodes = 10

from GlyphsApp import *
import random
random.seed()
ActiveFont = Glyphs.fonts[0]
ActiveLetters = Glyphs.fonts[0].selectedLayers.copy()

def renderAnimation(letter):
    newDrawing()
    size(pageHeight, pageWidth)
    
    page = 1
    while page <= amountOfMovements:
        print("Creating page %s"%page)
        translate(0, 250)
        
        #place a background
        fill(1)
        rect(0,-300,1500,1500)
        
        
        #Draw the paths
        fill(0)
        stroke(0)
        
        for thisPath in letter.paths:
            ListOfNodes = []
            for thisNode in thisPath.nodes:
                ListOfNodes += [[thisNode.x, thisNode.y]]
            
            item = 0
            while item < len(ListOfNodes):
                randomX = random.randint(-20, 20)
                randomY = random.randint(-20, 20)
                if item == len(ListOfNodes)-1:
                    line((ListOfNodes[item][0]+randomX, ListOfNodes[item][1]+randomY), (ListOfNodes[0][0]+randomX, ListOfNodes[0][1]+randomY))
                else:
                    line((ListOfNodes[item][0]+randomX, ListOfNodes[item][1]+randomY), (ListOfNodes[item+1][0]+randomX, ListOfNodes[item+1][1]+randomY))
            
                item += 1
        
        
        frameDuration(duration)
        if page < amountOfMovements:
            newPage(pageWidth, pageHeight)
            
        page +=1

for letter in ActiveLetters:
    renderAnimation(letter)
    PathToSaveTo = "~/Desktop/" + ActiveFont.familyName + "_" + letter.parent.name + "_" + ".mp4"
    saveImage(PathToSaveTo)




