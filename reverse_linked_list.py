# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        p1 = None
        p2 = head

        while p2:

            p2_next_temp = p2.next
            p2.next = p1

            p1 = p2
            p2 = p2_next_temp
        
        return p1


