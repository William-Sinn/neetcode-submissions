class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_count = 0
        char_dict = {}
        max_freq = 0
        l = r = 0

        while r < len(s):
            char_dict[s[r]] = char_dict.get(s[r], 0) + 1
            max_freq = max(max_freq, char_dict[s[r]])

            while (r - l + 1 - max_freq) > k:
                char_dict[s[l]] -= 1
                l += 1
            
            max_count = max(max_count, r - l + 1)
            r += 1

        return max_count

        