from math import prod
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []
        out = []

        for i, num in enumerate(nums):
            prefix.append(prod(nums[i+1:]))
        
        for i, num in enumerate(reversed(nums)):
            i -= len(nums)
            suffix.append(prod(nums[:i]))

        for i, num in enumerate(prefix):
            out.append(num * suffix[i])
        
        return out
        