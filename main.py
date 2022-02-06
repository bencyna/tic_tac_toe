Game = ["   ", "|", "   ", "|", "   ", "\n", "-----------", "\n", '   ', '|', '   ', "|", "   ", "\n", "-----------",
        "\n",
        "   ", "|", "   ", "|", "   ", ]
positions_dict = {'0, 0': 0, '0, 1': 2, '0, 2': 4, '1, 0': 8, '1, 1': 10, '1, 2': 12, '2, 0': 16, '2, 1': 18,
                  '2, 2': 20, }
player1_turn = True

winning_positions = [['0, 1', '0, 2', '0, 3'], ['1, 1', '1, 2', '1, 3'], ['2, 1', '2, 2', '2, 3'],
                     ['0, 0', '0, 1', '0, 2'], ['1, 0', '1, 1', '1, 2'], ['2, 0', '2, 1', '2, 2'],
                     ['0, 0', '1, 1', '2, 2'], ['0, 2', '1, 1', '2, 0']]

player1_positions = []
player2_positions = []
all_chosen = []


def init_game():
    global Game
    print("Play tic tac toe\n\n")
    print_game()


def check_for_winner(position):
    for winning_row in winning_positions:
        print(set(winning_row).issubset(player1_positions))
        if set(winning_row).issubset(player1_positions):
            print("Winner is player 1")
            return
        elif set(winning_row).issubset(player2_positions):
            print("winner is player 2")
            return

    all_chosen.append(position)
    if len(all_chosen) >= 9:
        print("The game is a draw")
    else:
        print_game()


def add_user_positions(player_num, position):
    if player_num == "1":
        player1_positions.append(position)
    else:
        player2_positions.append(position)

    check_for_winner(position)


def user_input():
    global positions_dict, player1_turn, Game
    if player1_turn:
        player = "1"
        symbol = " X "
    else:
        player = "2"
        symbol = " O "

    pos = input(
        f"\nPlayer {player}:\nenter the position of the element you want to add \ni.e. top left is 0, 0, bottom right is 2, 2, bottom middle is 1, 2\n")

    if pos in all_chosen:
        print("Position taken, choose a different spot")
        return user_input()

    try:
        place_in_pos = positions_dict[pos]
        Game[place_in_pos] = symbol
        player1_turn = not player1_turn
        add_user_positions(player, pos)

    except KeyError:
        print("The value entered must be in this format: 0, 1")
        user_input()


def print_game():
    print("".join(Game))

    user_input()


init_game()
