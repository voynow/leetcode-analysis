"""
Runtime: 39 ms, faster than 19.56% of Python online submissions for Valid Parentheses.
Memory Usage: 13.6 MB, less than 30.76% of Python online submissions for Valid Parentheses.
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        chmap = {
            '(': ')',
            '{': '}',
            '[': ']',
        }
        stack = []

        while s:
            ch = s[0]
            # check if open parentheses
            if ch in chmap:
                stack.append(ch)
            else:
                # stack is empty -> invalid
                if not stack:
                    return False
                # current char matches top of stack -> valid
                if ch == chmap[stack[-1]]:
                    stack = stack[:-1]
                # all other cases -> invalid
                else:
                    return False
            s = s[1:]
        
        # chars remaining in stack -> invalid
        if stack:
            return False

        return True
    