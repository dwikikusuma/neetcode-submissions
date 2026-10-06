class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1

        max_area = 0

        while l < r:
            widht = r - l
            bar_height = min(heights[r], heights[l])
            area = bar_height * widht

            max_area = max(max_area, area)

            if heights[r] > heights[l]:
                l+=1
            else:
                r-=1
                
        return max_area