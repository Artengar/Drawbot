#Template to create empty pages
#Free for use and modify, as long as a reference is provided.
#created by Maarten Renckens (maarten.renckens@artengar.com)


pageWidth = 1
pageHeight = 1
#The location to YOUR folder in which the images are positioned
Directory = '/Users/YOUR_USER_NAME/Desktop/FOLDER_NAME'
#This script assumes that all files in there are images with equal width/heights!



#Do the script
import os, sys, re
if Directory[len(Directory)-1] != "/":
    Directory += "/"
files = sorted(os.listdir(Directory))
toRemove = []

Columns = 0
Rows = 0

#clean up the input
for item in files:
    if item[0]== ".":
        print("not using this item: ", item)
        toRemove.append(item)
    if item[-4:]== ".mp4":
        print("not using this item: ", item)
        toRemove.append(item)
    if item[-4:]== ".ufo":
        print("not using this item: ", item)
        toRemove.append(item)
    if item[-7:]== ".glyphs":
        print("not using this item: ", item)
        toRemove.append(item)
for item in toRemove:
    files.remove(item)

#calculate how much colums and rows will be used:
def calculateSquares():
    global Columns
    global Rows
    previousNumber = 0
    for number in range(len(files)):
        number +=1
        print(number, previousNumber, len(files)/number)
        if number > (len(files)/number):
            Columns = number
            Rows = int(len(files)/number)+1
            print("This script will use %s colums and %s rows.\n" %(Columns, Rows))
            return
        elif number == (len(files)/number):
            Columns = number
            Rows = int(len(files)/number)
            print("This script will use %s colums and %s rows.\n" %(Columns, Rows))
            return
        previousNumber = number

calculateSquares()
#scale up the page size to fit
Sizes = imageSize((Directory+files[1]))[0]
size(pageWidth*Columns*Sizes, pageHeight*Rows*Sizes)

#Create the overview of images
def placeImages(Directory, item, RowNR, ColumnNR, Sizes):
    print("Coordinates: ", ((ColumnNR-1)*Sizes,Sizes*Rows-(Sizes*RowNR)) )
    image(Directory+item, ((ColumnNR-1)*Sizes,Sizes*Rows-(Sizes*RowNR)) )

#Run the script
ColumnNR = 0
RowNR = 1
for item in files:
    ColumnNR +=1
    if ColumnNR-Columns == 1:
        RowNR +=1
        ColumnNR-=Columns
    print("processing %s on column %s and row %s" %(item, ColumnNR, RowNR))
    placeImages(Directory, item, RowNR, ColumnNR, Sizes)

saveImage("~/Desktop/overview_of_images.jpg")

