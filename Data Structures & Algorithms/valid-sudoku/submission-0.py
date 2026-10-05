class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # check row
        for row in board:
            seen = set()
            for v in row:
                if v == ".":
                    continue
                    
                if v in seen:
                    print("False in row")
                    return False
                seen.add(v)

        # check column
        for i in range(9):
            seen = set()
            for row in board:
                if row[i] == ".":
                    continue

                if row[i] in seen:
                    print("false in columns")
                    return False
                seen.add(row[i])
        
        #check boxes
        col = 3
        row = 0

        for c in range(4):
            print(row, col)
            for j in range(3):
                seen = set()
                #check box row
                for r in range(3):
                    for rb in board[row][col-3:col]:
                        
                        if rb ==".":
                            continue
                        
                        if int(rb) not in seen:
                            seen.add(int(rb))
                            continue

                        print(f"false in box c:{col} | r:{row} | s:{seen} | rb:{rb}")
                        return False
                
                    row+=1
            col += 3
            row = 0
        
        return True

            
