#NOTE: this script is written for Drawbot within Glyphs!
#NOTE: this script creates a rainy animation from certain glyphs.
# For questions, contact Maarten Renckens: maarten.renckens@artengar.com

#DON'T USE THIS SCRIPT ON PRODUCTION FONTS, AS IT MESSES WITH THE GLYPHS!

from GlyphsApp import *
import random
ActiveFont = Glyphs.font

#Set all parameters
pages = 20
page = 0
pageWidth = 1000
pageHeight = 1000
lettersToDo = ['A', 'B', 'C']

#parameters for each letter
drop1LetterA = BezierPath(ActiveFont.glyphs['A'].layers['Text Regular'].bezierPath)
drop1ScaleSpeed=50
drop1DrawingStartHeight=1400
drop1DrawingHeight=0
drop1DistanceBetween=175
drop1LetterA.scale(0.1)
horizontalDistance1=random.randint(0,pageWidth-50)
drop1LetterA.translate(horizontalDistance1,drop1DrawingStartHeight)#move horizontally to the middle
drop1DrawingHeight = drop1DrawingStartHeight

#parameters for each letter
drop2LetterB = BezierPath(ActiveFont.glyphs['B'].layers['Text Regular'].bezierPath)
drop2ScaleSpeed=40
drop2DrawingStartHeight=1400
drop2DrawingHeight=0
drop2DistanceBetween=350
drop2LetterB.scale(0.25)
horizontalDistance2=random.randint(0,pageWidth-50)
drop2LetterB.translate(horizontalDistance2,drop2DrawingStartHeight)#move horizontally to the middle
drop2DrawingHeight = drop1DrawingStartHeight

#parameters for each letter
drop3LetterC = BezierPath(ActiveFont.glyphs['C'].layers['Text Regular'].bezierPath)
drop3ScaleSpeed=50
drop3DrawingStartHeight=1400
drop3DrawingHeight=0
drop3DistanceBetween=200
drop3LetterC.scale(0.35)
horizontalDistance3=random.randint(0,pageWidth-50)
drop3LetterC.translate(horizontalDistance3,drop3DrawingStartHeight)#move horizontally to the middle
drop3DrawingHeight = drop3DrawingStartHeight

#parameters for each letter
drop4LetterD = BezierPath(ActiveFont.glyphs['D'].layers['Text Regular'].bezierPath)
drop4ScaleSpeed=50
drop4DrawingStartHeight=1400
drop4DrawingHeight=0
drop4DistanceBetween=40
drop4LetterD.scale(0.05)
horizontalDistance4=random.randint(0,pageWidth-50)
drop4LetterD.translate(horizontalDistance4,drop4DrawingStartHeight)#move horizontally to the middle
drop4DrawingHeight = drop4DrawingStartHeight

#parameters for each letter
drop5LetterE = BezierPath(ActiveFont.glyphs['E'].layers['Text Regular'].bezierPath)
drop5ScaleSpeed=50
drop5DrawingStartHeight=1400
drop5DrawingHeight=0
drop5DistanceBetween=400
drop5LetterE.scale(0.3)
horizontalDistance5=random.randint(0,pageWidth-50)
drop5LetterE.translate(horizontalDistance5,drop5DrawingStartHeight)#move horizontally to the middle
drop5DrawingHeight = drop5DrawingStartHeight

#parameters for each letter
drop6LetterF = BezierPath(ActiveFont.glyphs['F'].layers['Text Regular'].bezierPath)
drop6ScaleSpeed=10
drop6DrawingStartHeight=1400
drop6DrawingHeight=0
drop6DistanceBetween=300
drop6LetterF.scale(0.2)
horizontalDistance6=random.randint(0,pageWidth-50)
drop6LetterF.translate(horizontalDistance6,drop6DrawingStartHeight)#move horizontally to the middle
drop6DrawingHeight = drop6DrawingStartHeight

#parameters for each letter
drop7LetterG = BezierPath(ActiveFont.glyphs['G'].layers['Text Regular'].bezierPath)
drop7ScaleSpeed=50
drop7DrawingStartHeight=1400
drop7DrawingHeight=0
drop7DistanceBetween=80
drop7LetterG.scale(0.08)
horizontalDistance7=random.randint(0,pageWidth-50)
drop7LetterG.translate(horizontalDistance7,drop7DrawingStartHeight)#move horizontally to the middle
drop7DrawingHeight = drop7DrawingStartHeight

#parameters for each letter
drop8LetterH = BezierPath(ActiveFont.glyphs['H'].layers['Text Regular'].bezierPath)
drop8ScaleSpeed=90
drop8DrawingStartHeight=1400
drop8DrawingHeight=0
drop8DistanceBetween=250
drop8LetterH.scale(0.125)
horizontalDistance8=random.randint(0,pageWidth-50)
drop8LetterH.translate(horizontalDistance8,drop8DrawingStartHeight)#move horizontally to the middle
drop8DrawingHeight = drop8DrawingStartHeight

#parameters for each letter
drop9LetterI = BezierPath(ActiveFont.glyphs['I'].layers['Text Regular'].bezierPath)
drop9ScaleSpeed=40
drop9DrawingStartHeight=1400
drop9DrawingHeight=0
drop9DistanceBetween=400
drop9LetterI.scale(0.175)
horizontalDistance9=random.randint(0,pageWidth-50)
drop9LetterI.translate(horizontalDistance9,drop9DrawingStartHeight)#move horizontally to the middle
drop9DrawingHeight = drop9DrawingStartHeight

#parameters for each letter
drop10LetterJ = BezierPath(ActiveFont.glyphs['J'].layers['Text Regular'].bezierPath)
drop10ScaleSpeed=30
drop10DrawingStartHeight=1400
drop10DrawingHeight=0
drop10DistanceBetween=250
drop10LetterJ.scale(0.25)
horizontalDistance10=random.randint(0,pageWidth-50)
drop10LetterJ.translate(horizontalDistance10,drop10DrawingStartHeight)#move horizontally to the middle
drop10DrawingHeight = drop10DrawingStartHeight

#parameters for each letter
drop11LetterK = BezierPath(ActiveFont.glyphs['K'].layers['Text Regular'].bezierPath)
drop11ScaleSpeed=60
drop11DrawingStartHeight=1400
drop11DrawingHeight=0
drop11DistanceBetween=200
drop11LetterK.scale(0.2)
horizontalDistance11=random.randint(0,pageWidth-50)
drop11LetterK.translate(horizontalDistance11,drop11DrawingStartHeight)#move horizontally to the middle
drop11DrawingHeight = drop11DrawingStartHeight

#parameters for each letter
drop12LetterL = BezierPath(ActiveFont.glyphs['L'].layers['Text Regular'].bezierPath)
drop12ScaleSpeed=30
drop12DrawingStartHeight=1400
drop12DrawingHeight=0
drop12DistanceBetween=250
drop12LetterL.scale(0.25)
horizontalDistance12=random.randint(0,pageWidth-50)
drop12LetterL.translate(horizontalDistance12,drop12DrawingStartHeight)#move horizontally to the middle
drop12DrawingHeight = drop12DrawingStartHeight

#parameters for each letter
drop13LetterM = BezierPath(ActiveFont.glyphs['M'].layers['Text Regular'].bezierPath)
drop13ScaleSpeed=90
drop13DrawingStartHeight=1400
drop13DrawingHeight=0
drop13DistanceBetween=200
drop13LetterM.scale(0.2)
horizontalDistance13=random.randint(0,pageWidth-50)
drop13LetterM.translate(horizontalDistance13,drop13DrawingStartHeight)#move horizontally to the middle
drop13DrawingHeight = drop13DrawingStartHeight

#parameters for each letter
drop14LetterN = BezierPath(ActiveFont.glyphs['N'].layers['Text Regular'].bezierPath)
drop14ScaleSpeed=50
drop14DrawingStartHeight=1400
drop14DrawingHeight=0
drop14DistanceBetween=250
drop14LetterN.scale(0.25)
horizontalDistance14=random.randint(0,pageWidth-50)
drop14LetterN.translate(horizontalDistance14,drop14DrawingStartHeight)#move horizontally to the middle
drop14DrawingHeight = drop14DrawingStartHeight

#parameters for each letter
drop15LetterO = BezierPath(ActiveFont.glyphs['O'].layers['Text Regular'].bezierPath)
drop15ScaleSpeed=10
drop15DrawingStartHeight=1400
drop15DrawingHeight=0
drop15DistanceBetween=350
drop15LetterO.scale(0.175)
horizontalDistance15=random.randint(0,pageWidth-50)
drop15LetterO.translate(horizontalDistance15,drop15DrawingStartHeight)#move horizontally to the middle
drop15DrawingHeight = drop15DrawingStartHeight

#parameters for each letter
drop16LetterP = BezierPath(ActiveFont.glyphs['P'].layers['Text Regular'].bezierPath)
drop16ScaleSpeed=120
drop16DrawingStartHeight=1400
drop16DrawingHeight=0
drop16DistanceBetween=100
drop16LetterP.scale(0.175)
horizontalDistance16=random.randint(0,pageWidth-50)
drop16LetterP.translate(horizontalDistance16,drop16DrawingStartHeight)#move horizontally to the middle
drop16DrawingHeight = drop16DrawingStartHeight

#Draw
while page < pages:
    page+=1
    newPage(pageWidth, pageHeight)
    frameDuration(1/15)
    fill(1,1,1)
    rect(0,0,pageWidth, pageHeight)
    fill(0,0,0)
    #drop1Letter.scale(1,1.05)
    drop1LetterA.translate(0,(-drop1DistanceBetween/pages))
    drop2LetterB.translate(0,(-drop2DistanceBetween/pages))
    drop3LetterC.translate(0,(-drop3DistanceBetween/pages))
    drop4LetterD.translate(0,(-drop4DistanceBetween/pages))
    drop5LetterE.translate(0,(-drop5DistanceBetween/pages))
    drop6LetterF.translate(0,(-drop6DistanceBetween/pages))
    drop7LetterG.translate(0,(-drop7DistanceBetween/pages))
    drop8LetterH.translate(0,(-drop8DistanceBetween/pages))
    drop9LetterI.translate(0,(-drop9DistanceBetween/pages))
    drop10LetterJ.translate(0,(-drop10DistanceBetween/pages))
    drop11LetterK.translate(0,(-drop11DistanceBetween/pages))
    drop12LetterL.translate(0,(-drop12DistanceBetween/pages))
    drop13LetterM.translate(0,(-drop13DistanceBetween/pages))
    drop14LetterN.translate(0,(-drop14DistanceBetween/pages))
    drop15LetterO.translate(0,(-drop15DistanceBetween/pages))
    drop16LetterP.translate(0,(-drop16DistanceBetween/pages))
    drawPath(drop1LetterA)
    drawPath(drop2LetterB)
    drawPath(drop3LetterC)
    drawPath(drop4LetterD)
    drawPath(drop5LetterE)
    drawPath(drop6LetterF)
    drawPath(drop7LetterG)
    drawPath(drop8LetterH)
    drawPath(drop9LetterI)
    drawPath(drop10LetterJ)
    drawPath(drop11LetterK)
    drawPath(drop12LetterL)
    drawPath(drop13LetterM)
    drawPath(drop14LetterN)
    drawPath(drop15LetterO)
    drawPath(drop16LetterP)
    #Draw the repeating images
    movedDown1=0
    movedDown2=0
    movedDown3=0
    movedDown4=0
    movedDown5=0
    movedDown6=0
    movedDown7=0
    movedDown8=0
    movedDown9=0
    movedDown10=0
    movedDown11=0
    movedDown12=0
    movedDown13=0
    movedDown14=0
    movedDown15=0
    movedDown16=0
    while drop1DrawingHeight > -400:
        movedDown1+=drop1DistanceBetween
        drop1LetterA.translate(0,-drop1DistanceBetween)
        drawPath(drop1LetterA)
        drop1DrawingHeight-=drop1DistanceBetween
    while drop2DrawingHeight > -400:
        movedDown2+=drop2DistanceBetween
        drop2LetterB.translate(0,-drop2DistanceBetween)
        drawPath(drop2LetterB)
        drop2DrawingHeight-=drop2DistanceBetween
    while drop3DrawingHeight > -400:
        movedDown3+=drop3DistanceBetween
        drop3LetterC.translate(0,-drop3DistanceBetween)
        drawPath(drop3LetterC)
        drop3DrawingHeight-=drop3DistanceBetween
    while drop4DrawingHeight > -400:
        movedDown4+=drop4DistanceBetween
        drop4LetterD.translate(0,-drop4DistanceBetween)
        drawPath(drop4LetterD)
        drop4DrawingHeight-=drop4DistanceBetween
    while drop5DrawingHeight > -400:
        movedDown5+=drop5DistanceBetween
        drop5LetterE.translate(0,-drop5DistanceBetween)
        drawPath(drop5LetterE)
        drop5DrawingHeight-=drop4DistanceBetween
    while drop6DrawingHeight > -400:
        movedDown6+=drop6DistanceBetween
        drop6LetterF.translate(0,-drop6DistanceBetween)
        drawPath(drop6LetterF)
        drop6DrawingHeight-=drop6DistanceBetween
    while drop7DrawingHeight > -400:
        movedDown7+=drop7DistanceBetween
        drop7LetterG.translate(0,-drop7DistanceBetween)
        drawPath(drop7LetterG)
        drop7DrawingHeight-=drop7DistanceBetween
    while drop8DrawingHeight > -400:
        movedDown8+=drop8DistanceBetween
        drop8LetterH.translate(0,-drop8DistanceBetween)
        drawPath(drop8LetterH)
        drop8DrawingHeight-=drop8DistanceBetween
    while drop9DrawingHeight > -400:
        movedDown9+=drop9DistanceBetween
        drop9LetterI.translate(0,-drop9DistanceBetween)
        drawPath(drop9LetterI)
        drop9DrawingHeight-=drop9DistanceBetween
    while drop10DrawingHeight > -400:
        movedDown10+=drop10DistanceBetween
        drop10LetterJ.translate(0,-drop10DistanceBetween)
        drawPath(drop10LetterJ)
        drop10DrawingHeight-=drop10DistanceBetween
    while drop11DrawingHeight > -400:
        movedDown11+=drop11DistanceBetween
        drop11LetterK.translate(0,-drop11DistanceBetween)
        drawPath(drop11LetterK)
        drop11DrawingHeight-=drop11DistanceBetween
    while drop12DrawingHeight > -400:
        movedDown12+=drop12DistanceBetween
        drop12LetterL.translate(0,-drop12DistanceBetween)
        drawPath(drop12LetterL)
        drop12DrawingHeight-=drop12DistanceBetween
    while drop13DrawingHeight > -400:
        movedDown13+=drop13DistanceBetween
        drop13LetterM.translate(0,-drop13DistanceBetween)
        drawPath(drop13LetterM)
        drop13DrawingHeight-=drop13DistanceBetween
    while drop14DrawingHeight > -400:
        movedDown14+=drop14DistanceBetween
        drop14LetterN.translate(0,-drop14DistanceBetween)
        drawPath(drop14LetterN)
        drop14DrawingHeight-=drop14DistanceBetween
    while drop15DrawingHeight > -400:
        movedDown15+=drop15DistanceBetween
        drop15LetterO.translate(0,-drop15DistanceBetween)
        drawPath(drop15LetterO)
        drop15DrawingHeight-=drop15DistanceBetween
    while drop16DrawingHeight > -400:
        movedDown16+=drop16DistanceBetween
        drop16LetterP.translate(0,-drop16DistanceBetween)
        drawPath(drop16LetterP)
        drop16DrawingHeight-=drop16DistanceBetween
    #For the next pages: jump up again
    drop1LetterA.translate(0,movedDown1)
    drop2LetterB.translate(0,movedDown2)
    drop3LetterC.translate(0,movedDown3)
    drop4LetterD.translate(0,movedDown4)
    drop5LetterE.translate(0,movedDown5)
    drop6LetterF.translate(0,movedDown6)
    drop7LetterG.translate(0,movedDown7)
    drop8LetterH.translate(0,movedDown8)
    drop9LetterI.translate(0,movedDown9)
    drop10LetterJ.translate(0,movedDown10)
    drop11LetterK.translate(0,movedDown11)
    drop12LetterL.translate(0,movedDown12)
    drop13LetterM.translate(0,movedDown13)
    drop14LetterN.translate(0,movedDown14)
    drop15LetterO.translate(0,movedDown15)
    drop16LetterP.translate(0,movedDown16)
    drop1DrawingStartHeight = drop1DrawingStartHeight-(drop1DistanceBetween/pages)
    drop2DrawingStartHeight = drop2DrawingStartHeight-(drop2DistanceBetween/pages)
    drop3DrawingStartHeight = drop3DrawingStartHeight-(drop3DistanceBetween/pages)
    drop4DrawingStartHeight = drop4DrawingStartHeight-(drop4DistanceBetween/pages)
    drop5DrawingStartHeight = drop5DrawingStartHeight-(drop5DistanceBetween/pages)
    drop6DrawingStartHeight = drop6DrawingStartHeight-(drop6DistanceBetween/pages)
    drop7DrawingStartHeight = drop7DrawingStartHeight-(drop7DistanceBetween/pages)
    drop8DrawingStartHeight = drop8DrawingStartHeight-(drop8DistanceBetween/pages)
    drop9DrawingStartHeight = drop9DrawingStartHeight-(drop9DistanceBetween/pages)
    drop10DrawingStartHeight = drop10DrawingStartHeight-(drop8DistanceBetween/pages)
    drop11DrawingStartHeight = drop11DrawingStartHeight-(drop9DistanceBetween/pages)
    drop12DrawingStartHeight = drop12DrawingStartHeight-(drop8DistanceBetween/pages)
    drop13DrawingStartHeight = drop13DrawingStartHeight-(drop9DistanceBetween/pages)
    drop14DrawingStartHeight = drop14DrawingStartHeight-(drop9DistanceBetween/pages)
    drop15DrawingStartHeight = drop15DrawingStartHeight-(drop8DistanceBetween/pages)
    drop16DrawingStartHeight = drop16DrawingStartHeight-(drop9DistanceBetween/pages)
    drop1DrawingHeight = drop1DrawingStartHeight
    drop2DrawingHeight = drop2DrawingStartHeight
    drop3DrawingHeight = drop3DrawingStartHeight
    drop4DrawingHeight = drop4DrawingStartHeight
    drop5DrawingHeight = drop5DrawingStartHeight
    drop6DrawingHeight = drop6DrawingStartHeight
    drop7DrawingHeight = drop7DrawingStartHeight
    drop8DrawingHeight = drop8DrawingStartHeight
    drop9DrawingHeight = drop9DrawingStartHeight
    drop10DrawingHeight = drop10DrawingStartHeight
    drop11DrawingHeight = drop11DrawingStartHeight
    drop12DrawingHeight = drop12DrawingStartHeight
    drop13DrawingHeight = drop13DrawingStartHeight
    drop14DrawingHeight = drop14DrawingStartHeight
    drop15DrawingHeight = drop15DrawingStartHeight
    drop16DrawingHeight = drop16DrawingStartHeight

saveImage("~/Desktop/rainy.mp4")