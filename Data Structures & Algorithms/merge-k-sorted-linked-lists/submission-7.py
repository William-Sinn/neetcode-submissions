# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode()
        curr = head

        while True:
            nxt = -1
            curr_min = float("inf")

            for i in range(len(lists)):
                if lists[i] and lists[i].val < curr_min:
                    nxt = i
                    curr_min = lists[i].val

            if nxt == -1:
                break

            curr.next = lists[nxt]
            curr = lists[nxt]
            lists[nxt] = lists[nxt].next

        return head.next