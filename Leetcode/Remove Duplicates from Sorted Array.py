from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in nums:
            if i == 0 or i == 1 or nums[i-2] != j:
                nums[i] = j
                i += 1
        return i

nums = [0,0,1,1,1,1,2,3,3]
obj = Solution()
print(obj.removeDuplicates(nums))