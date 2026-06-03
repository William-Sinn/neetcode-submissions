class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        par = {'(' : ')', '{' : '}', '[' : ']'}

        for c in s:
            if c in par:
                stack.append(c)
                continue
            
            elif len(stack) > 0 and c == par[stack[-1]]:
                stack.pop()
            else:
                return False
        
        return len(stack) == 0
        