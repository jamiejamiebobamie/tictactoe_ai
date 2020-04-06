from functions.play import play_game
from functions.pickle import convert_csv_to_Q

# load a.i.
file_path = 'Q_v1.csv'
Q = convert_csv_to_Q(file_path)

# play
print("Let's play!\n")
play_game(Q)
print("\nThanks for playing!")
