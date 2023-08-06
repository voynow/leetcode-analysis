class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        p = 0

        for i in range(len(haystack)):
            while i + p < len(haystack) and haystack[i + p] == needle[p]:
                if p + 1 == len(needle):
                    return i
                p += 1
            p = 0
        return -1