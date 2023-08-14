"""
242. Valid Anagram
Easy
10.1K
321
Companies
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        count = {}

        for ch in s:
            if ch not in count:
                count[ch] = 0
            count[ch] += 1

        for ch in t:
            if ch not in count:
                return False
            count[ch]-= 1
            if count[ch] == 0:
                del count[ch]

        return count == {}