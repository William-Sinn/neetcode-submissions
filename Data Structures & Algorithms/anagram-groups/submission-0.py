class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_group_map = {}
        out_groups = []

        for s in strs:
            alpha_list = [0] * 26
            for c in s:
                alpha_index = ord(c) - 97
                alpha_list[alpha_index] += 1
            alpha_tup = tuple(alpha_list)
                
            if alpha_tup in anagram_group_map:
                out_index = anagram_group_map[alpha_tup]
                out_groups[out_index].append(s)
            else:
                anagram_group_map[alpha_tup] = len(out_groups)
                out_groups.append([s])

        return out_groups
        