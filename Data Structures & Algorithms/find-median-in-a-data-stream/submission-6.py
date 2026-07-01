from collections import deque
from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        self.med = None
        self.left = []
        self.right = []
        

    def addNum(self, num: int) -> None:
        if self.med == None:
            self.med = num
            return

        if self.med != "False":
            if num < self.med:
                heappush(self.left, -num)
                heappush(self.right, self.med)
                self.med = "False"

            else:
                heappush(self.right, num)
                heappush(self.left, -self.med)
                self.med = "False"
            
            return
    
        new_med = num
        if self.left and num < -self.left[0]:
            heappush(self.left, -num)
            left = -heappop(self.left)
            new_med = left

        elif self.right and num > self.right[0]:
            heappush(self.right, num)
            right = heappop(self.right)
            new_med = right
        
        self.med = new_med
        return

    def findMedian(self) -> float:
        return self.med if self.med != "False" else (-self.left[0] + self.right[0]) / 2
        
        