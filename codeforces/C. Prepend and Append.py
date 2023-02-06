
import math
t = int(input())

for m in range(t):
    n = int(input())
    l = 0
    k = -1
    s = input()
    s = list(s)
    for i in range(math.floor(n/2)):
        if s[0] == '1' and s[-1] == '0':
            s.pop(0)
            s.pop(-1)
        elif s[0] == '0' and s[-1] == '1':
            s.pop((0))
            s.pop(-1)
        # if l>n/2:
        #     break

    print(len(s))

