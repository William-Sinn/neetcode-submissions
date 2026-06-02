class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_count = 0
        count = 0
        char_dict = {"": 0}
        max_char = ""
        l = r = 0

        while r < len(s):
            if s[r] not in char_dict:
                char_dict[s[r]] = 1
            else:
                char_dict[s[r]] += 1
            
            if char_dict[s[r]] >= char_dict[max_char]:
                max_char = s[r]
            count = r - l + 1

            if count - char_dict[max_char] <= k and count > max_count:
                max_count = count
            else:

                while count - char_dict[max_char] > k and l < r:
                    char_dict[s[l]] -= 1
                    count -= 1
                    l += 1
                    
                    if char_dict[s[r]] >= char_dict[max_char]:
                        max_char = s[r]

            r += 1

        return max_count

        