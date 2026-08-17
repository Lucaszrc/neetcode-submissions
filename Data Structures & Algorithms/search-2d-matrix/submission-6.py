from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False  # empty matrix guard
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        # Start at TOP-RIGHT corner
        row = 0
        col = cols - 1
        
        while row < rows and col >= 0:
            val = matrix[row][col]
            
            if val == target:
                return True
            elif target > val:
                row += 1  # move DOWN: target is bigger → go down
            else:
                col -= 1  # move LEFT: target is smaller → go left
        
        return False  # not found