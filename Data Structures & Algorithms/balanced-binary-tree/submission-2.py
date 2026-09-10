# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # approach go down the tree recursively and report back the height of the subtrees until they're at the final node. If they're more than 1 different, return false, otherwise true

        def height(root):
            if root is None:
                return 0
            height_l, height_r = height(root.left), height(root.right)
            if abs(height_l - height_r) > 1:
                return -2
            return max(height_l, height_r) + 1

        if root is None:
            return True
        
        h_l = height(root.left)
        h_r = height(root.right)
        if abs(h_l - h_r) > 1 or h_l < 0 or h_r < 0:
            return False
        else:
            return True
