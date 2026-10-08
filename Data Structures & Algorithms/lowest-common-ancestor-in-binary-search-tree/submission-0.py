# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return root

        numDescendants = {}

        def isAncestor(root, node, first, second):
            if not node:
                return False
            elif node.val == first.val or node.val == second.val:
                numDescendants[root.val] += 1
                if numDescendants[root.val] == 2:
                    return True
            return isAncestor(root, node.left, first, second) or isAncestor(root, node.right, first, second)
            

        queue = deque()
        queue.append(root)
        last_valid = None
        while queue:
            node = queue.popleft()
            if not node:
                continue
            numDescendants[node.val] = 0
            if isAncestor(node, node, p, q):
                last_valid = node
            queue.append(node.left)
            queue.append(node.right)
        return last_valid
