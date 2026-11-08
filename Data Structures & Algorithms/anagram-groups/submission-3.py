class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pair = {}

        for word in strs:
            sorted_w = str(sorted(word))
            if sorted_w not in pair:
                pair[sorted_w] = []
                
            pair[sorted_w].append(word)

        return list(pair.values())

