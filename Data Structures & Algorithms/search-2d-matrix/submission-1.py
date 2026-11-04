class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for mat in matrix:
            if mat[0] <= target <= mat[-1]:
                for v in mat:
                    if v == target:
                        return True
        
        return False