class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}

        for num in nums:
            if num not in counter:
                counter[num] = 0
            
            counter[num] += 1
        
        sorted_counter = dict(sorted(counter.items(), key=lambda item: item[1], reverse=True))
        return list(sorted_counter)[:k]