# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def findDepth(node):
            nonlocal res
            if not node:
                return 0
            leftDepth = findDepth(node.left)
            rightDepth = findDepth(node.right)
            res = max(res, leftDepth + rightDepth)
            return 1 + max(leftDepth, rightDepth)
        findDepth(root)
        return res