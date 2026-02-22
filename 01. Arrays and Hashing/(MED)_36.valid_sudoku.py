# In this file: the array solution 

from typing import List

# My solution
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]  # each value is a set (a row)
        cols = [set() for _ in range(9)]  # each value is a set (a column)
        boxes = [set() for _ in range(9)]  # each value is a set (a box)

        # Set is unordered collection of elements

        for i in range(9):
            for j in range(9):
                current = board[i][j]
                if current == ".": # don't check conditions if space is empty
                    continue

                box_index = 3 * (i // 3) + (j // 3)
                
                if (current in rows[i] or current in cols[j] or current in boxes[box_index]):
                    return False
                
                else:
                    rows[i].add(current)
                    cols[j].add(current)
                    boxes[box_index].add(current)

        return True

# Box 0: i <= 2, j <= 2
# Box 1: i <= 2, 2 < j <= 5

solution = Solution()
print(solution.isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))
print(solution.isValidSudoku([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))