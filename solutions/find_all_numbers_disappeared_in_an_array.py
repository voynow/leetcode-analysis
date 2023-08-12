"""
Runtime: 316 ms, faster than 72.66% of Python online submissions for Find All Numbers Disappeared in an Array.
Memory Usage: 25.1 MB, less than 5.04% of Python online submissions for Find All Numbers Disappeared in an Array.
"""
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_remaining = {i for i in range(1, len(nums) + 1)}
        
        for num in nums:
            if num in nums_remaining:
                nums_remaining.remove(num)
    
        return nums_remaining