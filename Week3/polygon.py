import turtle
turtle.home()


def drawPolygon(length, numberOfSide):
    for i in range(numberOfSide):
        turtle.left(360/numberOfSide)
        turtle.forward(length)


#drawPolygon(100, 3)
#drawPolygon(100, 4)
drawPolygon(100, 5)
#drawPolygon(50, 8)
