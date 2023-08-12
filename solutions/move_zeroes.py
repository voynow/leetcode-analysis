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
            