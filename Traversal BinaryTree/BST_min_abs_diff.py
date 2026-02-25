# 二叉搜索树的最小绝对差

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.last = []
        self.now = 0
        self.diff = 1000000
    def Traversal(self, root:Optional[TreeNode], last:int=-10):
        if root is None: return self.diff
        if len(self.last) == 0: self.last.append(last)
        else: 
            if last != self.last[-1]:
                self.last.append(last)
        self.Traversal(root.left,root.val)
        for i in self.last:
            self.now = abs(root.val - i)
            if self.now < self.diff: self.diff = self.now
        self.Traversal(root.right,root.val)
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.Traversal(root)
        return self.diff