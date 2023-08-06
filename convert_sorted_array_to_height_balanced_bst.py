# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        def create_tree(nums):
            if not nums:
                return None
        
            center_idx = len(nums) // 2
            c = nums[center_idx]
            l = nums[:center_idx]
            r = nums[center_idx + 1:]

            root = TreeNode(c)
            root.left = create_tree(l)
            root.right = create_tree(r)

            return root

        return create_tree(nums)
