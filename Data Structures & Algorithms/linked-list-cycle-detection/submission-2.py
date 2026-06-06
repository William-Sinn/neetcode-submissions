# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fp = sp = head
        sp_flag = False
        while fp != None:
            fp = fp.next
            if fp == sp:
                return True
            sp = sp.next if sp_flag else sp
            sp_flag = not sp_flag

        return False
        