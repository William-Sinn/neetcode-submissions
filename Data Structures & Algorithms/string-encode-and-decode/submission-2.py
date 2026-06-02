class Solution:

    def encode(self, strs: List[str]) -> str:
        e = ""
        for s in strs:
            e += str(len(s)) + "#" + s 
        
        return e

    def decode(self, s: str) -> List[str]:
        d = []

        i = 0 
        while i < len(s):
            n, s = s[i:].split("#", 1)
            n = int(n)
            d_str = s[:n]
            d.append(d_str)
            i = n
        
        return d


