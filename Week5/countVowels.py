def count_vowels(word):
    count=0
    for i in word:
        if i in ["a", "e", "i", "u", "o"]:
            count = count + 1
    return count

print(count_vowels("Hello"))
print(count_vowels("Programming"))
