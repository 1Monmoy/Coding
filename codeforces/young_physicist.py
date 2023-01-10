
n = int(input())
s = []
sum = 0
for i in range(n):
    a = list(map(int, input().split()))
    s.append(a)

for i in range(n):
    for j in range(2):
        sum += s[i][j]

if sum == 0:
    print("YES")
else:
    print("NO")
    sum = 0



