from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = nums
        target = target
        for i in range(len(nums)-1):
            for j in range(i, len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i, j]
        return []


nums = [3,3]
obj = Solution()
print(obj.twoSum(nums, target=6))