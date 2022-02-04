"""
Runtime: 746 ms, faster than 69.39% of Python online submissions for 3Sum.
Memory Usage: 16.8 MB, less than 66.46% of Python online submissions for 3Sum.
Cred: NeetCode 3Sum - Leetcode 15 - Python
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        triplets = []
        nums.sort()
        print(nums)
        
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue
                
            l = i + 1
            r = len(nums) - 1
            
            while l < r:
                three_sum = num + nums[l] + nums[r]
                if  three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                elif three_sum == 0:
                    triplets.append([num, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                
        return triplets
                    