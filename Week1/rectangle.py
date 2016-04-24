import turtle
turtle.home()

# 1) Draw a rectangle with width 200 and height 100

def drawRect(width, height):
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)

drawRect(100, 200)

input("Press enter to exit")
