"""
Runtime: 36 ms, faster than 66.91% of Python online submissions for Diameter of Binary Tree.
Memory Usage: 16.8 MB, less than 6.62% of Python online submissions for Diameter of Binary Tree.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # initialize diameter
        self.diameter = 0

        def depth(node):
            if node is None:
                return 0

            # depth first search right, left
            rightmax = depth(node.right)
            leftmax = depth(node.left)

            # diameter either stays the same or is sum of left and right diameters
            self.diameter = max(self.diameter, leftmax + rightmax)

            # return max depth of two subtrees
            return max(leftmax, rightmax) + 1
        
        depth(root)
        return self.diameter
        