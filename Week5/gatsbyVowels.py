def count_vowels(word):
    count=0
    for i in word:
        if i in ["a", "e", "i", "u", "o"]:
            count = count + 1
    return count

gatsby = open("gatsby.txt")

# 1) List for collecting words
words = []

for line in gatsby.readlines():
    for word in line.split():
        words.append(word)

# 2) Empty dictionary
word_count = {}

# 3) Count vowels for each word in text
for w in words:
    word_count[w] = count_vowels(w)

def findMax():
    maxVow = max(word_count, key=word_count.get)
    return maxVow

print(findMax())
