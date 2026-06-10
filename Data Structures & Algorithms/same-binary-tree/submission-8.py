# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = deque()
        q2 = deque()
        q1.append(p)
        q2.append(q)

        while q1 and q2:
            for i in range(len(q1)):
                nodep = q1.popleft()
                nodeq = q2.popleft()

                if not nodep and not nodeq:
                    continue
                if nodep and not nodeq or not nodep and nodeq or nodep.val != nodeq.val:
                    return False

                q1.append(nodep.left)
                q1.append(nodep.right)
                q2.append(nodeq.left)
                q2.append(nodeq.right)

        
        return True


        