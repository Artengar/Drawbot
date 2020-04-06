translate(500,500)

#0.55229 is the value used by Glyphs to create circles (see Georg Seifert, Glyphs forum)

stroke(0)
fill(1)
path = BezierPath()
path.moveTo((0,100))

path.curveTo( (100*0.55229, 100), (100, 100*0.55229), (100,0) )
path.curveTo( (100, -100*0.55229), (100*0.55229, -100), (0,-100) )
path.curveTo( (-100*0.55229, -100), (-100, -100*0.55229), (-100,0) )
path.curveTo( (-100, 100*0.55229), (-100*0.55229, 100), (0,100) )

drawPath(path)