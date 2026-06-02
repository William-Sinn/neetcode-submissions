class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [0] * n

        pref[0] = 1
        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]

        suff = 1
        for i in range(n - 2, -1, -1):
            pref[i] = nums[i + 1] * suff * pref[i]
            suff = suff * nums[i + 1]
        
        return pref        