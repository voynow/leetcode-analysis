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

        # sort list O(n log(n))
        nums.sort()
        
        # iterate over elements
        for i, num in enumerate(nums):

            # dont consider duplicates
            if i > 0 and num == nums[i - 1]:
                continue
                
            # set pointers
            l = i + 1
            r = len(nums) - 1
            
            # iterate until pointers converge
            while l < r:

                # calculate sum, update pointers accordingly
                three_sum = num + nums[l] + nums[r]
                if  three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                elif three_sum == 0:
                    triplets.append([num, nums[l], nums[r]])

                    # update left pointer to skip any duplicate elements
                    # this part was TRICKY to unpack
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

                    # Alternate solution to the skip duplicate idea
                    # while l < r and nums[l] == nums[l + 1]:
                    #     l += 1
                    # while l < r and nums[r] == nums[r - 1]:
                    #     r -= 1
                    # l += 1
                    # r -= 1
                
        return triplets
                    