
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        # this works
        s[:] = [s[i - 1] for i in range(len(s), 0, -1)]

        # but interestingly, this doesn't
        # s = [s[i - 1] for i in range(len(s), 0, -1)]
