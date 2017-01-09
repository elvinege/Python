def findMaxThree(a, y, z):
    Max = a
    if y > Max:
        Max = y
    if z > Max:
        Max = z
        if y > z:
            Max = y
    return Max

print(findMaxThree(1, 4, 2))
