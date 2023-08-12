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