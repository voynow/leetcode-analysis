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
class Solution(object):
    def isSymmetric(self, root):

        def traverse_right(node, vals):
            if node:
                vals.append(node.val)
                vals = traverse_right(node.right, vals)
                vals = traverse_right(node.left, vals)
            else:
                vals.append(None)
            return vals

        def traverse_left(node, vals):
            if node:
                vals.append(node.val)
                vals = traverse_left(node.left, vals)
                vals = traverse_left(node.right, vals)
            else:
                vals.append(None)
            return vals

        l = traverse_left(root.left, [])
        r = traverse_right(root.right, [])

        return l == r