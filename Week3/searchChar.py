def iterativelySearch(word, char):
    for i in word:
        if i == char:
            return True
    return False

#print(iterativelySearch("hello", "l"))
#print(iterativelySearch("hello", "h"))
#print(iterativelySearch("hello", "o"))
#print(iterativelySearch("hello", "v"))
#print(iterativelySearch("hello", "p"))


def recursivelySearch(word, char):
    if len(word) == 0:
        return False
    if char == word[0]:
        return True
    else:
        return recursivelySearch(word[1:], char)

print(recursivelySearch("hello", "l"))
print(recursivelySearch("hello", "h"))
print(recursivelySearch("hello", "v"))
