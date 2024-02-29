from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        nums = prices
        max_prof = 0
        right = 1
        left = 0
        currentprof = 0
        if len(nums) > 1:
            while right < len(nums):
                currentprof = nums[right] - nums[left]
                max_prof = max(max_prof, currentprof)
                if nums[left] > nums[right]:
                    left = right
                right += 1
        else:
            return 0
        

        if max_prof > 0:
            return max_prof
        else:
            return 0
        

prices = [7,1,5,3,6,4]
obj = Solution()
print(obj.maxProfit(prices))





