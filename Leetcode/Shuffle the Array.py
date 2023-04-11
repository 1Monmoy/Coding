class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        nums = nums
        n = n
        l = []
        for i in range(2*n):
            l.append(nums[i])
            l.append(nums[i+n])
        return l