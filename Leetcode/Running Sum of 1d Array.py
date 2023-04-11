class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = []
        j = 0
        for i in range(len(nums)):
            l.append(j)
            j = j + nums[i]
        return l
