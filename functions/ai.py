import random

from functions.utils import get_indices_of_max

def suggest_move(Q, state):
    """
        Given a trained brain, Q, and a state:
            (True, (0, 1, 0, 1, None, None, None, None, 0))
        recieve an index into the board state for the suggested next move.
    """
    best_actions = []
    # test to see if the move is in the dictionary.
    valid = Q.get(state, False)

    if valid:
        Q_rewards_array = valid
        best_actions = get_indices_of_max(Q_rewards_array)

    return random.choice(best_actions) if len(best_actions) else -1
