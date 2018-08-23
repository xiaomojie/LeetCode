"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or len(word) == 0:
            return False
        visited = [[False] * len(board[0]) for i in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.search(board, word, i, j, 0, visited):
                    return True
        return False

    def search(self, board, word, i, j, cur, visited):
        if cur == len(word):
            return True
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[i]) or visited[i][j] or board[i][j] != word[cur]:
            return False

        visited[i][j] = True
        result = self.search(board, word, i, j-1, cur+1, visited) or self.search(board, word, i-1, j, cur+1, visited) \
               or self.search(board, word, i, j+1, cur+1, visited) or self.search(board, word, i+1, j, cur+1, visited)
        visited[i][j] = False
        return result

board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
print(Solution().exist(board, 'ABCCED'))
print(Solution().exist(board, 'SEE'))
print(Solution().exist(board, 'ABCB'))
