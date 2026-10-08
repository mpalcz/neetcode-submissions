# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p and not q) or (not p and q):
            return False
        to_visit_p = deque()
        to_visit_p.append(p)
        to_visit_q = deque()
        to_visit_q.append(q)

        while to_visit_p:
            if not to_visit_q:
                return False
            node_p = to_visit_p.popleft()
            node_q = to_visit_q.popleft()
            if not node_p and not node_q:
                continue

            if (not node_p and node_q) or (node_p and not node_q):
                return False
            if node_p.val != node_q.val:
                return False
            to_visit_p.append(node_p.left)
            to_visit_p.append(node_p.right)
            to_visit_q.append(node_q.left)
            to_visit_q.append(node_q.right)
        return True
