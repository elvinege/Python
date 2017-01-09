vowel = ["a", "e", "i", "u", "o"]

def vowelOrNot(character):
    for i in vowel:
        if character == i:
            return True
    return False

print(vowelOrNot("e"))
print(vowelOrNot("f"))
print(vowelOrNot("i"))
print(vowelOrNot("r"))
