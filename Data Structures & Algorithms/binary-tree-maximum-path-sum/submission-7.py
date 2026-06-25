class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')
        self.recSum(root)
        return self.max_sum

    
    def recSum(self, root):
        if not root.left and not root.right:
            self.max_sum = max(self.max_sum, root.val)
            return root.val
        left = float('-inf')
        if root.left:
            left = self.recSum(root.left)
        
        right = float('-inf')
        if root.right:
            right = self.recSum(root.right)
    
        self.max_sum = max(self.max_sum, 
                           root.val,
                           root.val + left,
                           root.val + right,
                           root.val + left + right,
                           )

        return root.val + max(left, right, 0)
        

        

        