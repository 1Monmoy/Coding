t = int(input())
for i in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    iseven = 0
    isodd = 0
    if n%2==0:
        j = 1
    else:
        j = 0
    for i in s:
        if  i % 2 != 0:
            iseven += 1
        else:
            isodd += 1
    if iseven == 0 or isodd == 0:
        print("YES")
    else:
        iseven = 0
        isodd = 0

        while j < n:
            s[j] = s[j]+1
            j += 2

        for i in s:
            if  i % 2 != 0:
                iseven += 1
            else:
                isodd += 1
        if iseven == 0 or isodd == 0:
            print("YES")
        else:
            print("NO")

