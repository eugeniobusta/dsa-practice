"""
36. Valid Sudoku - Medium
https://neetcode.io/problems/valid-sudoku/question

Approach: - Have 3 arrays, each to check the indicies of rows, cols and the 3x3 grid.
          - Check if in each rows[i] for num, same for cols[i] and grids[i]
            
TIME: O(1) for 9x9 but O(n^2) for NxN boards
SPACE: O(1) for 9x9 but O(n^2) for NxN boards

Mistake: Not figuring out how to check for 3x3 grid.
"""

# 1st Solution using hint to figure out how to check for 3x3 grid
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        check_r = [set() for n in range(len(board))]
        check_c = [set() for n in range(len(board))]
        check_b = {}

        for row in range(9):
            for col in range(9):
                num = board[row][col]

                # only manage numbers
                if num != ".":
                    # Check if seen in the same row or col
                    if (num in check_r[row]) or (num in check_c[col]):
                        return False
                    box = (row // 3, col // 3)
                    if num in check_b.get(box, set()):
                        return False
                        
                    check_r[row].add(num)
                    check_c[col].add(num)
                    check_b.setdefault(box, set()).add(num)

        return True
