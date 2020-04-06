# Tic Tac Toe AI

This is an attempt at improving the accuracy and robustness of my model.

Two methods that I've come up with for improving my model are:
    * When building the initial Q and during training, rotate the board 90 degrees three times. After each rotation add the board_state to the Q (if initializing) or update the values of the rewards matrix for the rotated board (if training).
    * During training, always randomly pick the first move. Never exploit the Q for the ideal move if it is the first move of the game.
