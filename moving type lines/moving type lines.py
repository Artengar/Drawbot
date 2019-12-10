x=0

def placetext(x):
    txt = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi. Nam liber tempor cum soluta nobis eleifend option congue nihil imperdiet doming id quod mazim placerat facer possim assum. Typi non habent claritatem insitam; est usus legentis in iis qui facit eorum claritatem. Investigationes demonstraverunt lectores legere me lius quod ii legunt saepius. Claritas est etiam processus dynamicus, qui sequitur mutationem consuetudium lectorum. Mirum est notare quam littera gothica, quam nunc putamus parum claram, anteposuerit litterarum formas humanitatis per seacula quarta decima et quinta decima. Eodem modo typi, qui nunc nobis videntur parum clari, fiant sollemnes in futurum."
    font("Times-Italic", 100)
    fontSize(50)
    fallbackFont("Times")
    hyphenation(True)
    lineHeight(35)
    tracking(5)
    baselineShift(x)
    #text("Hello World!", (500, 500), align="center")
    textBox(txt, (100, 100, 800, 800))
    print(x)
    
    
#firstpage
fill(1)
rect(0,0,1000,1000)
fill(0)
rect(0,880,120,120)
placetext(0)

for i in range(10):
    newPage()
    fill(1)
    rect(0,0,1000,1000)
    fill(0)
    placetext(i*9)
    rect(0,880,120,120)

newPage()
bez=BezierPath()
bez.text("m", font="Helvetica", fontSize=1000, offset=(71,100))
fill(0.8)
drawPath(bez)

PixelSize = 50
for x in range(0,1000,PixelSize):
    for y in range(0,1000,PixelSize):
        rect(x,y,PixelSize-5,PixelSize-5)

saveImage("~/Desktop/test.gif")