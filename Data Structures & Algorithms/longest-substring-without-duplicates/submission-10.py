class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        longest = 0

        l, r = 0, 0
        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
            else:
                while s[r] in seen:
                    seen.remove(s[l])
                    l+=1
            
            longest = max(len(seen), longest)
        
        return longest
            
