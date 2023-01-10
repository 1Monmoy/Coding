t = int(input())
for i in range(t):
    ticket = input()
    firsthalf = 0
    secondhalf = 0
    for i in range(3):
        firsthalf += int(ticket[i])
    for i in range(3, len(ticket)):
        secondhalf += int(ticket[i])
    if firsthalf == secondhalf:
        print("YES")
    else:
        print("NO")