# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        q = deque()
        q.append(root)

        while q:
            for i in range(len(q)):
                out = True
                node = q.popleft()
                subNode= subRoot

                nodeq = deque()
                subNodeq = deque()
                nodeq.append(node)
                subNodeq.append(subNode)

                while out and nodeq and subNodeq:
                    for i in range(len(nodeq)):
                        nodeq_node = nodeq.popleft()
                        subNodeq_node = subNodeq.popleft()
                        if not nodeq_node and not subNodeq_node:
                            continue
                        if nodeq_node and not subNodeq_node or not nodeq_node and subNodeq_node or nodeq_node.val != subNodeq_node.val:
                            out = False
                            break
                        nodeq.append(nodeq_node.left)
                        nodeq.append(nodeq_node.right)
                        subNodeq.append(subNodeq_node.left)
                        subNodeq.append(subNodeq_node.right)

                if out:
                    return True
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return False


        
