from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        c_dict = {}
        m_set = {}
        l = 0
        r = 0
        count = float('inf')
        cord = ()

        t_dict = dict(Counter(t))
        m_set = set(t_dict)

        while r < len(s):

            c_dict[s[r]] = c_dict.get(s[r], 0) + 1

            if s[r] in t_dict and c_dict[s[r]] >= t_dict[s[r]]:
                m_set.discard(s[r])

                if len(m_set) == 0 and (r - l + 1) < count:
                    count = r - l + 1
                    cord = (l , r)


            while len(m_set) == 0:

                if len(m_set) == 0 and (r - l + 1) < count:
                    count = r - l + 1
                    cord = (l , r)

                c_dict[s[l]] -= 1

                if s[l] in t_dict and c_dict[s[l]] < t_dict[s[l]]:
                    m_set.add(s[l])

                l += 1
            
            r += 1

        return s[cord[0]: cord[1] + 1] if cord != () else ""




        