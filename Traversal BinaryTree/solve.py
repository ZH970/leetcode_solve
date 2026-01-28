# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxd = 0
    def Traversal(self, root:Optional[TreeNode], depth:int):
        if root is None: return depth
        now = depth+1
        if now > self.maxd: self.maxd = now
        self.Traversal(root.left,now)
        self.Traversal(root.right,now)


        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.Traversal(root,0)
        return self.maxd
        