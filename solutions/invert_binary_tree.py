"""
226. Invert Binary Tree
Easy

Given the root of a binary tree, invert the tree, and return its root.

 

Example 1:


Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
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