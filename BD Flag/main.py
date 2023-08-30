from turtle import *

title('Bangladesh Flag')
Screen().setup(width=1200, height=680)

hideturtle()

color('white')
begin_fill()
left(90)
forward(300)
end_fill()

color('green')
begin_fill()
right(90)
forward(300)
right(90)
forward(300)
right(90)
forward(500)
right(90)
forward(300)
right(90)
forward(170)
end_fill()

right(90)
forward(140)

color('red')
begin_fill()
circle(90)
end_fill()

color('green')
right(90)
forward(170)
left(90)
forward(160)

color('chocolate')
begin_fill()
forward(300)
left(90)
forward(20)
left(90)
forward(300)
end_fill()

done()
