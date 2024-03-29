"""
101. Symmetric Tree
Easy

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
 

Follow up: Could you solve it both recursively and iteratively?
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class RecursiveSolution(object):
    def isSymmetric(self, root):

        def compare(l, r):
            if l is None and r is None:
                return True
            if l is None and r is not None or r is None and l is not None:
                return False
            if l.val != r.val:
                return False
            return compare(l.left, r.right) and compare(l.right, r.left)

        return compare(root.left, root.right)
    

class IterativeSolution(object):
    def isSymmetric(self, root):

        q = [root.left, root.right]

        while q:
            lnode = q.pop(0)
            rnode = q.pop(0)
            
            if lnode is None and rnode is None:
                continue
            elif lnode is None or rnode is None or lnode.val != rnode.val:
                return False
            else:
                q.extend([lnode.left, rnode.right, lnode.right, rnode.left])

        return True
