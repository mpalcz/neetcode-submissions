# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        def comp(node, target):
            if not node and not target:
                return True
            elif (not node and target) or (node and not target):
                return False
            elif node.val != target.val:
                return False
            else:
                return comp(node.left, target.left) and comp(node.right, target.right)
        
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if comp(node, subRoot):
                return True
            if not node:
                continue
            queue.append(node.right)
            queue.append(node.left)
        return False

