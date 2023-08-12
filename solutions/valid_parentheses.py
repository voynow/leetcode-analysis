"""
20. Valid Parentheses
Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
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

            

