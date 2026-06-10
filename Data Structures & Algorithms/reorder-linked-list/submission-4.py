# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def recLink(self, ep):

        if not ep.next:
            self.count += 1
            self.count = (self.count + 2 - 1) // 2
            return ep

        self.count += 1

        old_ep = self.recLink(ep.next)
        self.count -= 1

        if self.count > 0:
            tmp = self.head.next
            self.head.next = old_ep
            old_ep.next = tmp
            self.head = tmp
            return ep
        elif self.count == 0:
            old_ep.next = None
            self.count -= 1
            return ep
        else:
            return 

    def reorderList(self, head: Optional[ListNode]) -> None:
        ep = self.head = head
        self.count = 0
        self.recLink(ep)
        return

