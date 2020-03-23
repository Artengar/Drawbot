#NOTE: this script is written for Drawbot within Glyphs!
#NOTE: this script is suited for Glyphs animations on OpenType variations trough pre-defined instances. The design has to be adapted in order to create a loop.
# For questions, contact Maarten Renckens: maarten.renckens@artengar.com

from GlyphsApp import *
import objc
GSInstance = objc.lookUpClass("GSInstance")
GSInterpolationFontProxy = objc.lookUpClass("GSInterpolationFontProxy")

#https://forum.glyphsapp.com/t/drawing-instances-with-drawbot-plugin/5189/6

# General document information
ActiveFont = Glyphs.font
selectedLayers = ActiveFont.selectedLayers
pages = len(ActiveFont.instances)
pageHeight = 1000
pageWidth = 1000
canvasWidth = 0
canvasHeight = 0

#provide general information in the log:
print('For the font "%s" I can draw:')%ActiveFont.familyName

#Decompose the components
for thisLayer in selectedLayers:
    currentGlyph = thisLayer.parent
    for master in ActiveFont.masters:
        if len(ActiveFont.glyphs[currentGlyph.name].layers[master.id].components) > 0:
         ActiveFont.glyphs[currentGlyph.name].layers[master.id].decomposeComponents()

#Create the different frames
def renderAnimation():
    page=0
    for instance in ActiveFont.instances:
        page+=1
        if page == pages:
            break
        print("processing page %s")%page
        newPage(pageWidth, pageHeight)
        
        fill(1)
        rect(-10,-10,1020,1020)
        fill(0, 0, 0, 1)
        #=======
        frameDuration(1/15)
        #width and heigth only works after a page is created.
        canvasWidth = width()
        canvasHeight = height()
        translate(canvasWidth/2-500, canvasHeight/2-300)
    
        
        #place a background
        fill(1)
        rect(0,-200,1000,1000)
        
        fill(0, 0, 0, 1)
        instanceFont = instance.interpolatedFontProxy
        for thisLayer in selectedLayers:
            instanceGlyph = instanceFont.glyphForName_(thisLayer.parent.name)
            instanceLayer = instanceGlyph.layers[instanceFont.fontMasterID()]
            drawPath(instanceLayer.bezierPath)

renderAnimation()

saveToPath = "~/Desktop/" + ActiveFont.familyName + ".gif"
saveImage(saveToPath)
print("ready!")
