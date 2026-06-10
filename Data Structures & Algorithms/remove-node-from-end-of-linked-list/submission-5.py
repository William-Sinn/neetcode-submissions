# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fp = head
        sp = ListNode()
        dummy = ListNode()
        dummy.next = head
        sp = dummy

        while n - 1:
            fp = fp.next
            n -= 1
        
        while fp.next:
            fp = fp.next
            sp = sp.next

        sp.next = sp.next.next

        return dummy.next
