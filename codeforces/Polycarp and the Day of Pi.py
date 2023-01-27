s = 314159265358979323846264338327
s = str(s)
t = int(input())

for i in range(t):

    n = input()
    count = 0
    for i, x in enumerate(n):
        if x == str(s[int(i)]):
            count+=1
        else:
            break
    print(count)

