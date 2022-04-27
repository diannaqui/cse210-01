
"""
File : W02_TicTacToe.py

Autor : Diana Quispe

Purpose: Tic Tac Toe game

Requirements:

    Your program must also meet the following requirements.

        * The program must have a comment with assignment and author names.
        * The program must have at least one if/then block.
        * The program must have at least one while loop.
        * The program must have more than one function.
        * The program must have a function called main.
"""


def main():
    player = 'X'
    counter = 0
    board = list('123456789')
    while True:
        print()
        print_board(board)
        winner = player
        player, board = selecction(player, board)
        counter += 1
        win = new_winner(board)

        if counter == 9:
            print('\n\tIt is a tie\n\n')
            break

        elif win == 'Yes':
            print_board(board)
            print(f'\n\tOur winner is {winner}\n\n')
            break
        else:
            continue


def print_board(board):
    """
        Print the board

        Parameters:
            board: This variable holds the board in its current stage.
        Return:
            Nothing
    """

    board_number = 0

    print('\n\tTIC - TAC - TOE\n')
    for _ in range(3):
        print_symbol(board_number, board), print('\033[0m | ', end='')
        print_symbol(board_number+1, board), print('\033[0m | ', end='')
        print_symbol(board_number+2, board)

        if board_number != 6:
            print('\n\033[0m--+---+--')

        board_number += 3

    print()


def print_symbol(number, board):
    """
        Print the letter (X or O) or a number in the right color

        Parameters:
            number: The place on the board [1 to 9]
            board: This variable holds the board in its current stage.
        Return:
            Nothing
    """

    if board[number] == 'X':
        print('\033[1;34mX', end='')
    elif board[number] == 'O':
        print('\033[1;31mO', end='')
    else:
        print(f'\033[0m{number+1}', end='')


def selecction(player, board):
    """
        Ask the player her/his next move

        Parameters:
            player: This variable has the player in turn X or O
            board: This variable holds the board in its current stage.
        Return:
            player: This variable has the player in turn X or O
            board: This variable holds the board in its current stage.
    """

    while True:
        square = int(
            input(f"\n{player}'s turn. Choose an square [1-9]: "))

        if square < 1 or square > 9:
            print(f'\n\tNumber "{square}" is not part of the game board\n\n')
            print_board(board)
            continue

        elif board[square-1] == 'X' or board[square-1] == 'O':
            print('\n\tThis spot is already taking it, try again\n\n')
            print_board(board)
            continue
        else:
            board, player = update_board(square, player, board)
            break

    return player, board


def update_board(square, player, board):
    """
        Update the board with the last move and choose the next player

        Parameters:
            square: The place on the board that the player selected.
            player: This variable has the player in turn X or O
            board: This variable holds the board in its current stage.
        Return:
            player: This variable has the player in turn X or O
            board: This variable holds the board in its current stage.
    """

    board[square-1] = player

    if player == 'X':
        player = 'O'
    else:
        player = 'X'

    return board, player


def new_winner(board):
    """
        This function reads the actual board and decides if there is a winner.

        Parameters:
            board: This variable holds the board in its current stage.
        Return:
            win: This function returns Yes or No depending on whether there is a winner or not.
    """

    win = 'No'

    if (board[0] == board[1] == board[2] or
        board[3] == board[4] == board[5] or
        board[6] == board[7] == board[8] or
        board[0] == board[3] == board[6] or
        board[1] == board[4] == board[7] or
        board[2] == board[5] == board[8] or
        board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6]):

        win = 'Yes'

    return win


if __name__ == "__main__":
    main()
