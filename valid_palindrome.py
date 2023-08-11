"""
125. Valid Palindrome
Easy


A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = "".join([ch.lower() for ch in s if ch.isalpha() or ch.isnumeric()])
        mid = len(s) // 2

        print(s)

        l = s[:mid]
        if len(s) % 2:
            r = s[mid + 1:]
        else:
            r = s[mid:]

        print(l, r)

        for i in range(len(l)):
            if l[i] != r[-(i + 1)]:
                return False
        return True