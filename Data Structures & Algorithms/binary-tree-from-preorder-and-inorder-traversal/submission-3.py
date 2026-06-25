# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.inor_dict = {}
        self.po_pos = 0
        for i, node in enumerate(inorder):
            self.inor_dict[node] = i 

        return self.recBuild(preorder, inorder, 0, len(inorder))
    
    def recBuild(self, preorder, inorder, left, right):
        node = TreeNode(val=preorder[self.po_pos])

        if right - left == 0:
            return node
        
        mid = self.inor_dict[node.val]

        if mid != left and self.po_pos + 1 < len(preorder):
            self.po_pos += 1
            node.left = self.recBuild(preorder, inorder, left, mid - 1)


        if mid != right and self.po_pos  + 1 < len(preorder):
            self.po_pos += 1

            node.right = self.recBuild(preorder, inorder, mid + 1, right)
        
        return node



        



        

        






        