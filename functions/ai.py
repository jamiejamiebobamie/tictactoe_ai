import random

from train import compute_R
from utils import get_index_of_max
from play import check_winner

def suggest_move(Q, state):
    """
        Given a trained brain, Q, and a state:
            (True, (0, 1, 0, 1, None, None, None, None, 0))
        recieve an index into the board state for the suggested next move.
    """
    _, board_state = state
    winner = check_winner(board_state)
    # there is already a winner.
    if winner != None:
        return -1

    max_indices = []
    max_choice = float("-inf")

    # test to see if the move is in the dictionary.
    valid = Q.get(state, None)

    # if it is not, add an empty set of actions to the brain.
    # this is a fail safe. this should never happen.
    if not valid:
        empty_actions = [0,0,0,0,0,0,0,0,0]
        new_entry = {state: empty_actions}
        Q.update(new_entry)
        print("NEW STATE ADDED! CHECK CODE. SOMETHING IS WRONG.")
        print(new_entry)

    Q_reward_array = Q[state]

    # NOTE: this block of code seems to only affect the instances when both
        # players are using the AI. the built model switches from 100% ties
        # to a 100% wins for the player who went first when this block is
        # commented out, leading me to think there are errors in how the Q
        # model is built. it *should* be contentious when both are using the
        # AI.
    max_Q_action = int(max(Q_reward_array))
    # if the Q table is empty (all zeroes)
    # fallback on the Rewards Array.
    if max_Q_action == 0:
        R = compute_R(state)
        index_of_max_R = get_index_of_max(R)
        return index_of_max_R

    # find all of the max positions from the Q for a given state.
    for i, choice in enumerate(Q_reward_array):
        if board_state[i] == None:
            temp = max_choice
            max_choice = max(max_choice, choice)
            if temp != max_choice:
                max_indices = []
                max_indices.append(i)
            if choice == max_choice:
                max_indices.append(i)

    return random.choice(max_indices)
