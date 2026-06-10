# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        else:
            return self.divideLists(lists, 0, len(lists) - 1)


    def divideLists(self, lists, l, r):
        if l > r:
            return None
        if l == r:
            return lists[l]
            
        mid = (l + r) // 2
        left = self.divideLists(lists, l, mid)
        right = self.divideLists(lists, mid + 1, r)
        
        return self.conquerLists(lists, left, right)

    def conquerLists(self, lists, l, r):
        head = ListNode()
        curr = head

        while l and r:
            if l.val < r.val:
                curr.next = l
                l = l.next
                curr = curr.next
            else:
                curr.next = r
                r = r.next
                curr = curr.next        
        if l:
            curr.next = l
        if r:
            curr.next = r

        return head.next
