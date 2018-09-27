#NOTE: this script is written for Drawbot within Glyphs!
#NOTE: this script creates a typeface.
# For questions, contact Maarten Renckens: maarten.renckens@artengar.com

#Get necessary information from Glyphs
from GlyphsApp import *
myFont = Glyphs.font

#Put the parameters right
pageSize = 'A4' #This is equal to 595 units on the x-axis and 842 units on the y-axis
pageNumber = 0
text1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
text2 = 'abcdefghijklmnopqrstuvwxyz'
text3 = '01234567890 .,:;!?*&"@'
text4 = 'lynx cq vos prikt bh dag zwemjuf \ndoch bep flink sexy qua vorm zwijgt \npechdag sexy quizvrouw blijft mank \ndoch vlakbij zwerft n exquis gympje \nwazig tvfilmpje rond chique skybox \nsexy qua lijf doch bang voor t zwempak \nfilmquiz bracht knappe ex yogi van de wijs \npas wijze lynx bezag vroom het fikse aquaduct \nop brute wijze ving de schooljuf de quasi kalme lynx \ntypisch kaf bij zo exquis gevormde juwelen \npack my box with five dozen liquor jugs \nthe quick brown fox jumps over the lazy dog \nTHE QUICK BROWN FOX JUMPS OVER THE LAZY DOG'
text5 = ''

#Start the script
for thisInstance in myFont.instances:#takes only the active instances from Glyphs
    pageNumber+=1
    newPage(pageSize)
    #place header/footer
    fontSize(9)
    instanceFont = thisInstance.interpolatedFontProxy
    header=myFont.familyName + ' ' + thisInstance.name
    footer=str(pageNumber) + ' Test specimen. This Drawbot script © Maarten Renckens. Freely available at Github: https://github.com/Artengar/drawbot'
    font("Helvetica")
    textBox(header,(30,800,535,30), align="center")#(x, y, w, h)
    textBox(footer,(30,0,535,30), align="center")#(x, y, w, h)
    #place the designed typeface
    font("Vivace-"+thisInstance.name)
    fontSize(30)
    textBox(text1,(30,740,535,50), align="center")#(x, y, w, h)
    #if textOverflow(txt, box, align=None)¶
    textBox(text2,(30,690,535,50), align="center")#(x, y, w, h)
    #if textOverflow(txt, box, align=None)¶
    textBox(text3,(30,640,535,50), align="center")#(x, y, w, h)
    #if textOverflow(txt, box, align=None)¶
    fontSize(15)
    textBox(text4,(30,50,595,600), align="left")#(x, y, w, h)
    #if textOverflow(txt, box, align=None)¶
    print "page", pageNumber, thisInstance

    for glyph in myFont.glyphs:
        text5+=glyph.name
    textBox(text5,(30,50,535,350), align="left")#(x, y, w, h)
    if textOverflow(text5,(30,50,535,350), align="left"):
        print("text has overflow!")

#saveImage("~/Desktop/Specimen.pdf")