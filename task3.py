""" Крестики-нолики
● Контекст
Вероятнее всего, вы с детства знакомы с этой игрой. Пришло
время реализовать её. Два игрока по очереди ставят крестики
и нолики на игровое поле. Игра завершается когда кто-то
победил, либо наступила ничья, либо игроки отказались
играть.
● Задача
Написать игру в “Крестики-нолики”. Можете использовать
любые парадигмы, которые посчитаете наиболее
подходящими. Можете реализовать доску как угодно - как
одномерный массив или двумерный массив (массив массивов).
Можете использовать как правила, так и хардкод, на своё
усмотрение. Главное, чтобы в игру можно было поиграть через
терминал с вашего компьютера. """
def check_winner(board, player):
    # Проверка строк и столбцов
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True

    # Проверка диагоналей
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        row = int(input(f"Игрок {current_player}, введите номер строки (0, 1, 2): "))
        col = int(input(f"Игрок {current_player}, введите номер столбца (0, 1, 2): "))

        if board[row][col] == ' ':
            board[row][col] = current_player
            if check_winner(board, current_player):
                print_board(board)
                print(f"Игрок {current_player} победил!")
                break
            elif is_board_full(board):
                print_board(board)
                print("Ничья!")
                break
            else:
                current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Эта ячейка уже занята. Попробуйте снова.")

if __name__ == "__main__":
    tic_tac_toe()
