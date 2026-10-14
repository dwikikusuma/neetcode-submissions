from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        map_t = Counter(t)          
        map_r = {}                  
        need = len(map_t)          
        have = 0                   

        best = None                 
        l = 0

        for r in range(len(s)):
            c = s[r]
            map_r[c] = map_r.get(c, 0) + 1
            if c in map_t and map_r[c] == map_t[c]:
                have += 1

            while have == need:
                if best is None or r - l + 1 < best[1] - best[0] + 1:
                    best = (l, r)

                d = s[l]
                map_r[d] -= 1
                if d in map_t and map_r[d] < map_t[d]:
                    have -= 1
                l += 1

        return s[best[0]:best[1] + 1] if best else ""