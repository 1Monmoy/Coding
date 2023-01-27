nums = list(map(int, input().split()))

Sum = sum(nums)
leftsum = 0

for i, x in enumerate(nums):
    if leftsum == (Sum - leftsum - x):
        print(i)
    leftsum+=x

