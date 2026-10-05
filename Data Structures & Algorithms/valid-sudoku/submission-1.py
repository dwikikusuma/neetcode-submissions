class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # check row
        for row in board:
            seen = set()
            for v in row:
                if v == ".":
                    continue
                    
                if v in seen:
                    return False
                seen.add(v)

        # check column
        for i in range(9):
            seen = set()
            for row in board:
                if row[i] == ".":
                    continue

                if row[i] in seen:
                    return False
                seen.add(row[i])
        
        #check boxes
        col = 3
        row = 0

        for c in range(4):
            for j in range(3):
                seen = set()
                for r in range(3):
                    for rb in board[row][col-3:col]:
                        
                        if rb ==".":
                            continue
                        
                        if int(rb) not in seen:
                            seen.add(int(rb))
                            continue

                        return False
                
                    row+=1
            col += 3
            row = 0
        
        return True

            
