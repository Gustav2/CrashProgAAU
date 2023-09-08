import random

board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
players = ["X", "O"]


# Probably not the best way to do this, but it works
class GameDone(Exception):
    pass


def print_board():
    print(f"""
    -------------
    | {board[0]} | {board[1]} | {board[2]} |
    -------------
    | {board[3]} | {board[4]} | {board[5]} |
    -------------
    | {board[6]} | {board[7]} | {board[8]} |
    -------------
    """)


def check_win():
    # TODO: Make this way better later
    if board[0] == board[1] == board[2]:
        return True
    if board[3] == board[4] == board[5]:
        return True
    if board[6] == board[7] == board[8]:
        return True
    if board[0] == board[3] == board[6]:
        return True
    if board[1] == board[4] == board[7]:
        return True
    if board[2] == board[5] == board[8]:
        return True
    if board[0] == board[4] == board[8]:
        return True
    if board[2] == board[4] == board[6]:
        return True
    return False


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
                num = int(input(f"Player {players[player]}, choose a number to change: "))
            else:
                num = int(input(f"Player {players[player]}, choose a number: "))

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


def ai_move():
    free = get_free_spots()
    move = random.choice(free)
    board[move] = players[1]
    print(f"AI chose {move + 1}")
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
    while True:
        update_board(0)

        ai_move()


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
