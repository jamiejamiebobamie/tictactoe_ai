import random

from functions.ai import suggest_move
from functions.train import compute_R
from functions.play import play_tictactoe_turn, check_winner
from functions. utils import pick_random_move

def test_single_moves(num_moves, Q):
    """
        Given an integer # of moves to test and a trained Q,
        see what the Q is suggesting the player do,
        for that given board_state and player turn.
    """
    for _ in range(num_moves):
        rand_state = random.choice(list(Q.keys()))
        turn, board_state = rand_state
        suggested_index_of_move = suggest_move(Q, rand_state)

        print("\nBoard State:")
        print(board_state[:3])
        print(board_state[3:6])
        print(board_state[6:9])
        print("Turn: ", int(turn))
        print("\nSuggested next move (0-8):")
        print(suggested_index_of_move)
        print(compute_R(rand_state))
        print(Q[rand_state])

def test_accuracy(number_of_games, Q):
    def unit_test(first, AI, starting_percent=0):
        """
            Tests the Q model with the given parameters for the number_of_games
            Record it in the record dictionary.

            INPUT:
                (True, True, 0)

            who goes first:
                True/False
            who has ai:
                True/False/both/neither
            starting_percent:
                0/50, increment the progress percent on the output display.
        """
        for game in range(number_of_games):
            board = [None,None,None,None,None,None,None,None,None]
            board_state = tuple(board)

            turn = first
            winner = None

            state = (turn, board_state)

            while winner == None:
                # play match.

                # use AI (or not)
                if AI == turn or AI == both:
                    suggested_move = suggest_move(Q, state)
                    action = suggested_move
                else:
                    board_state = state[1]
                    action = pick_random_move(board_state)

                state = play_tictactoe_turn(action, state)
                turn, board_state = state
                winner = check_winner(board_state)
            else:
                # record outcome.
                record[first][AI][winner] += 1

                # show progress.
                fraction = game/number_of_games
                if not fraction % .01:
                    print(fraction * 50+starting_percent, "% done.")

    # records a histogram of the outcomes of the games
    record = dict()

    # who won and how many times.
    X, O, tie = True, False, -1
    win_count1 = { X: 0, O: 0, tie: 0 }
    win_count2 = { X: 0, O: 0, tie: 0 }
    win_count3 = { X: 0, O: 0, tie: 0 }
    win_count4 = { X: 0, O: 0, tie: 0 }

    win_count5 = { X: 0, O: 0, tie: 0 }
    win_count6 = { X: 0, O: 0, tie: 0 }
    win_count7 = { X: 0, O: 0, tie: 0 }
    win_count8 = { X: 0, O: 0, tie: 0 }

    # who was using ai
    both, neither = -1, 2
    ai1 = { X: win_count1, O: win_count2, both: win_count3, neither: win_count4}
    ai2 = { X: win_count5, O: win_count6, both: win_count7, neither: win_count8}

    # who went first
    record[X] = ai1
    record[O] = ai2

    print("Testing when X goes first and X is using the AI.")
    unit_test(first=X, AI=X, starting_percent=0)

    print("Testing when X goes first and O is using AI.")
    unit_test(first=X, AI=O, starting_percent=50)

    print("Testing when X goes first and both players have AI.")
    unit_test(first=X, AI=both, starting_percent=0)

    print("Testing when O goes first and both players have AI.")
    unit_test(first=O, AI=both, starting_percent=50)

    print("Testing when O goes first and O is using the AI.")
    unit_test(first=O, AI=O, starting_percent=0)

    print("Testing when O goes first and X is using AI.")
    unit_test(first=O, AI=X, starting_percent=50)

    print("Testing when X goes first and neither is using AI.")
    unit_test(first=X, AI=neither, starting_percent=0)

    print("Testing when O goes first and neither is using AI.")
    unit_test(first=O, AI=neither, starting_percent=50)


    print(record)
