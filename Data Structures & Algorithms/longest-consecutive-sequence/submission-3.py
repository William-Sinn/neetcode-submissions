class Solution:
    def rec_climb(self, k, nd, r):
        nd[k] = r
        if k + 1 in nd:
            return self.rec_climb(k + 1, nd, r)
        return k

    def longestConsecutive(self, nums: List[int]) -> int:
        sd = dict.fromkeys(nums, 0)
        max_count = 0

        for num in nums:
            max_count = 1 if max_count == 0 else max_count
            if not sd[num]:
                if num + 1 not in sd:
                    pass
                else:
                    if not sd[num + 1]:
                        sd[num] = self.rec_climb(num + 1, sd, num)

                    else:
                        sd[num] = sd[num + 1]
                        sd[num + 1] = num
                    count = sd[num] - num + 1
                    if count > max_count:
                        max_count = count
            
            else:
                pass

        print(sd)
        return max_count
        