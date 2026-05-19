class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = {nums[0]: 0}
        out = {nums[0]}
        prev_min = nums[0]

        for num in nums:
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1

            out.add(num)
            if len(out) > k:
                out.discard(min(out, key=num_count.get))
        return list(out)
