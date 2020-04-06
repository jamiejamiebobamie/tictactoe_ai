import random

def pick_random_move(board_state):
    """
    Input:
         board_state:
            (0,1,0,None,None,None,None,None,None)
         a tuple of the board's state

    Output:
         a random move from the possibilities.
    """
    possible_moves = get_available_moves(board_state)
    number_of_possible_moves = len(possible_moves)

    if number_of_possible_moves < 1:
        return -1

    random_index_into_possible_moves = random.randint(0,
                                                number_of_possible_moves-1)

    return possible_moves[random_index_into_possible_moves]

def get_available_moves(board_state):
    """
    Return an array of board positions/indices that contain "None".

    Input:
         board_state:
            (0,1,0,None,None,None,None,None,None)
         a tuple of the board's state

    Output:
         an array of board positions/indices of possible moves:
            [3,4,5,6,7,8]
    """
    possible_moves = []
    for i, board_position in enumerate(board_state):
        if board_position == None:
            possible_moves.append(i)

    return possible_moves

def get_index_of_max(iterable):
    """
    Return the first index of one of the maximum items in the iterable.
    """
    max_i = -1
    max_v = float('-inf')

    for i, iter in enumerate(iterable):
        temp = max_v
        max_v = max(iter,max_v)
        if max_v != temp:
            max_i = i

    return max_i

def get_indices_of_max(iterable):
    """Return the max indices of the iterable."""

    max_indices = []
    max_v = float('-inf')
    ACCEPTABLE_DIFFERENCE = 1 # hyperparameter

    for i, iter in enumerate(iterable):
        difference = max_v - iter
        squared_difference = difference*difference
        if squared_difference < ACCEPTABLE_DIFFERENCE:
            max_indices.append(i)
        else:
            temp = max_v
            max_v = max(iter,max_v)
            if max_v != temp:
                max_indices = []
                max_i = i
                max_indices.append(max_i)

    return max_indices

def print_vals_at_indices(vals_array, indices_array):
    vals = []
    if len(vals_array) > len(indices_array):
        for i in indices_array:
            vals.append(vals_array[i])
    return vals

def rotate_matrix_clockwise(flattened_array_of_length_nine):
    return_array = [None]*9
    return_array[0] = flattened_array_of_length_nine[6]
    return_array[1] = flattened_array_of_length_nine[3]
    return_array[2] = flattened_array_of_length_nine[0]
    return_array[3] = flattened_array_of_length_nine[7]
    return_array[4] = flattened_array_of_length_nine[4]
    return_array[5] = flattened_array_of_length_nine[1]
    return_array[6] = flattened_array_of_length_nine[8]
    return_array[7] = flattened_array_of_length_nine[5]
    return_array[8] = flattened_array_of_length_nine[2]
    return return_array
