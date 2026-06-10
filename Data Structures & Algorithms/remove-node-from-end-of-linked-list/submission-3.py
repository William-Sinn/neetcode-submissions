# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        curr = head

        while curr.next:
            count += 1
            curr = curr.next

        count -= n
        count += 1
        
        curr = head
        dummy = ListNode()
        dummy.next = head
        prev = dummy

        while count:
            prev = curr
            curr = curr.next
            count -= 1
        
        prev.next = curr.next

        return dummy.next
