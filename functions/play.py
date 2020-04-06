import random

from variables.constants import AFFIRMATIVE, WINNERS
from functions.utils import get_available_moves
from functions.ai import suggest_move

def play_game(Q):
    """
        Play against and with the AI in the terminal.
    """
    def pick_symbol():
        """
        Pick your symbol X or O.
        """
        player_symbol = None
        while player_symbol != "X" and player_symbol != "O":
            print("Do you want to be X's or O's?")
            player_symbol = input()
            if player_symbol.isalpha():
                player_symbol = player_symbol.upper()

        return player_symbol

    play_again = 'y'
    while play_again in AFFIRMATIVE:

        state, winner, player_symbol = reset_game()
        player_symbol = pick_symbol()

        turn, board_state = state

        while winner == None:
            action = -1

            print("\nBoard State:")
            print_board_state(board_state, player_symbol)

            suggested_move = suggest_move(Q, state)

            if turn:
                possible_moves = get_available_moves(board_state)
                print("The possible moves (0-8) are:", possible_moves)
                print("From the available positions where would you like to go?")
                print("The algorithm thinks you should go here:", suggested_move)
                print()

                while action not in possible_moves:
                    action = input()
                    action = int(action)
            else:
                action = suggested_move

            state = play_tictactoe_turn(action, state)
            turn, board_state = state
            winner = check_winner(board_state)

        if winner == 1:
            print("You won!")
        elif winner == 0:
            print("You lost :(.")
        else:
            print("Tie!")

        print_board_state(board_state, player_symbol)

        print("Would you like to play again?\n y / n ?\n")
        play_again = input()
        play_again = play_again.lower()

def print_board_state(board_state, player_symbol):
    """
        Print the board state given the player's picked symbol.
    """
    if player_symbol == "X":
        computer_symbol = "O"
    else:
        computer_symbol = "X"

    board = []
    for i, position in enumerate(board_state):
        if position == 1:
            board.append(player_symbol)
        elif position == 0:
            board.append(computer_symbol)
        else:
            board.append(i)

    print(board[:3])
    print(board[3:6])
    print(board[6:9])

def reset_game():
    """
    'Zero's' everything out.
    """
    board = [None,None,None,None,None,None,None,None,None]

    board_state = tuple(board)
    turn = bool(random.getrandbits(1))
    state = (turn, board_state)

    winner = None
    player_symbol = None

    return state, winner, player_symbol

def play_tictactoe_turn(action, state):
    """
    Play a single turn of tictac toe. Returns the next person's turn and the
    new board_state given the input action.

    Input:
         action:
            0-8, an index into the board array

         state:
             board_state:
                (0,1,0,None,None,None,None,None,None),
             a tuple of the board's state

             turn:
                True/False,
             the player's whose turn it is

    Output:
         a new state:
            (True, (0,1,0,None,None,None,None,None,1))
    """

    turn, board_state = state

    board = list(board_state)
    board[action] = int(turn)
    new_turn = not turn
    new_board_state = tuple(board)

    new_state = (new_turn, new_board_state)

    return new_state

def check_winner(board_state):
    """
        Iterates over the board spaces,
        Recording the indices of 1's (1) and 0's (0) in two sets.

        Iterates through the winning combinations in WINNERS
        to see if there is a winner.

        Returns 1, 0, or -1 if True wins, False wins,
        or if there is a tie, respectively.

        Returns None if there is no winner or tie.

        (True and False can represent X's or O's in the game
        and either True or False can go first.)
    """

    indices_ones = set()
    indices_zeroes = set()

    # iterate over board spaces. record indices in sets.
    for i, board_position in enumerate(board_state):
        if board_position == 1:
            indices_ones.add(i)
        elif board_position == 0:
            indices_zeroes.add(i)

    # iterate through the set of winner tuples.
    # for each item in a winning configuration, check
    # if the item is contained in one of the sets.
    for winner in WINNERS:
        One_count = 0
        Zero_count = 0
        for w in winner:
            if w in indices_ones:
                One_count += 1
            elif w in indices_zeroes:
                Zero_count += 1

        # 1 wins
        if One_count == 3:
            return 1
        # 0 wins
        elif Zero_count == 3:
            return 0

    # tie
    if len(indices_ones) + len(indices_zeroes) == len(board_state):
        return -1
