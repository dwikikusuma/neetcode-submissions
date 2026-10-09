class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        area = 0

        while l < r:
            min_bar = min(heights[l], heights[r])
            area = max(area, min_bar * (r-l))
            if heights[l] > heights[r]:
                r-=1
            else:
                l+=1
        
        return area