"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Jana Halasova
email: hajanalas@gmail.com
discord: janah.444
"""
import random

# Greeting players
print("Welcome to Tic Tac Toe")

# Game rules
print("""\
============================================
GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row
============================================
Let´s start the game
--------------------------------------------
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+"""
      )


def playing_board(current_board: dict):
    """
    To display current game board status
    :param current_board: dictionary contents current values of the fields
    :return: printing of the current status of the board
    """
    board = current_board
    return print(f"""\
============================================
+---+---+---+
| {board[1]} | {board[2]} | {board[3]} |
+---+---+---+
| {board[4]} | {board[5]} | {board[6]} |
+---+---+---+
| {board[7]} | {board[8]} | {board[9]} |
+---+---+---+"""
    )


def choose_a_field(current_player: str, current_board: dict) -> str:
    """
    To ask current player to input his choice and verify its validity
    :param current_player: letter indicating a player on the turn
    :param current_board: dictionary contents current values of the fields
    :return: integer indicating the choice of the current player
    """
    verify_input = True
    while verify_input:
        player_choice = input(f"{44 * '='}\nPlayer {current_player}"
                              f" | Please enter your move number: ")
        if not player_choice.isdigit():
            print("You entered a wrong input! "
                  "You have to enter a number (from 1 to 9).")
            continue
        elif int(player_choice) not in range(1, 10):
            print("You entered a wrong number! "
                  "Only number from 1 to 9 is possible to choose.")
            continue
        elif current_board[int(player_choice)] != " ":
            print("The field is already occupied! Choose another one.")
            continue
        else:
            return player_choice


def end_of_game(current_board: dict, current_player: str) -> bool:
    """
    To evaluate whether someone has won or it is a draw
    :param current_board: dictionary contents current values of the fields
    :param current_player: letter indicating a player on the turn
    :return: bool value indicating whether the game continues or ended
    """
    if (current_board[1] == current_board[2] == current_board[3] ==
            current_player or
            current_board[4] == current_board[5] == current_board[6] ==
            current_player or
            current_board[7] == current_board[8] == current_board[9] ==
            current_player or
            current_board[1] == current_board[4] == current_board[7] ==
            current_player or
            current_board[2] == current_board[5] == current_board[8] ==
            current_player or
            current_board[3] == current_board[6] == current_board[9] ==
            current_player or
            current_board[1] == current_board[5] == current_board[9] ==
            current_player or
            current_board[3] == current_board[5] == current_board[7] ==
            current_player):
        print(f"Congratulations player {current_player}, you won!!!")
        game_runs = False
    elif " " not in current_board.values():
        print("It is a draw, nobody won...")
        game_runs = False
    else:
        game_runs = True
    return game_runs


def tic_tac_toe():
    """
    The whole game Tic Tac Toe
    """
    game_runs = True
    current_board = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ",
                     6: " ", 7: " ", 8: " ", 9: " "}
    start_possibilities = random.choice([("o", "x"), ("x", "o")])
    while game_runs:
        for player in start_possibilities:
            current_player = player
            stone_position = choose_a_field(current_player, current_board)
            current_board[int(stone_position)] = current_player
            playing_board(current_board)
            game_runs = end_of_game(current_board, current_player)
            if game_runs is False:
                break


if __name__ == '__main__':
    tic_tac_toe()
