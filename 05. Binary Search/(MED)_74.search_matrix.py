class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Extra micro-optimisation: find out from the get-go if the value cannot possibly be in the matrix
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
            
        # Step 1: Binary search on the 2D array
        top = 0
        bottom = len(matrix) - 1

        while top <= bottom:
            mid = (top + bottom) // 2

            row = matrix[mid]

            if target < row[0]:
                bottom = mid - 1
            elif target > row[-1]:
                top = mid + 1
            elif target == row[0] or target == row[-1]:
                return True
            else:
                break # If the target is in the matrix, it must be in this row

        left = 0
        right = len(row) - 1

        while left <= right:
            mid = (left + right) // 2

            if target == row[mid]:
                return True
            elif target > row[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return False

# O(log m) + O(log n)

# December 21st, 2025