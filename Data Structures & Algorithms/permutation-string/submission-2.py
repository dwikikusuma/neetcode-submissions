class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        l = 0
        r = len(s1)
        s1_key = [0]*26
        for i in s1:
            ord_num = ord(i) - ord("a")
            s1_key[ord_num] += 1

        for l in range(len(s2)-r+1):
            window_key = [0]*26
            windowed_c = s2[l:l+r]
            for c in windowed_c:
                c_ord = ord(c) - ord("a")
                window_key[c_ord] += 1
            
            if window_key == s1_key:
                return True
        
        return False

