word = input()
lower = 0
upper = 0
for i in word:
    if i.isupper():
        upper += 1
    elif i.islower:
        lower += 1
    
if upper>lower:
    print(word.upper())
else:
    print(word.lower())