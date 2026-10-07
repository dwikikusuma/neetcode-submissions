class Solution:
    def trap(self, height: List[int]) -> int:
        tallest_bar = height.index(max(height))
        drop = 0
        l = 0
        r = len(height)-1
        
        w = 0
        while l < tallest_bar:
            w=max(w, height[l])
            drop += abs(height[l] - w)
            
            l+=1

        w = 0
        while r > tallest_bar:
            w=max(w, height[r])
            drop += abs(height[r] - w)
            r-=1
        
        return drop