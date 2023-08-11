"""
101. Symmetric Tree
Easy
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
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
            lqueue = []
            rqueue = []

            mid = len(q) // 2
            l = q[:mid]
            r = q[mid:]

            for _ in range(len(l)):
                q.pop()
                q.pop()
                lnode = l.pop(0)
                rnode = r.pop(0)
                
                if lnode is None and rnode is None:
                    continue
                elif lnode is None or rnode is None or lnode.val != rnode.val:
                    return False
                else:
                    lqueue.extend([lnode.left, lnode.right])
                    rqueue.extend([rnode.right, rnode.left])

            q.extend(lqueue + rqueue)

        return True
