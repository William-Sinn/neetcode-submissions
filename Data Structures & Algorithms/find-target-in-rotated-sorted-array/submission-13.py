class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        print(nums[l])
        mod = len(nums)
        r = l - 1 if l < 0 else mod - 1
        r += l
        l = l % mod
        while l < r:
            m = (l + r) // 2
            print(nums[l % mod], nums[m % mod], nums[r % mod])


            if nums[m % mod] == target:
                return m % mod

            if nums[m % mod] < target:
                l = m + 1
                if nums[l % mod] == target:
                    return l % mod
            else:
                r = m

        return -1
        