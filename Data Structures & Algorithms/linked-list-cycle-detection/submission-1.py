# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node_set = set()
        
        while head and head.next != None:
            if head in node_set:
                return True
            else:
                node_set.add(head)
                head = head.next

        return False
        