"""
Runtime: 29 ms, faster than 24.50% of Python online submissions for Invert Binary Tree.
Memory Usage: 13.1 MB, less than 99.29% of Python online submissions for Invert Binary Tree.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):

    def invertTree_BFS(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        # edge case for None input
        if not root:
            return None
        
        # initialize queue to contain root
        queue = [root]

        # BFS iterate over all layers
        while queue:
            
            # for each node in BFS layer
            for _ in range(len(queue)):

                # pop node, switch left and right children
                node = queue.pop(0)
                temp_left = node.left
                node.left = node.right
                node.right = temp_left
                
                # append childen to queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
        # return edited tree
        return root

    def invertTree_DFS(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # edge case for None input
        if not root:
            return None

        # switch left and right children
        temp_left = root.left
        root.left = root.right
        root.right = temp_left

        # DFS recursive calls to left and right children
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root