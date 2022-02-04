class Solution(object):

    def twoSum(self, nums, target):
        """
        O(n^2) quadratic runtime
        Runtime: 4019 ms, faster than 20.39% of Python online submissions for Two Sum.
        Memory Usage: 14.2 MB, less than 89.73% of Python online submissions for Two Sum.
        """
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum(self, nums, target):
        """
        O(n) linear runtime
        Runtime: 55 ms, faster than 74.38% of Python online submissions for Two Sum.
        Memory Usage: 14.3 MB, less than 48.40% of Python online submissions for Two Sum.
        """

        lookup = {}
        
        for i, num in enumerate(nums):
            if target - num in lookup:
                return [i, lookup[target - num]]
            else:
                lookup[num] = i
