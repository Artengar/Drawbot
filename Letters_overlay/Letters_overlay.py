#This script put letters on top of each other, comparing which parts of the letters are similar in all typefaces installed on your computer

presentFonts = installedFonts()
fill(0, 0, 0, 0.2)

for item in presentFonts:
    if item != item.endswith("egular"):
        print(type(item))
        print(item)
        font(item, 450)
        text("f", (350, 400))
        
saveImage("~/Desktop/f.jpg")