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