from collections import deque
from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        self.med = deque([])
        self.left = []
        self.right = []
        

    def addNum(self, num: int) -> None:
        if not len(self.med):
            self.med.append(num)
            return

        if len(self.med) == 1:
            if num < self.med[0]:
                heappush(self.left, -num)
                popped_left = -heappop(self.left)
                self.med.appendleft(popped_left)

            else:
                heappush(self.right, num)
                popped_right = heappop(self.right)
                self.med.append(popped_right)
            
            return
    
        if num < self.med[0]:
            heappush(self.left, -num)
            popped_right = self.med.pop()
            heappush(self.right, popped_right)
            return

        if num > self.med[-1]:
            heappush(self.right, num)
            popped_left = self.med.popleft()
            heappush(self.left, -popped_left)
            return
        
        popped_left = self.med.popleft()
        popped_right = self.med.pop()
        heappush(self.left, -popped_left)
        heappush(self.right, popped_right)
        self.med.append(num)

    def findMedian(self) -> float:
        return self.med[0] if len(self.med) == 1 else (self.med[0] + self.med[-1]) / 2
        
        