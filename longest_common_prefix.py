"""
Runtime: 24 ms, faster than 81.42% of Python online submissions for Longest Common Prefix.
Memory Usage: 13.7 MB, less than 59.32% of Python online submissions for Longest Common Prefix.
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