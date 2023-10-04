
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


#def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(row[col] == player for row in board):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    moves = 0

    print("Гра 'Хрестики-нолики'!")
    print_board(board)

    while True:
        row = int(input(f"Гравець {current_player}, введіть номер рядка (0, 1, або 2): "))
        col = int(input(f"Гравець {current_player}, введіть номер стовпця (0, 1, або 2): "))

        if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != " ":
            print("Недійсний хід. Спробуйте ще раз.")
            continue

       # board[row][col] = current_player
        moves += 1
        print_board(board)

        if check_winner(board, current_player):
            print(f"Гравець {current_player} виграв!")
            break
        elif moves == 9:
            print("Нічия!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()

