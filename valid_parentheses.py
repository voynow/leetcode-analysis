"""
Runtime
11ms
Beats 94.74%of users with Python
Memory
13.49mb
Beats 50.18%of users with Python
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        strmap = {
            '(': ')',
            '{': '}',
            '[': ']',
        }

        stack = []
        while s:
            if s[0] in strmap:
                stack.append(s[0])
            else:
                if not stack and s:
                    return False
                if stack and s[0] != strmap[stack.pop()]:
                    return False
            s = s[1:]
    
        if stack:
            return False

        return True

            

