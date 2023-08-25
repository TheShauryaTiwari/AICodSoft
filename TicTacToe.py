import random

# Constants for representing the players and empty spots
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(cell == player for cell in board[i]) or all(row[i] == player for row in board) \
                or (board[0][0] == board[1][1] == board[2][2] == player) \
                or (board[0][2] == board[1][1] == board[2][0] == player):
            return True
    return False

def get_empty_cells(board):
    return [(row, col) for row in range(3) for col in range(3) if board[row][col] == EMPTY]

def minimax(board, depth, is_maximizing):
    scores = {'X': 1, 'O': -1, 'tie': 0}

    if is_winner(board, PLAYER_X):
        return scores[PLAYER_X]
    if is_winner(board, PLAYER_O):
        return scores[PLAYER_O]

    empty_cells = get_empty_cells(board)
    if not empty_cells:
        return scores['tie']

    if is_maximizing:
        best_score = -float('inf')
        for row, col in empty_cells:
            board[row][col] = PLAYER_X
            score = minimax(board, depth + 1, False)
            board[row][col] = EMPTY
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for row, col in empty_cells:
            board[row][col] = PLAYER_O
            score = minimax(board, depth + 1, True)
            board[row][col] = EMPTY
            best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -float('inf')
    best_move = None

    for row, col in get_empty_cells(board):
        board[row][col] = PLAYER_X
        score = minimax(board, 0, False)
        board[row][col] = EMPTY

        if score > best_score:
            best_score = score
            best_move = (row, col)

    return best_move

def main():
    board = [[EMPTY] * 3 for _ in range(3)]
    player = random.choice([PLAYER_X, PLAYER_O])

    while True:
        print_board(board)
        if player == PLAYER_X:
            row, col = best_move(board)
            print("AI's Move:", row, col)
        else:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))

        if board[row][col] == EMPTY:
            board[row][col] = player
            if is_winner(board, player):
                print_board(board)
                print(player, "wins!")
                break
            if all(board[i][j] != EMPTY for i in range(3) for j in range(3)):
                print_board(board)
                print("It's a tie!")
                break
            player = PLAYER_X if player == PLAYER_O else PLAYER_O
        else:
            print("Cell already taken. Try again.")

if __name__ == "__main__":
    main()
