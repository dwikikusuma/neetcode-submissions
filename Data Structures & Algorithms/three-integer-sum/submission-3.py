class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        result = []
        prev_num = None
        n = len(sorted_nums)
        for num in range(len(sorted_nums)):
            fixed_num = sorted_nums[num]
            if fixed_num == prev_num:
                continue
            
            l = num+1
            r = len(sorted_nums)-1
            while l < r:
                move_l = False
                move_r = False
                sums = sorted_nums[l] + sorted_nums[r] + fixed_num
                if sums == 0:
                    result.append([sorted_nums[l],sorted_nums[r],fixed_num])
                    move_l = True
                    move_r = True
                elif sums < 0:
                    move_l = True

                else:
                    move_r = True
  
                
                if move_l:
                    move = 1
                    while sorted_nums[l] == sorted_nums[l+move]:
                        move += 1
                        if move >= n-1:
                            break
                    l+=move
                    
                if move_r:
                    move = -1   
                    while sorted_nums[r] == sorted_nums[r+move]:
                        move += -1
                        if abs(move) >= n-1:
                            break
                    r+=move

            prev_num = fixed_num
        return result

        