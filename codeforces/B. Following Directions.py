
t = int(input())

for i in range(t):
    n = int(input())
    a = input()
    a2, b2 = 0,0
    count = 0
    for i in a:
        if i == "R":
            a2+=1
            if a2 == 1 and b2 == 1:
                count+= 1
                break
        elif i == "L":
            a2-=1
            if a2 == 1 and b2 == 1:
                count+= 1
                break
        elif i == "U":
            b2+=1
            if a2 == 1 and b2 == 1:
                count+= 1
                break
        elif i == "D":
            b2-=1
            if a2 == 1 and b2 == 1:
                count+= 1
                break
    if count>0:
        print("YES")
    else:
        print("NO")
