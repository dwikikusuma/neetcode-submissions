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
        for i in s2[:r]:
            i_ord = ord(i) - ord("a")
            window_key[i_ord] += 1

        if window_key == s1_key:
            return True

        print(f"reserved: {s2[:r]}")
        for l in range(r, len(s2)):
            print(f"new_key: {s2[l]}")
            print(f"rem_key: {s2[l-len(s1)]}")
            l_ord = ord(s2[l]) - ord("a")
            del_ord = ord(s2[l-len(s1)]) - ord("a")

            window_key[l_ord] += 1
            window_key[del_ord] -= 1
            print(window_key)
            if window_key == s1_key:
                return True
        
        return False

