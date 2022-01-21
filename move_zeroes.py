"""
Runtime: 1023 ms, faster than 13.68% of Python online submissions for Move Zeroes.
Memory Usage: 14.6 MB, less than 85.23% of Python online submissions for Move Zeroes.
"""
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        remove_idxs = []
        for i, num in enumerate(nums):
            if num == 0:
                remove_idxs.append(i)
                
        for i, idx in enumerate(remove_idxs):
            nums.remove(nums[idx - i])
            nums.append(0)
            