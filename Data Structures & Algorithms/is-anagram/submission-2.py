class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n_s = len(s)
        n_t = len(t)

        if n_s != n_t:
            return False

        sorted_s = sorted(s)
        sorted_t = sorted(t)

        return sorted_s == sorted_t