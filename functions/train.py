import random

from constants import EPOCHS, EPSILON, LEARNING_RATE, GAMMA

from utils import pick_random_move
from play import play_tictactoe_turn, reset_game, check_winner
from ai import suggest_move

def generate_initial_Q():
    """
        This builds the initial brain or 'Q'.

        Returns a dictionary of states associated with an array of actions.
        All actions are set to an intial value of zero.

        'Q' stands for 'Quality'.

    dictionary of states:
          state = (turn, board_state)

    associated with actions:
          actions = [0,0,0,0,0,0,0,0,0]

    Q = { state: actions }
    """

    Q = {}

    state = (True, (None,None,None,None,None,None,None,None,None))
    Q[state] = [0,0,0,0,0,0,0,0,0]
    state = (False, (None,None,None,None,None,None,None,None,None))
    Q[state] = [0,0,0,0,0,0,0,0,0]

    # play enough games to generate all states.
    for _ in range(100000):

        # ignore 'player_symbol' variable.
        state, winner, player_symbol = reset_game()
        turn, board_state = state

        while winner == None:

            move_here = pick_random_move(board_state)
            action = move_here
            state = play_tictactoe_turn(action, state)

            if state not in Q:
                Q[state] = [0,0,0, 0,0,0, 0,0,0]

            turn, board_state = state
            winner = check_winner(board_state)

    return Q # 8953 valid states, but 3**9 or 19683*2 permutations in all.

def compute_R(state):
    """
    Compute the rewards array which signifies the rewards for the given board
    state and player's turn. "Immediate gratification."

    Input:
        state:
            (True, (None,None,None,1,1,0,1,0,None))

    Output:
        an array of integers, the largest integer being the best move.

    """
    turn, board_state = state

    # possible actions given current state
    Reward_Array = []

    # look for empty board_positions
    for i, board_position in enumerate(board_state):
        if board_position == None:
            Reward_Array.append(0)
        else:
            Reward_Array.append(-1)

    # builds up the values in the rewards array by iterating through the board
    # and testing if either the opponent or the player is one move away from
    # winning
    for i, reward in enumerate(Reward_Array):
        if reward != -1:

            test_board_state = list()
            # deep copy needed.
            for j, board_position in enumerate(board_state):
                if j != i:
                    test_board_state.append(board_position)
                else:
                    test_board_state.append(int(turn))

            possible_winner = check_winner(test_board_state)

            # if the possible winner equals the person's who turn it is.
            if possible_winner == turn:
                Reward_Array[i] += 100 # LOG WINNING MOVE.

            test_board_state = list()
            # deep copy needed.
            for j, board_position in enumerate(board_state):
                if j != i:
                    test_board_state.append(board_position)
                else:
                    test_board_state.append(int(not turn))

            possible_winner = check_winner(test_board_state)

            # if the possible winner equals the other guy.
            if possible_winner == (not turn):
                Reward_Array[i] += 50 # BLOCK THE OTHER PLAYER.

    return Reward_Array

def train(EPOCHS, Q):
    """
    Given an integer # of epochs and an initialized Q, train the Q, by slowly
    building up the state-actions by playing tic-tac-toe and recording the
    rewards.
    """
    for epoch in range(EPOCHS):

        # ignore 'player_symbol' variable.
        state, winner, player_symbol = reset_game()

        while winner == None:
            state = play_tictactoe_turn_training(Q, state)
            board_state = state[1]
            winner = check_winner(board_state)

        else:
            # show progress.
            percent = epoch/EPOCHS
            if not percent % .01:
                print(percent *100, "% done.")

def play_tictactoe_turn_training(Q, state):
    """
        Play a single turn of tic tac toe while training.

        * * * UPDATES THE Q MODEL. * * *

        Returns the new board state and the next person's turn.
    """

    # the immediate rewards based on the given board_state
    R = compute_R(state)

    if random.uniform(0, 1) < EPSILON:
        # exploration
        board_state = state[1]
        action = pick_random_move(board_state)
    else:
        # exploitation
        action = suggest_move(Q, state)

    next_state = play_tictactoe_turn(action, state)

    # Update the Q model.
    Q[state][action] = ( (1 - LEARNING_RATE) * Q[state][action]
                                                + LEARNING_RATE
                                                * ( R[action] + GAMMA
                                                    * max(Q[next_state]) ) )

    return next_state


def get_Q_version_number(filepath):
    with open(filepath, "r+") as vers_var:
        print(vers_var.read()[0])

def increment_Q_version_number(filepath, incrementedNum):
    with open(filepath, "w") as vers_var:
        vers_var.write(incrementedNum)
