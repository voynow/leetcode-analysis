"""
Runtime: 1011 ms, faster than 21.07% of Python online submissions for Container With Most Water.
Memory Usage: 23.8 MB, less than 95.31% of Python online submissions for Container With Most Water.
"""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        # init left and right as outter most arr elements
        l = 0
        r = len(height) - 1
        maxvol = 0
        
        # iterate until left and right converge
        while l != r:

            # calculate vol and compare to maximum
            maxvol = max(maxvol, min(height[l], height[r]) * (r - l))

            # shift pointers
            # keep pointer associated with largest height
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return maxvol
            