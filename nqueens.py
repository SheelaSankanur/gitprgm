class Solution:

    def isSafe(self, board, row, col, n):
        # Check same column
        for i in range(row):
            if board[i][col] == 'Q':
                return False

        # Upper-left diagonal
        i, j = row-1, col-1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        # Upper-right diagonal
        i, j = row-1, col+1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        return True


    def nQueens(self, board, row, n, ans):
        if row == n:
            ans.append(["".join(r) for r in board])
            return

        for col in range(n):
            if self.isSafe(board, row, col, n):
                board[row][col] = 'Q'
                self.nQueens(board, row + 1, n, ans)
                board[row][col] = '.'


    def solveNQueens(self, n):
        board = [['.' for _ in range(n)] for _ in range(n)]
        ans = []
        self.nQueens(board, 0, n, ans)
        return ans


# Main program
obj = Solution()

n = int(input("Enter value of n: "))

result = obj.solveNQueens(n)

print("\nNumber of solutions:", len(result))

for board in result:
    for row in board:
        print(row)
    print()
    
