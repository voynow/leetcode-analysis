"""
234. Palindrome Linked List
Easy

Given the head of a singly linked list, return true if it is a 
palindrome
 or false otherwise.

 

Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false
 

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
 

Follow up: Could you do it in O(n) time and O(1) space?
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
        