# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        num_good = 0
        current_max = root.val

        def dfs(node, cur_max):
            nonlocal num_good
            if not node:
                return
            if node.val >= cur_max:
                num_good += 1
                cur_max = node.val
            dfs(node.left, cur_max)
            dfs(node.right, cur_max)
            return

        dfs(root, current_max)
        return num_good
            