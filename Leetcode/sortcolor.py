def bubbleSort(nums):
    n = len(nums)
    # optimize code, so if the numsay is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all numsay elements
    for i in range(n-1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the numsay from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if nums[j] > nums[j + 1]:
                swapped = True
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
         
        if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            return
nums = list(map(int, input().split()))

bubbleSort(nums)

for i in nums:
    print(i, end=' ')

