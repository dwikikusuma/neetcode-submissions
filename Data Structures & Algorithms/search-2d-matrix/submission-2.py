class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for mat in matrix:
            if mat[0] <= target <= mat[-1]:
                l = 0
                r = len(mat) - 1

                while l <= r:
                    mid = (l + r) // 2
                    mid_val = mat[mid]

                    if mid_val > target:
                        r = mid - 1
                    elif mid_val < target:
                        l = mid + 1
                    else:
                        return True

        return False