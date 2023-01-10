t = int(input())
for i in range(t):
    s = input()
    first = 'aa'
    l = []
    l.append(first[0])
    l.append(first[1])
    count = 0
    for i in range(26):
        if count > 0:
            l[0] = chr(ord(l[0]) +1 )
            l[1] = '`'
        for j in range(25):
            l[1] = chr(ord(l[1]) + 1)
            count += 1
            if l[0] == l[1]:
                l[1] = chr(ord(l[1]) + 1)
            if s[0] == l[0] and s[1] == l[1]:
                print(count)
                break

            

