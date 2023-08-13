"""
169. Majority Element
Easy

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
 

Follow-up: Could you solve the problem in linear time and in O(1) space?
"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # linear space complexity

        counter = {}

        numslen = len(nums)
        for item in nums:
            if item not in counter:
                counter[item] = 1
            else:
                counter[item] += 1

            if counter[item] > numslen / 2:
                return item
            


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Boyer-Moore Voting Algorithm
        # constant space complexity

        candidate = -1
        counter = 0

        for item in nums:
            if candidate == item or counter == 0:
                candidate = item
                counter += 1
            else:
                counter -= 1
        return candidate
