Game = ["  ", "|", "  ", "|", "  ", "\n", "---------", "\n", '  ', '|', '  ', "|" "  ", "\n", "----------", "\n",
        "  ", "|", "  ", "|", "  ", ]


def init_game():
    global Game
    print("Play tic tac toe\n\n")


def print_game():
    print("".join(Game))


init_game()


def user_input():
    pos = input(
        "\nenter the position of the element you want to add \ni.e. top left is 0, 0, bottom right is 2, 2, bottom middle is 1, 2\n")
