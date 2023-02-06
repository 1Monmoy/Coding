s = "codeforces"

t = int(input())

for i in range(t):
    a = input()
    count = 0

    for i in s:
        if a == i:
            count = 1
            break
    if count >0:
        print("YES")
    else:
        print("NO")
