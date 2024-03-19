class TicTacToe:
    def __init__(self, board=None, player='X'):
        self.player = player  # 'X' or 'O'
        if board is None:
            self.board = [[' ' for _ in range(3)] for _ in range(3)]
        else:
            self.board = board

    def is_terminal(self):
        # Sprawdzenie, czy jest zwycięzca
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True

        # Sprawdzenie, czy plansza jest pełna
        for row in self.board:
            if ' ' in row:
                return False

        return True

    def utility(self):
        # Sprawdzenie, kim jest zwycięzca
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return 1 if self.board[i][0] == 'X' else -1
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return 1 if self.board[0][i] == 'X' else -1

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return 1 if self.board[0][0] == 'X' else -1
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return 1 if self.board[0][2] == 'X' else -1

        return 0  # Remis

    def children(self):
        children = []
        next_player = 'O' if self.player == 'X' else 'X'
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    new_board = [row.copy() for row in self.board]
                    new_board[i][j] = self.player
                    children.append(TicTacToe(new_board, next_player))
        return children


def alpha_beta_pruning(node, depth, alpha, beta, maximizing_player=True):
    if depth == 0 or node.is_terminal():
        return node.utility()

    if maximizing_player:
        max_eval = float('-inf')
        for child in node.children():
            eval = alpha_beta_pruning(child, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for child in node.children():
            eval = alpha_beta_pruning(child, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval


# Testujemy algorytm na pustej planszy
initial_board = TicTacToe()
best_outcome = alpha_beta_pruning(initial_board, depth=9, alpha=float('-inf'), beta=float('inf'),
                                  maximizing_player=True)
print(best_outcome)
