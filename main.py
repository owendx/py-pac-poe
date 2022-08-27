# print a message that says the following
# ________________________
# Let's Play Py-Pac-Poe'
# ------------------------
print('------------------------')
print("Let's Play Py-Pac-Poe'")
print('------------------------')

board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
print()

def board_printer(board_data):
    print('    A     B     C   ')
    print(f"1)  {board_data[0][0]}  |  {board_data[0][1]}  |  {board_data[0][2]}  ")
    print('   ----------------')
    print(f"2)  {board_data[1][0]}  |  {board_data[1][1]}  |  {board_data[1][2]}  ")
    print('   ----------------')
    print(f"3)  {board_data[2][0]}  |  {board_data[2][1]}  |  {board_data[2][2]}  ")

board_printer(board)

def player_choice(player):
    choice = input(f"{player}, please choose a square: ")
    valid_choices = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
    if choice in valid_choices:
        def choice_shifter(input_string):
            input_string = input_string.replace('A', '1').replace('B', '2').replace('C', '3')
            x = int(input_string[1]) - 1
            y = int(input_string[0]) - 1
            if board[x][y] == ' ':
                board[x][y] = player
                return board[x][y]
            else:
                print("That square is already taken.")
                player_choice(player)
            pass
        choice_shifter(choice)
    else:
        print("Invalid choice, please choose again.")
        player_choice(player)
    return board


def game_over(board):
    if board[0][0] == board[0][1] == board[0][2] != ' ':
        return True
    elif board[1][0] == board[1][1] == board[1][2] != ' ':
        return True
    elif board[2][0] == board[2][1] == board[2][2] != ' ':
        return True
    elif board[0][0] == board[1][0] == board[2][0] != ' ':
        return True
    elif board[0][1] == board[1][1] == board[2][1] != ' ':
        return True
    elif board[0][2] == board[1][2] == board[2][2] != ' ':
        return True
    elif board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    elif board[0][2] == board[1][1] == board[2][0] != ' ':
        return True
    else:
        return False


def game_winner(board):
    if board[0][0] == board[0][1] == board[0][2] != ' ':
        return board[0][0]
    elif board[1][0] == board[1][1] == board[1][2] != ' ':
        return board[1][0]
    elif board[2][0] == board[2][1] == board[2][2] != ' ':
        return board[2][0]
    elif board[0][0] == board[1][0] == board[2][0] != ' ':
        return board[0][0]
    elif board[0][1] == board[1][1] == board[2][1] != ' ':
        return board[0][1]
    elif board[0][2] == board[1][2] == board[2][2] != ' ':
        return board[0][2]
    elif board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    else:
        return False


def game_draw(board):
    for x in board:
        for y in x:
            if y == ' ':
                return False
    return True


def game_winner_printer(winner):
    if winner == 'X':
        print("X wins!")
    elif winner == 'O':
        print("O wins!")
    else:
        print("It's a draw!")


def game_winner_check(board):
    if game_over(board):
        winner = game_winner(board)
        game_winner_printer(winner)
        return True
    else:
        return False


def game_draw_check(board):
    if game_draw(board):
        print("It's a draw!")
        return True
    else:
        return False


def game_loop(board):
    while not game_winner_check(board) and not game_draw_check(board):
        player_choice('X')
        board_printer(board)
        if game_winner_check(board):
            break
        if game_draw_check(board):
            break
        player_choice('O')
        board_printer(board)
        if game_winner_check(board):
            break
        if game_draw_check(board):
            break


def game_start():
    game_loop(board)


game_start()
