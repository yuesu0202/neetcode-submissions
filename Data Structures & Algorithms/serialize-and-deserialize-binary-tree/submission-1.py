# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Codec:
    
#     # Encodes a tree to a single string.
#     def serialize(self, root: Optional[TreeNode]) -> str:
#         res = []
#         def dfs(node):
#             if not node:
#                 res.append("N")
#                 return
#             res.append(str(node.val))
#             dfs(node.left)
#             dfs(node.right)
#         dfs(root)
#         return ",".join(res)
        
#     # Decodes your encoded data to tree.
#     def deserialize(self, data: str) -> Optional[TreeNode]:
#         val = data.split(",")
#         self.i = 0
#         def dfs():
#             if val[self.i] == "N":
#                 self.i += 1
#                 return
#             node = TreeNode(int(val[self.i]))
#             self.i += 1
#             node.left = dfs()
#             node.right = dfs()
#             return node
#         return dfs()

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def dfs(node):
            if not node:
                res.append('N')
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.i = 0
        val = data.split(",")

        def dfs():
            if val[self.i] == "N":
                self.i += 1
                return
            node = TreeNode(int(val[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs() 