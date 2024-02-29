from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums = nums
        n = len(nums)
        nums.sort()
        c = 1
        j = 1
        l = []
        if n == 1:
            return nums[0]

        for i in nums:
            c += 1
            
            if nums[j] != i:
                
                c = 1
            l.append(c)
            j+=1

            if l[-1] > n/2:
                return i

nums = [2,2,1,1,1,2,2]
obj = Solution()
print(obj.majorityElement(nums))