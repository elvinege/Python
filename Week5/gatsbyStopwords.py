gatsby = open("gatsby.txt")

words = []

for line in gatsby.readlines():
    for word in line.split():
        words.append(word)

word_dict = {}

for w in words:
    if w in word_dict:
        word_dict[w] = word_dict[w] + 1
    else:
        word_dict[w] = 1

stopwords = open("stopwords.txt")

stop_words = []

for line in stopwords.readlines():
    for word in line.split():
        word = line.strip()
        stop_words.append(word)

filtered_words = {}

for w in word_dict:
    if w not in stop_words:
        filtered_words[w] = word_dict[w]

# Find max 

current_highest = ('',0)
for word, count in filtered_words.items():
    if count > current_highest[1]:
        current_highest = (word,count)
print(current_highest)
