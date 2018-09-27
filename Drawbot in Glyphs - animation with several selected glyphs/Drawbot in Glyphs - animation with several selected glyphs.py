#NOTE: this script is written for Drawbot within Glyphs!
#NOTE: this script is suited for Glyphs animations trough different selected glyphs.
# For questions, contact Maarten Renckens: maarten.renckens@artengar.com

from GlyphsApp import *

# General document information
ActiveFont = Glyphs.font
selectedLayers = ActiveFont.selectedLayers
widestFrame = 0

#provide general information in the log:
print('For the font "%s":')%ActiveFont.familyName

#prepare the canvas:
#get the widest frame:
for thisLayer in selectedLayers:
    if thisLayer.width > widestFrame:
        widestFrame = thisLayer.width
print "The widest frame I found was %s"%widestFrame
#determine the canvas size:
pageHeight = ActiveFont.upm + 400
pageWidth = widestFrame + 400
canvasWidth = 0
canvasHeight = 0

#Decompose the components
for thisLayer in selectedLayers:
    newPage(pageWidth, pageHeight)
    fill(0, 0, 0, 1)
    frameDuration(1/6)
    #width and heigth only works after a page is created.
    canvasWidth = width()
    canvasHeight = height()
    translate(canvasWidth/2-500, canvasHeight/2-300)
    drawPath(thisLayer.bezierPath)

saveToPath = "~/Desktop/" + ActiveFont.familyName + ".gif"
saveImage(saveToPath)
print("ready!")

