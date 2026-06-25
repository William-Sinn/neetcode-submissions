# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.found = None
        self.count = k
        self.recSearch(root)
        return self.found if not self.found else self.found.val

    def recSearch(self, root):
        if self.count <= 0:
            return 
        if not root.left and not root.right:
            self.count -= 1
            self.found = root
            return 
            
        if root.left:
            self.recSearch(root.left)
        
        if self.count > 0:
            self.count -= 1
            self.found = root
        
        if root.right:
            self.recSearch(root.right)
        
        return
        


