# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fp = sp = head
        
        while fp != None and fp.next:
            fp = fp.next.next
            if fp == sp:
                return True
            sp = sp.next 

        return False
        