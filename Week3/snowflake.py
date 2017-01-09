import turtle
turtle.home()

def calculatePerimeter(length, depth):
    if depth == 1:
        return float(3 * length)
    else:
        return float(4)/3 * calculatePerimeter(length, depth-1)

print(calculatePerimeter(100, 3))
print(calculatePerimeter(100, 2))
print(calculatePerimeter(100, 1))
#print(calculatePerimeter(100, 0))
print(calculatePerimeter(100, 4))
