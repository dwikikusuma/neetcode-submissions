class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tmp = {}

        for idx,num in enumerate(nums):
            if num in tmp:
                return [tmp[num], idx]

            s = target - num
            tmp[s] = idx

        return [0]