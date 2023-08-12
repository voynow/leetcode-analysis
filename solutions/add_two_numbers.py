"""
2. Add Two Numbers
Medium

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """        
        
        def linked_list_to_num(node):
            """
            Convert linked list into valid numerical representation
            """
            nums = []
            while node:
                nums.append(str(node.val))
                node = node.next
            
            # reverse vals, join as string, convert back to int
            nums.reverse()
            nums = "".join(nums)
            return int(nums)
        
        # add two numbers
        numerical_sum = sum([linked_list_to_num(node) for node in [l1, l2]])
        
        # create linked list
        root = ListNode()
        node = root
        
        # iterate over reversed chars of sum result
        for i, ch in enumerate(str(numerical_sum)[::-1]):
            node.val = int(ch)
            
            # do not create a new node
            if i != len(str(numerical_sum)) - 1:
                node.next = ListNode()
                node = node.next
        
        return root


    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # sums across linked lists
        sums = []
        while l1 or l2:
            
            # add sum of vals to sums
            if l1 and l2:
                sums.append(l1.val + l2.val)
                l1 = l1.next
                l2 = l2.next
                
            # add l1 val to sums
            elif not l1:
                sums.append(l2.val)
                l2 = l2.next
                
            # add l2 val to sums
            elif not l2:
                sums.append(l1.val)
                l1 = l1.next
        
        # "carry the one" like in elementary school 
        for i in range(len(sums)):
            if sums[i] >= 10:
                sums[i] -= 10
                if i == len(sums) - 1:
                    sums.append(1)
                else:
                    sums[i + 1] += 1        
                    
        # create linked list
        root = ListNode()
        node = root
        
        # iterate over sums
        for i, ch in enumerate(sums):
            node.val = ch
            
            # do not create a new node
            if i != len(sums) - 1:
                node.next = ListNode()
                node = node.next
        
        return root