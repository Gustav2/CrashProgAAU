import os
import random

os.system("")  # Enables ANSI escape codes for Windows

board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
players = ["X", "O"]


# Probably not the best way to do this, but it works
class GameDone(Exception):
    pass


class Colors:
    GREEN = '\33[1m\33[32m'
    RED = '\33[1m\33[31m'
    END = '\033[0m'


def get_player_color(player: int):
    if player == 0:
        return Colors.GREEN
    elif player == 1:
        return Colors.RED


def print_board():
    temp_board = board.copy()
    for i in temp_board:
        if i == players[0]:
            temp_board[temp_board.index(i)] = f"{Colors.GREEN}{i}{Colors.END}"
        elif i == players[1]:
            temp_board[temp_board.index(i)] = f"{Colors.RED}{i}{Colors.END}"
    print(f"""
    -------------
    | {temp_board[0]} | {temp_board[1]} | {temp_board[2]} |
    -------------
    | {temp_board[3]} | {temp_board[4]} | {temp_board[5]} |
    -------------
    | {temp_board[6]} | {temp_board[7]} | {temp_board[8]} |
    -------------
    """)


def check_win():
    magic_square = [4, 9, 2, 3, 5, 7, 8, 1, 6]
    total_x = 0
    total_o = 0
    for i in range(len(board)):
        if board[i] == players[0]:
            total_x += magic_square[i]
        elif board[i] == players[1]:
            total_o += magic_square[i]

    if total_x == 15 or total_o == 15:
        return True


def check_tie():
    if check_win():
        return False
    for i in board:
        if i not in players:
            return False
    return True


def get_input(player: int, change: bool = False):
    while True:
        try:
            if change:
                num = int(input(
                    f"Player {get_player_color(player)}{players[player]}{Colors.END}, choose a number to change: "))
            else:
                num = int(input(f"Player {get_player_color(player)}{players[player]}{Colors.END}, choose a number: "))

        except ValueError:
            print("Invalid input")
            continue

        if num < 1 or num > 9:
            print("Invalid input")
            continue
        if board[num - 1] in players and not change:
            print("Spot already taken")
            continue

        if change:
            if board[num - 1] != players[player]:
                print("You can only change your own spots")
                continue

        return num


def update_board(player: int):
    if board.count(players[player]) >= 3:
        change = get_input(player, True)
        board[change - 1] = str(change)

    num = get_input(player)
    board[num - 1] = players[player]
    print_board()

    if check_win():
        print(f"Player {players[player]} wins!")
        raise GameDone

    if check_tie():
        print("Tie!")
        raise GameDone


def get_free_spots():
    free = []
    for i in range(len(board)):
        if board[i] not in players:
            free.append(i)
    return free


def get_ai_spots():
    ai_spots = []
    for i in range(len(board)):
        if board[i] == players[1]:
            ai_spots.append(i)
    return ai_spots


def ai_move():
    free = get_free_spots()
    ai_spots = get_ai_spots()
    if board.count(players[1]) >= 3:
        remove = random.choice(ai_spots)
        board[remove] = str(remove + 1)
        print(f"AI removed {Colors.RED + str(remove + 1) + Colors.END}")

    move = random.choice(free)
    board[move] = players[1]

    print(f"AI chose {Colors.RED + str(move + 1) + Colors.END}")
    print_board()

    if check_win():
        print(f"AI wins!")
        raise GameDone

    if check_tie():
        print("Tie!")
        raise GameDone


def run_game():
    print_board()
    try:
        while True:
            update_board(0)
            update_board(1)
    except GameDone:
        print("Game done!")


def run_game_single_player():
    print_board()
    try:
        while True:
            update_board(0)
            ai_move()
    except GameDone:
        print("Game done!")


def start():
    while True:
        print("\033[91mWelcome to tic-tac-toe! \033[0m")
        val = input("Do you want to play multiplayer or single player? (m/s): ")
        match val:
            case "m":
                run_game()
                break
            case "s":
                run_game_single_player()
                break
            case "q":
                print("Quitting...")
                return
            case _:
                print("Invalid input")


if __name__ == "__main__":
    try:
        print("\033[H\033[J", end="")  # Clears the screen with crazy hack
        start()
    except KeyboardInterrupt:
        print("Quitting...")
