import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 10)
    print()

def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    
    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_random_move(board):
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    return random.choice(empty_cells) if empty_cells else None

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    turn = 0 

    while True:
        print_board(board)
        
        if turn % 2 == 0:  
            row, col = map(int, input("Enter row and column (1-3): ").split())
            row-=1
            col-=1
            if board[row][col] == ' ':
                board[row][col] = 'X'
            else:
                print("Invalid move. Try again.")
                continue
        else:
            move = get_random_move(board)
            if move:
                board[move[0]][move[1]] = 'O'
            else:
                print("No empty cells found. This should not happen.")
                break
        
        if check_winner(board, 'X') or check_winner(board, 'O'):
            print_board(board)
            winner = 'X' if check_winner(board, 'X') else 'O'
            print(f"Player {winner} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        turn += 1
