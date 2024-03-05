def minimax_alpha_beta(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or is_terminal(board):
        return evaluate(board)

    if maximizing_player:
        max_eval = float('-inf')
        for move in get_available_moves(board):
            new_board = make_move(board, move, 'X')
            eval = minimax_alpha_beta(new_board, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in get_available_moves(board):
            new_board = make_move(board, move, 'O')
            eval = minimax_alpha_beta(new_board, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval


def find_best_move(board):
    best_val = float('-inf')
    best_move = None

    for move in get_available_moves(board):
        new_board = make_move(board, move, 'X')
        move_val = minimax_alpha_beta(new_board, 3, float('-inf'), float('inf'), False)

        if move_val > best_val:
            best_val = move_val
            best_move = move

    return best_move


def is_terminal(board):
    pass


def evaluate(board):
    pass


def get_available_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                moves.append((i, j))
    return moves


def make_move(board, move, player):
    # Wykonuje ruch na planszy
    i, j = move
    new_board = [row.copy() for row in board]
    new_board[i][j] = player
    return new_board


# Przykładowa plansza
sample_board = [
    ['X', 'O', 'X'],
    ['O', ' ', ' '],
    [' ', 'X', 'X']
]

best_move = find_best_move(sample_board)

print("Optymalny ruch:", best_move)
