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
        
        # while head.next:
        #     tmp = head.next
        #     head.next = sp.next
        #     head.next.next = 
        pp = None
        cp = sp.next

        while cp:
            np = cp.next
            cp.next = pp
            pp = cp
            cp = np
        
        while pp.next:
            print("pp.val", pp.val)
            print("head.val", head.val)
            htp = head.next
            ptp = pp.next
            if head:
                head.next = pp 
                pp.next = htp

            pp = ptp
            head = htp

        # print(sp.val)
        return 
