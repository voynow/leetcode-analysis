"""
Runtime: 3753 ms, faster than 24.51% of Python online submissions for Longest Palindromic Substring.
Memory Usage: 13.5 MB, less than 72.36% of Python online submissions for Longest Palindromic Substring.
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # tracking longest
        longest = ""
        
        # iterate through characters
        for i in range(len(s)):
            
            # checking even vs odd substrings
            for j in range(2):
                l = i
                r = i + j
                
                # edge case for even at end of string
                if r == len(s):
                    continue
                
                # iterate while chars at pointers are equal
                # check for new longest palindrome
                # break if pointers go out of bounds
                # increment pointers
                while s[l] == s[r]:
                    if len(s[l:r+1]) > len(longest):
                        longest = s[l:r+1]
                    if l == 0 or r == len(s) - 1:
                        break
                    else:
                        l -= 1
                        r += 1

        return longest
            