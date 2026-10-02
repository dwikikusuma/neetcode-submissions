class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_anagram = {}

        for word in strs:
            slot = [0]*26

            for c in word:
                slot[ord(c) - ord('a')] += 1
            
            hashable = tuple(slot)
            if hashable not in grouped_anagram:
                grouped_anagram[hashable] = []
            
            grouped_anagram[hashable].append(word)
        
        return list(grouped_anagram.values())