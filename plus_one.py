class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        return [int(s) for s in str(int("".join(map(str, digits))) + 1)]