class Solution:
    def calcWater(self, le, ri, dist):
        low = le if le < ri else ri
        return low * dist

    def maxArea(self, heights: List[int]) -> int:
        high = max(heights)
        h_index = heights.index(high)
                
        l_index = 0 if heights[0] > heights[-1] else len(heights) - 1
        long = heights[l_index]

        l = 0
        r = len(heights) - 1
        max_water = 0

        while l < l_index:
            water = self.calcWater(heights[l], long, l_index - l)
            if water > max_water:
                max_water = water
            l += 1
        
        while r > l_index:
            water = self.calcWater(heights[r], long, r - l_index)
            if water > max_water:
                max_water = water
            r -= 1

        while l < h_index:
            water = self.calcWater(heights[l], high, h_index - l)
            if water > max_water:
                max_water = water
            l += 1
        
        while r > h_index:
            water = self.calcWater(heights[r], high, r - h_index)
            if water > max_water:
                max_water = water
            r -= 1

        return max_water
        