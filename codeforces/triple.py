
n = int(input())
for i in range(n):
    res = -1
    c = 0
    a = int(input())
    s = list(map(int, input().split()))

    s.sort()
    for i in range(len(s)-2):
        if s[i] == s[i+1] and s[i] == s[i+2]:
            print(s[i])
            c += 1
            break
    if c<1:
        print('-1')



