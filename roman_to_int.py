#  Forgot to record runtime/memory for this one
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        value_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        
        if len(s) == 1:
            return value_map[s[0]]
        
        l = 0
        r = 1
        total = 0
        
        while l < len(s) - 1:
            if value_map[s[l]] < value_map[s[r]]:
                total += value_map[s[r]] - value_map[s[l]]
                l += 2
                r += 2
            else:
                total += value_map[s[l]]
                l += 1
                r += 1
        
        if l > len(s) - 1:
            return total
        return total + value_map[s[l]]
        
# Runtime: 56 ms, faster than 63.17% of Python online submissions for Roman to Integer.
# Memory Usage: 13.6 MB, less than 30.90% of Python online submissions for Roman to Integer.
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        vmap = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        
        total = 0
        
        while s:
            if len(s) > 1:
                if vmap[s[0]] < vmap[s[1]]:
                    l = s[0]
                    r = s[1]
                    s = s[1:]
                    total += vmap[r] - vmap[l]
                else:
                    total += vmap[s[0]]
            else:
                total += vmap[s[0]]
            s = s[1:]
        return total
