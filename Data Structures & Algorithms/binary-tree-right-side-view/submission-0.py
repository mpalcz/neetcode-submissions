# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque()
        level = 0
        queue.append((root, level))
        res = []
        while queue:
            node, lvl = queue.popleft()
            if not node:
                continue
            if not res:
                res.append(node.val)
            if len(res) - 1 < lvl:
                res.append(node.val)
            queue.append((node.right, lvl+1))
            queue.append((node.left, lvl+1))
        return res
