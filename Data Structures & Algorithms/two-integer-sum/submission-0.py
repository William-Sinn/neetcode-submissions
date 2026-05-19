class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_sum_hash_map = {}

        for i, num in enumerate(nums):
            if num in target_sum_hash_map:
                return [target_sum_hash_map[num], i]
            
            target_sum_hash_map[target - num] = i
