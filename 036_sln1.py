class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        seen = sum(([(i, c), (c, j), (i/3, j/3, c)]
                    for i, row in enumerate(board)
                    for j, c in enumerate(row)
                    if c != '.'), [])
        return len(seen) == len(set(seen))


sln = Solution()
board = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
print(sln.isValidSudoku(board))