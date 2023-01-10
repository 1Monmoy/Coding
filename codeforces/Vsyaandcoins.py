t = int(input())
for i in range(t):
    a, b = input().split()
    if int(a) > 0:
        print(int(a) + (int(b)*2) +1)
    else:
        print("1")