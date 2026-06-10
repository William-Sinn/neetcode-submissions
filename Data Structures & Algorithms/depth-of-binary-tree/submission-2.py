# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.recCount(0, root)

    def recCount(self, count, root):
        if not root:
            return count
        count += 1
        
        if not root.left and not root.right:
            return count
        
        l_count = self.recCount(count, root.left)
        r_count = self.recCount(count, root.right)

        return max(l_count, r_count)

        