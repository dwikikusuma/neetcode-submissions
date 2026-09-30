class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        pairs = {}
        if len(s) != len(t):
            return False
            
        for i in t:
            if i not in pairs:
                pairs[i] = 0
            pairs[i] = pairs[i] + 1
        
        for i in s:
            if i not in pairs:
                return False
            
            val = pairs[i]
            if val == 0:
                return False
            
            pairs[i] = val - 1

        return True