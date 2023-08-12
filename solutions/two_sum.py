"""
1. Two Sum
Easy
49.9K
1.6K
Companies
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
Accepted
10.4M
Submissions
20.7M
Acceptance Rate
50.4%
"""
class Solution(object):
    def twoSum(self, nums, target):
        # check all combinations
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

class Solution(object):
    def twoSum(self, nums, target):
        lookup = {}
        
        # add eliments in order to lookup table
        # search for required second element in lookup table for return
        for i, num in enumerate(nums):
            if target - num in lookup:
                return [i, lookup[target - num]]
            else:
                lookup[num] = i
