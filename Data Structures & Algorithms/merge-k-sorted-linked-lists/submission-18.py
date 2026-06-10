# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode()
        curr = head
        min_heap = []
        
        for l in lists:
            if l:
                heapq.heappush(min_heap, NodeWrapper(l))

        while len(min_heap):
            nxt = heapq.heappop(min_heap).node
            curr.next = nxt
            curr = curr.next
            if nxt.next:
                heapq.heappush(min_heap, NodeWrapper(nxt.next))
        
        return head.next
