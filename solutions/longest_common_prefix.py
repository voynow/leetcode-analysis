"""
14. Longest Common Prefix
Easy

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        prefix = ""
        prefix_len = len(prefix)
        min_len = min(len(s) for s in strs)
        
        # iterate until index out of bounds
        while prefix_len < min_len:

            # select current char
            ch = strs[0][prefix_len]
            break_loop = False
            
            # check every string contains common char
            for s in strs:
                if s[prefix_len] != ch:
                    break_loop = True

            # if char is missing anywhere, break loop
            if break_loop:
                break

            # add new char and increment index
            else:
                prefix += ch
                prefix_len += 1

        return prefix