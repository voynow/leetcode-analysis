"""
3. Longest Substring Without Repeating Characters
Medium
36.2K
1.6K
Companies
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        current_longest = 0
        unique = set()
        l = 0
        r = 0

        # iterate until right pointer exceeds length of string
        while r < len(s):
            
            # clear substring until valid unqiue set if duplicate value found
            while s[r] in unique:
                unique.remove(s[l])
                l += 1
            # add value to set, tracking current longest and incrementing right pointer
            else:
                unique.add(s[r])
                current_longest = max(len(unique), current_longest)
                r += 1
                
        return current_longest