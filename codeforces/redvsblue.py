import math
n = int(input())
res = []
for i in range(n):
    a = list(map(int, input().split()))
    k = a[0]
    r = a[1]
    b = a[2]
    while r > 0:
        print("R"*math.ceil((r/(b+1))), end='')
        if b > 0:
            print("B", end='')
        r = r - math.ceil(r/(b+1))
        b = b - 1
    print()