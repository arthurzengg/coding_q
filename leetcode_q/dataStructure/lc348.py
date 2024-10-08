class TicTacToe:
    def __init__(self, n: int):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0
        self.rev_diag = 0

    def move(self, row: int, col: int, player: int) -> int:
        player_value = 1 if player == 1 else -1

        # Update the row, column, and potentially the diagonals
        self.rows[row] += player_value
        self.cols[col] += player_value

        # Check if the move is on the main diagonal
        if row == col:
            self.diag += player_value

        # Check if the move is on the reverse diagonal
        if col == self.n - 1 - row:
            self.rev_diag += player_value

        # Determine if any have reached the winning condition
        if (abs(self.rows[row]) == self.n or
                abs(self.cols[col]) == self.n or
                abs(self.diag) == self.n or
                abs(self.rev_diag) == self.n):
            return player

        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)