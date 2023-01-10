import math
import random


def nthRoot(A,N):
 
    # initially guessing a random number between
    # 0 and 9
    xPre = random.randint(1,101) % 10
  
    #  smaller eps, denotes more accuracy
    eps = 0.001
  
    # initializing difference between two
    # roots by INT_MAX
    delX = 2147483647
  
    #  xK denotes current value of x
    xK=0.0
  
    #  loop until we reach desired accuracy
    while (delX > eps):
 
        # calculating current value from previous
        # value by newton's method
        xK = ((N - 1.0) * xPre +
              A/pow(xPre, N-1)) /N
        delX = abs(xK - xPre)
        xPre = xK;
         
    return xK
t = int(input())
for i in range(t):
    x, y = input().split()
    x = int(x)
    y = int(y)
    a = 0
    b = 0
    if x <= y:
        if y % x == 0:
            b = int(y/x)
            a = 1
        else:
            a = 0
            b = 0
    print(a, b)

