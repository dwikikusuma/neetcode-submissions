class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for i in nums_set:
            if i-1 not in nums_set:
                counter = 1
                start = i
                while start+1 in nums_set:
                    counter += 1
                    start += 1

                if counter > longest:
                    longest = counter
        
        return longest

