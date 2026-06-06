# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 or list2

        if list1.val <= list2.val:
            next_node = self.mergeTwoLists(list1.next, list2)
            list1.next = next_node
            return list1

        else:
            next_node = self.mergeTwoLists(list1, list2.next)
            list2.next = next_node
            return list2
        

