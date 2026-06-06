# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_head = list1
        if not new_head or list2 and new_head.val > list2.val:
            new_head = list2
            list2 = None if not list2 else list2.next
        elif list1:
            list1 = list1.next

        curr = new_head

        while list1 and list2:
            if list1.val >= curr.val and list1.val <= list2.val:
                curr.next = list1
                curr = curr.next
                list1 = list1.next
            else:
                curr.next = list2
                curr = curr.next
                list2 = list2.next

        if curr:
            curr.next = list1 or list2
        
        return new_head
