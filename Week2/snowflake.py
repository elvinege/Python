import turtle
turtle.home()

def drawCurve(length, depth):
    if depth == 1:
        turtle.forward(length)
    else:
        drawCurve(length/3, depth-1)
        turtle.right(60)
        drawCurve(length/3, depth-1)
        turtle.left(120)
        drawCurve(length/3, depth-1)
        turtle.right(60)
        drawCurve(length/3, depth-1)

def snowflake(length, snowDepth):
    for i in range(3):
        drawCurve(length, snowDepth)
        turtle.left(120)

#turtle.speed(0);

#snowflake(50, 1);
#snowflake(50, 2);
snowflake(100, 0);
#snowflake(50, 4);
#snowflake(50, 5);
