def split(x, n, res):
    if(x < n):
        print(-1)
    elif (x % n == 0):
        for i in range(n):
            res.append(x//n)
    else:
        zp = n - (x % n)
        pp = x//n
        for i in range(n):
            if(i>= zp):
                res.append(pp + 1)
            else:
                res.append(pp)

t = int(input())
for i in range(t):
    res = []
    a = list(map(int, input().split()))
    x = int(a[2])
    x = x
    n = int(a[0])
    n = n-1
    split(x, n, res)
    res.append(a[1] - a[2])
 
    for item in res:
        print(item, end=" ")

