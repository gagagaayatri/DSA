"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
      columns = defaultdict(set) #create hashset to check for duplicates
      rows = defaultdict(set)
      squares = defaultdict(set) #will contain 3X3 as key
      # Since board is 9x9 , we will iterate through each cell.
      for r in range(9):
        for c in range(9):
          #IF a cell is empty, the sudoku board is still valid
          if board[r][c] == '.':
            continue
          if (board[r][c] in columns[c] or board[r][c] in rows[r] or board[r][c] in squares[(r//3,c//3)]):#Check if duplicates are present, for each 3X3 convert index of 9x9 to compare each 3x3
            return False
          columns[c].add(board[r][c])
          rows[r].add(board[r][c])
          squares[(r//3,c//3)].add(board[r][c])
      return True
      
