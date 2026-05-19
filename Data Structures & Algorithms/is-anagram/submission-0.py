class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map_s = {}
        hash_map_t = {}

        for char in s:
            if char in hash_map_s:
                hash_map_s[char] += 1
            else:
                hash_map_s[char] = 1

        for char in t:
            if char not in hash_map_s:
                return False
            if char in hash_map_t:
                hash_map_t[char] += 1
            else:
                hash_map_t[char] = 1

        return hash_map_s == hash_map_t



            