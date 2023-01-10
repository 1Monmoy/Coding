s = []
l = 0
k = 0
count = 0
for i in range(5):
    a = list(map(int, input().split()))
    s.append(a)

for i in range(5):
    for j in range(5):
        if s[i][j] == 1:
            l = i+1
            k = j+1
            break
while 1:
    if l == 3 and k == 3:
        break
    if l < 3:
        l += 1
        count += 1
    elif l > 3:
        l -= 1
        count += 1
    elif k < 3:
        k += 1
        count += 1
    elif k > 3:
        k -= 1
        count += 1
print(count)