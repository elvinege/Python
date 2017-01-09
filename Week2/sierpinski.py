import turtle
turtle.home()

def sierpinskiTriangle(length, depth):
    if depth == 1:
        for i in range(3):
            turtle.forward(length)
            turtle.left(120)
    else:
        sierpinskiTriangle(length/2,depth-1)
        turtle.forward(length/2)
        sierpinskiTriangle(length/2,depth-1)
        turtle.back(length/2)
        turtle.left(60)
        turtle.forward(length/2)
        turtle.right(60)
        sierpinskiTriangle(length/2,depth-1)
        turtle.left(60)
        turtle.back(length/2)
        turtle.right(60)

sierpinskiTriangle(300, 2);
