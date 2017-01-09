import turtle
turtle.home()

def drawCurve(length, depth):
    if depth < 2:
        turtle.forward(length)
    else:
        drawCurve(length/3, depth-1)
        turtle.left(60)
        drawCurve(length/3, depth-1)
        turtle.right(120)
        drawCurve(length/3, depth-1)
        turtle.left(60)
        drawCurve(length/3, depth-1)


turtle.speed(0);

#drawCurve(200, 0);
#drawCurve(200, 1);
#drawCurve(200, 2);
#drawCurve(200, 5);
#drawCurve(200, 4);
drawCurve(50, 3);

input("Press enter to exit")
