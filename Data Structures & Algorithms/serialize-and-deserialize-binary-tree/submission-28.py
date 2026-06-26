from collections import deque

class Codec:
    def __init__(self):
        data = None
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ser = []
        node_queue = deque()
        node_queue.append(root)

        while root and node_queue:
            node = node_queue.popleft()

            if node == '':
                ser.append("|")
                continue

            ser.append(str(node.val) + "|")

            if node.left:
                node_queue.append(node.left)
            else:
                node_queue.append('')

            if node.right:
                node_queue.append(node.right)
            else:
                node_queue.append('')
        
        return "".join(ser)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        node_queue = deque()
        tokens = data.split("|")[:-1]

        if not tokens:
            return None
            
        val = tokens[0]

        node = TreeNode(val=int(val)) if val else None
        root = node
        node_queue.append(node)

        i = 1
        while i < len(tokens):
            lq = len(node_queue)
            for x in range(lq):
                node = node_queue.popleft()
                val = tokens[i]
                i += 1
                node.left = TreeNode(val=int(val)) if val else None

                val = tokens[i]
                i += 1
                node.right = TreeNode(val=int(val)) if val else None

                if node.left:
                    node_queue.append(node.left)
                
                if node.right:
                    node_queue.append(node.right)

        return root









