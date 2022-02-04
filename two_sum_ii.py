class Solution(object):
    def twoSum(self, numbers, target):
        """
        Runtime: 172 ms, faster than 5.15% of Python online submissions for Two Sum II - Input Array Is Sorted.
        Memory Usage: 14.1 MB, less than 18.92% of Python online submissions for Two Sum II - Input Array Is Sorted.
        """

        lookup = {}
        
        for i, num in enumerate(numbers):
            if target - num in lookup:
                return [lookup[target - num] + 1, i + 1]
            else:
                lookup[num] = i

    def twoSum(self, numbers, target):
        """
        Runtime: 100 ms, faster than 7.58% of Python online submissions for Two Sum II - Input Array Is Sorted.
        Memory Usage: 14.3 MB, less than 17.74% of Python online submissions for Two Sum II - Input Array Is Sorted.
        """

        l = 0
        r = len(numbers) - 1
        
        while True:
            twosum = numbers[l] + numbers[r]
            if twosum == target:
                return [l + 1, r + 1]
            elif twosum < target:
                l += 1
            else:
                r -= 1
