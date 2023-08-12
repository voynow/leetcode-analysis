"""
Runtime
33ms
Beats 97.04%of users with Python
Memory
13.23mb
Beats 59.99%of users with Python
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        string = str(x)

        if len(string) % 2:
            l = r = len(string) // 2
        else:
            r = len(string) // 2
            l = len(string) // 2 - 1

        while l >= 0:
            if string[l] == string[r]:
                l -= 1
                r += 1
            else:
                return False
        return True
