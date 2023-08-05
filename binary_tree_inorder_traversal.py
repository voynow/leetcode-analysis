# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def traverse(node, vals):
            if node is None:
                return vals
                
            vals = traverse(node.left, vals)
            vals.append(node.val)
            vals = traverse(node.right, vals)

            return vals


        return traverse(root, [])