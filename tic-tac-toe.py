import random

board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
players = ["X", "O"]


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
    # Make this wayyy better later
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


def get_input(player: int):
    while True:
        try:
            num = int(input(f"Player {players[player]}, choose a number: "))
        except ValueError:
            print("Invalid input")
            continue
        if num < 1 or num > 9:
            print("Invalid input")
            continue
        if board[num - 1] in players:
            print("Spot already taken")
            continue
        return num


def update_board(player: int):
    num = get_input(player)
    board[num - 1] = players[player]
    print_board()


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


def run_game():
    while True:
        print_board()
        update_board(0)
        if check_win():
            print(f"Player {players[0]} wins!")
            break
        update_board(1)
        if check_win():
            print(f"Player {players[1]} wins!")
            break


def run_game_singleplayer():
    while True:
        print_board()
        update_board(0)
        if check_win():
            print(f"Player {players[0]} wins!")
            break
        ai_move()
        if check_win():
            print(f"AI wins!")
            break


def start():
    print("Welcome to tic-tac-toe!")
    val = input("Do you want to play multiplayer or singleplayer? (m/s): ")
    if val == "m":
        run_game()
    elif val == "s":
        run_game_singleplayer()
    elif val == "q":
        print("Quitting...")
        return
    else:
        print("Invalid input")
        start()


if __name__ == "__main__":
    start()
