board = ["-" for i in range(1, 10)]

def print_board(board):
    print("  0 1 2")
    for i in range(3):
        print(0 + i, board[0 + i * 3], board[1 + i * 3], board[2 + i * 3])

def make_move(player):
    field_input = input("Введите номер ячейки в формате 'i j': ")
    try:
        field_number = [int(i) for i in field_input.split()]
    except ValueError:
        print("Номер ячейки введен некорректно. Попробуйте еще раз.")
        return False

    try:
        board_number = field_number[0] + field_number[1] * 3
    except IndexError:
        print("Номер ячейки введен некорректно. Попробуйте еще раз.")
        return False
    if 0 <= board_number <= 8:
        if str(board[board_number]) == "-":
            board[board_number] = player
            return True
        else:
            print("Упс. Эта клетка занята! Попробуйте снова.")
            return False
    else:
        print("Значения строки и столбца не могут быть больше 2. Попробуйте снова.")
        return False

def check_combination(board):
    win_combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for combination in win_combinations:
        if board[combination[0]] != "-" and board[combination[0]] == board[combination[1]] == board[combination[2]]:
            return board[combination[0]]
    return False

def play_game(board):
    player_counter = 0
    win_condition = False

    while not win_condition:
        print_board(board)

        if player_counter % 2 == 0:
            move = make_move("x")
            if move:
                player_counter += 1
            else:
                continue
        else:
            move = make_move("o")
            if move:
                player_counter += 1
            else:
                continue

        win = check_combination(board)
        if win:
            print_board(board)
            print("Игра окончена. Игрок", win, "выиграл! Поздравляем!")
            break
        if player_counter == 9:
            print_board(board)
            print("Ничья! Сыграйте еще раз!")
            break

play_game(board)