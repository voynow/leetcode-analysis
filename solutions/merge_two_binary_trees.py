"""
617. Merge Two Binary Trees
Easy

You are given two binary trees root1 and root2.

Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

Return the merged tree.

Note: The merging process must start from the root nodes of both trees.

 

Example 1:


Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
Output: [3,4,5,5,4,null,7]
Example 2:

Input: root1 = [1], root2 = [1,2]
Output: [2,2]
 

Constraints:

The number of nodes in both trees is in the range [0, 2000].
-104 <= Node.val <= 104
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        
        def populate(merge_node, node):
            """
            postorder depth first search
            """

            # search left
            if node.left:
                # add node to master tree if node does not exist in master tree
                if merge_node.left is None:
                    merge_node.left = TreeNode()
                # recursive call
                populate(merge_node.left, node.left)

            # search right
            if node.right:
                # add node to master tree if node does not exist in master tree
                if merge_node.right is None:
                    merge_node.right = TreeNode()
                # recursive call
                populate(merge_node.right, node.right)

            # sum vals
            merge_node.val += node.val
            return
        
        # edge cases for empty trees
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        if root1 is None and root2 is None:
            return None
        
        # create master tree
        root_merge = TreeNode()

        # add trees onto master tree
        # this will work with any number of trees i.e.
        # for root in [root1, root2, root3, ... rootn]:
        #     populate(root_merge, root)
        populate(root_merge, root1)
        populate(root_merge, root2)
        return root_merge