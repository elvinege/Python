import turtle
turtle.home()

# 2) Draw a equilateral triangle with edge-length 100
def drawTriangle(length):
    turtle.forward(100);
    turtle.left(120);
    turtle.forward(100);
    turtle.left(120);
    turtle.forward(100);

drawTriangle(50);
input("Press enter to exit")
