# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class NotEqual(Exception): 
    pass

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        try:
            self.recComp(p, q)
            return True
        except NotEqual as e:
            return False


    def recComp(self, p, q):
        if not p and not q:
            return
        if not p or not q or p.val != q.val:
            raise NotEqual(False)
        
        self.recComp(p.left, q.left)
        self.recComp(p.right, q.right)
        