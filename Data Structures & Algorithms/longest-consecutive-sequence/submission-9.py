class Solution:
    def rec_climb(self, k, nd):
        if nd[k] is not None:
            return nd[k]
        t = self.rec_climb(k + 1, nd) if k + 1 in nd else k
        nd[k] = t
        return t

    def longestConsecutive(self, nums: List[int]) -> int:
        sd = dict.fromkeys(nums)
        max_count = 0

        for num in nums:
            max_count = 1 if max_count == 0 else max_count
            if sd[num] == None:
                if num + 1 not in sd:
                    pass
                else:
                    if sd[num + 1] == None:
                        sd[num] = self.rec_climb(num + 1, sd)

                    else:
                        sd[num] = sd[num + 1]
                        sd[num + 1] = num
                    count = sd[num] - num + 1
                    if count > max_count:
                        max_count = count
            
            else:
                pass

        return max_count
        