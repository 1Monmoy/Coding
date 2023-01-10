t = int(input())
for i in range(t):
    m = list(map(int, input().split()))
    s = []
    count = 0
    l = []
    for j in range(m[0]):
        a = input()
        s.append(a)
    for j in range(m[0]-1):
        for k in range(j, m[0]-1):
            for z in range(m[1]):
                q = 0
                f = s[j][z]
                if ord(s[k+1][z]) < ord(f):
                    count += ord(f) - ord(s[k+1][z])
                else:
                    count += ord(s[k+1][z]) - ord(f)
            if q <= 0:
                l.append(count)
            count = 0

    if len(l) == 0:
        print("0")
    else:
        l.sort()
        print(l[0])

