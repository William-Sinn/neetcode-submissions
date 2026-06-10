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
        
        for i in range(len(lists)):
            while lists[i]:
                heapq.heappush(min_heap, NodeWrapper(lists[i]))
                lists[i] = lists[i].next              

        i = 20
        while len(min_heap):
            nxt = heapq.heappop(min_heap).node
            curr.next = nxt
            curr = curr.next
            # print(nxt.val)
            # i -= 1
            # if not i:
            #     return head
        
        return head.next
