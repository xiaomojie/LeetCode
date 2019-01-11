"""
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true
"""
# import numpy as np


class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # 检测行
        for row in board:
            rowSet = [i for i in row if i != '.']
            if len(set(rowSet)) != len(rowSet):
                return False
        # 检测列
        for col in zip(*board):
            colSet = [j for j in col if j != '.']
            if len(set(colSet)) != len(colSet):
                return False

        # 检测小方格
        # array_board = np.array(board)
        for i in [0,3,6]:
            for j in [0,3,6]:
                # 下行代码在 leetcode 上会报错，没有numpy
                # square = [item for row in array_board[i:i+3,j:j+3] for item in row if item != '.']
                square = [board[p][q] for p in range(i, i+3) for q in range(j, j+3) if board[p][q] != '.']
                if len(set(square)) != len(square):
                    # print(i,j,square)
                    return False
        return True

a = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
print(Solution().isValidSudoku(a))

# a = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(a[0:2,0:2])