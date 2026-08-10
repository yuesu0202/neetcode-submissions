# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        node = root

        def dfs(node, p, q):
            if not node or p == node or q == node:
                return node
            if (max(p.val, q.val) < node.val):
                left = dfs(node.left, p, q)
                return left
            if (min(p.val, q.val) > node.val):
                right = dfs(node.right, p, q)
                return right
            else:
                return node
        return dfs(node, p, q)
            