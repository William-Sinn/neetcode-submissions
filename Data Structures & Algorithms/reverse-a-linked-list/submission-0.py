# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return
            
        next_node = head.next 
        head.next = None
        while next_node != None:
            next_node_next = next_node.next
            next_node.next = head
            head = next_node
            next_node = next_node_next

        return head




        