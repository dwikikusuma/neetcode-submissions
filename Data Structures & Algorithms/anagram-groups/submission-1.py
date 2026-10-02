class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_anagram = {}

        for word in strs:
            sorted_w = "".join(sorted(word))
            
            if sorted_w not in grouped_anagram:
                grouped_anagram[sorted_w] = []
            
            grouped_anagram[sorted_w].append(word)

        return [val for _, val in grouped_anagram.items()]
