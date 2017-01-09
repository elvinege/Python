#This function finds number of character in a string

def findLength(word):
    length = 0
    for i in word:
        length = length + 1
    return length

print(findLength("elvin"))
