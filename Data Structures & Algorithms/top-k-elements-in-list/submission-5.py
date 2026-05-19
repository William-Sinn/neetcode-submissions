class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket_groups = [set()] 
        seen = {}
        last_group = 0
        max_group = 0
        
        for num in nums:
            if num not in seen:
                seen[num] = 1
                bucket_groups[0].add(num)
                last_group = 1
            else:
                bucket_groups[seen[num] - 1].remove(num)
                seen[num] += 1
                if seen[num] > max_group:
                    bucket_groups.append(set())
                bucket_groups[seen[num] - 1].add(num)
                last_group = seen[num]
            if last_group > max_group:
                max_group = last_group


        out = []
        while len(out) < k:
            out.extend(list(bucket_groups[max_group - 1]))
            max_group -= 1

        return out



            



