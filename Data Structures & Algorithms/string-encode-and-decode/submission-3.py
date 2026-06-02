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
            n = ""
            while s[i] != "#":
                n += s[i]
                i += 1
            i += 1
            n = int(n)
            d_str = s[i:n + i]
            d.append(d_str)
            i += n
        
        return d


