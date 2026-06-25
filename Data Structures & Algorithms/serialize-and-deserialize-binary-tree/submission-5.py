from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    def __init__(self):
        data = None
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ser = []
        node_queue = deque()
        node_queue.append(root)
        layer = 0
        last_node = None

        while root and node_queue:
            node = node_queue.popleft()
            if last_node == node:
                last_node = None
                layer += 1

            if node == '':
                ser.append(str(layer + 1) + "%" + "|")
                continue

            ser.append(str(layer) + "%" + str(node.val) + "|")

            if node.left:
                node_queue.append(node.left)
                last_node = node.left if not last_node else last_node
            else:
                node_queue.append('')

            if node.right:
                node_queue.append(node.right)
                last_node = node.right if not last_node else last_node
            else:
                node_queue.append('')
        
        return "".join(ser)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        node_queue = deque()

        tokens = deque(data.split("|")[:-1])
        if not tokens:
            return None
        layer, val = tokens.popleft().split("%")

        node = TreeNode(val=val) if val else None
        root = node
        node_queue.append(node)

        for i in range(len(tokens)):
            lq = len(node_queue)
            for i in range(lq):
                node = node_queue.popleft()
                val = tokens.popleft().split("%")[1]
                node.left = TreeNode(val=int(val)) if val else None

                val = tokens.popleft().split("%")[1]
                node.right = TreeNode(val=int(val)) if val else None

                if node.left:
                    node_queue.append(node.left)
                
                if node.right:
                    node_queue.append(node.right)

        return root









