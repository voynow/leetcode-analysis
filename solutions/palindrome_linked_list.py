"""
Runtime: 1529 ms, faster than 30.10% of Python online submissions for Palindrome Linked List.
Memory Usage: 85.4 MB, less than 25.97% of Python online submissions for Palindrome Linked
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # edge case for None input
        if not head:
            return False

        # convert LinkedList into List
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        
        # compare first and (reversed) second half
        # logic is slightly different for list length even or odd
        half_idx = len(vals) // 2
        if len(vals) % 2: 
            return vals[:half_idx + 1] == vals[half_idx:][::-1]
        else:
            return vals[:half_idx] == vals[half_idx:][::-1]
        