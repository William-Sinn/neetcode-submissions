# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode()
        dummy.next = head
        sp = fp = dummy

        while fp.next and fp.next.next:
            fp = fp.next.next
            sp = sp.next
        
        pp = None
        cp = sp.next

        while cp:
            np = cp.next
            cp.next = pp
            pp = cp
            cp = np
        
        while pp.next:
            htp = head.next
            ptp = pp.next
            if head:
                head.next = pp 
                pp.next = htp

            pp = ptp
            head = htp

        return 
