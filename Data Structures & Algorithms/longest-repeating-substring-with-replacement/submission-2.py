class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {}
        longest = 0
        l = 0

        for r in range(len(s)):
            if s[r] not in counter:
                counter[s[r]] = 0

            counter[s[r]] += 1
            max_counter = max(counter.values())

            while (r-l+1) > max_counter + k:
                counter[s[l]] -= 1
                l += 1
            
            longest = max(longest, r-l+1)
        return longest

            
            