# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        depth = 0

        q = [root]
        while root and q:  # while root handles for root = None
            depth += 1

            q_len = len(q)
            for _ in range(q_len):
                node = q.pop(0)  # must pop from the front of the queue
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return depth