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
            # print(node_queue)
            if last_node == node:
                last_node = None
                layer += 1

            # if node.val == 4:
            #     print("node.left: ", node.left.val)
            #     print("node.right: ", node.right.val)
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
        
        print(ser)
        return "".join(ser)


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        node_queue = deque()

        layer, discard, data = data.partition("%")
        val, discard, data = data.partition("|")

        node = TreeNode(val=val) if val else None
        root = node
        node_queue.append(node)

        while data:
            lq = len(node_queue)

            for i in range(lq):
                node = node_queue.popleft()
                discard, discard, data = data.partition("%")
                val, discard, data = data.partition("|")
                node.left = TreeNode(val=val) if val else None

                discard, discard, data = data.partition("%")
                val, discard, data = data.partition("|")
                node.right = TreeNode(val=val) if val else None

                if node.left:
                    node_queue.append(node.left)

                
                if node.right:
                    node_queue.append(node.right)

        return root









