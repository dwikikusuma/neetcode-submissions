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
        
        window_key = [0]*26
        left_ord = None
        for l in range(len(s2)-r+1):
            windowed_c = s2[l:l+r]
            print(windowed_c)
            if l == 0:
                for c in windowed_c:
                    c_ord = ord(c) - ord("a")
                    window_key[c_ord] += 1
            else:
                window_key[left_ord] -= 1
                r_ord = ord(windowed_c[-1]) - ord("a")
                window_key[r_ord] += 1
            
            if window_key == s1_key:
                return True
            
            left_ord = ord(windowed_c[0]) - ord("a")

        return False

