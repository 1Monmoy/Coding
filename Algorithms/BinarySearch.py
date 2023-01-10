# Binary Search Using Loop
import math
def BS(A, n):
    l = 0
    h = (len(A) - 1)
    counter = False
    while l<=h:
        mid = math.floor((l+h)/2)
        if n == A[mid]:
            print("Element present at:", mid)
            counter = True
            break
        else:
            if n > A[mid]:
                l = mid+1
            else:
                h = mid - 1
    if counter == False:
        print("Element not found")

A = list(map(int, input().split()))
n = int(input())
BS(A, n)