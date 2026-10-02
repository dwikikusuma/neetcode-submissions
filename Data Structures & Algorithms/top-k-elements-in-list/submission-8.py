class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}

        for num in nums:
            if num not in counter:
                counter[num] = 0
            
            counter[num] += 1
        
        bucket = [[] for _ in range(len(nums)+1)]
        for key, value in counter.items():
            bucket[value].append(key)

        k_counter = 0
        result = []
        for i in bucket[::-1]:
            if k_counter == k:
                break

            if i:
                result += i
                k_counter += len(i)
                
        
        return result