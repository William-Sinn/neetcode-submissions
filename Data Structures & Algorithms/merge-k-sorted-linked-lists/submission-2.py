# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode()
        curr = head
        remain_set = set(range(len(lists)))

        while remain_set:
            # print(remain_set)
            curr_min = float("inf")

            for i in remain_set:
                if lists[i] and lists[i].val < curr_min:
                    nxt = i
                    curr_min = lists[i].val
                    # print(l.val)
                    # lists[i] = lists[i].next
                    # print(l.val)
            # print(nxt)
            # print(lists[nxt])
            if not lists[nxt]:
                remain_set.discard(nxt)
                break
            # print("Nxt",lists[nxt].val)
            # print(count)
                # print(lists[0].val)
            # x -= 1
            # if not x:
            #     break
            curr.next = lists[nxt]
            curr = lists[nxt]
            lists[nxt] = lists[nxt].next

        return head.next