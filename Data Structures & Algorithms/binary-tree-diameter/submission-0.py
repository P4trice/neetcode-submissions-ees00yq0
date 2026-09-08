# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.best = 0
        if root is None:
            return 0

        def height(node):
            if node is None:
                return 0
            height_l = height(node.left)
            height_r = height(node.right)
            self.best = max(self.best, height_l + height_r) # biggest diameter scanning
            return 1 + max(height_l, height_r) # this returns the height of a node

        height(root)
        return self.best