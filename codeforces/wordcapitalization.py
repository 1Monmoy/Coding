word = input()
if word[0].isupper():
    print(word)
else:
    word2 = word[0].upper()
    word2 = word2 + word[1:]
    print(word2)