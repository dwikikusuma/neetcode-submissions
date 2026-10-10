class Solution:
    def trap(self, height: List[int]) -> int:
        tallest_bar = height.index(max(height))

        tank = 0 
        
        wall = 0
        for i in range(0, tallest_bar):
            h = height[i]
            wall = max(wall, h)
            water = wall - h
            tank += water
            
        
        wall = 0
        for i in range(len(height)-1, tallest_bar, -1):
            h = height[i]
            wall = max(wall, h)
            water = wall - h
            tank += water
            
        return tank
