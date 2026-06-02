class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1

        print(end)

        while start < end:
            while start < end and not (s[end].isalpha() or s[end].isnumeric()):
                end -= 1
            
            while end > start and not (s[start].isalpha() or s[start].isnumeric()):
                start += 1

            if s[start].lower() != s[end].lower():
                return False

            start += 1
            end -= 1

        return True 

