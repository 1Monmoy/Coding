def linear(A, l):
    j = 0
    counter = True
    for i in l:
        if A == i:
            print("Available in this index:", (j))
            counter = True
            break
        j += 1
        counter = False
    if counter == False:
        print("not in the array")


l = list(map(int, input().split()))
n = int(input())
linear(n, l)