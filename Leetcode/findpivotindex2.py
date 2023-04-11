nums = list(map(int, input().split()))

for i in range(1, len(nums)+1):
    leftsum = 0
    rightsum = 0
    for k in range(i-1):
        leftsum += nums[k]
    for j in range(len(nums)-i):
        rightsum += nums[-j-1]
    if leftsum == rightsum:
        print(i)
#this code gets TLE in leetcode judge.

    
