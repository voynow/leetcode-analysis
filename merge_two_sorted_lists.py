# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        merged_list = return_head = ListNode()

        p1 = list1
        p2 = list2
        
        while p1 and p2:
            if p1.val > p2.val:
                merged_list.next = p2
                merged_list = merged_list.next
                p2 = p2.next
            else:
                merged_list.next = p1
                merged_list = merged_list.next
                p1 = p1.next

        if p1:
            merged_list.next = p1
        if p2:
            merged_list.next = p2

        return return_head.next

