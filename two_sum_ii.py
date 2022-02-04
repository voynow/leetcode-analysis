"""
Runtime: 172 ms, faster than 5.15% of Python online submissions for Two Sum II - Input Array Is Sorted.
Memory Usage: 14.1 MB, less than 18.92% of Python online submissions for Two Sum II - Input Array Is Sorted.
"""
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        lookup = {}
        
        for i, num in enumerate(numbers):
            if target - num in lookup:
                return [lookup[target - num] + 1, i + 1]
            else:
                lookup[num] = i