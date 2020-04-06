import random

from functions.utils import get_indices_of_max, get_index_of_max, pick_random_move, get_available_moves

def suggest_move(Q, state):
    """
        Given a trained brain, Q, and a state:
            (True, (0, 1, 0, 1, None, None, None, None, 0))
        recieve an index into the board state for the suggested next move.
    """
    index_max_move = -1

    _, board_state = state

    indices_possible_moves = get_available_moves(board_state)

    # test to see if the move is in the dictionary.
    valid = Q.get(state, False)

    if valid:
        Q_rewards_array = valid
        max_Q_score = float('-inf')

        for index in indices_possible_moves:
            temp = max_Q_score
            max_Q_score = max(Q_rewards_array[index],max_Q_score)
            if temp != max_Q_score:
                index_max_move = index

    return index_max_move if index_max_move != -1 else random.choice(indices_possible_moves)
