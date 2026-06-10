# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def recLink(self, ep):

        if not ep.next:
            self.count += 1
            self.count = (self.count + 2 - 1) // 2
            return ep

        self.count += 1

        # head = head.next
        old_ep = self.recLink(ep.next)
        # print("head",self.head.val)
        # print("old ep", old_ep.val)
        # print(self.count)
        # print("ep",ep.val)
        # print("test")
        # return
        self.count -= 1

        if self.count > 0:
            tmp = self.head.next
            # print("tmp", tmp.val)
            self.head.next = old_ep
            old_ep.next = tmp
            self.head = tmp
            return ep
        elif self.count == 0:
            old_ep.next = None
            print(ep.val)
            # print(self.count)
            # ep.next = None
            self.count -= 1
            return ep
        else:
            return 

    def reorderList(self, head: Optional[ListNode]) -> None:
        ep = head
        self.head = ListNode()
        self.head = head
        self.stop = head
        self.count = 0
        self.recLink(ep)
        # for i in range(10):
        #     print(self.stop.val)
        #     self.stop = self.stop.next
        # return 5
        return

