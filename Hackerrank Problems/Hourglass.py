arra = []
sum1 = []
t = 0
for i in range(6):
    s = list(map(int, input().split()))
    arra.append(s)
while t < 4:
    sum = 0
    u = 0
    while u < 4:
        sum = sum + arra[t][u] + arra[t][u+1] + arra[t][u+2] + arra[t+1][u+1] + arra[t+2][u] + arra[t+2][u+1] + arra[t+2][u+2]
        sum1.append(sum)
        u += 1
        sum = 0
    t += 1
sum1.sort()

print(sum1[-1])