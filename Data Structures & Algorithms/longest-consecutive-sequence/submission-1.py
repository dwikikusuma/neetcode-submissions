class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0

        for num in nums:
            if num-1 not in nums:
                start = num
                counter = 1
                while start+1 in nums:
                    counter += 1
                    start += 1

                longest = max(longest, counter)
        
        return longest

