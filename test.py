from functions.pickle import convert_csv_to_Q
from tests.test_accuracy import test_accuracy, test_single_moves

# load a.i.
file_path = 'Q_v2.csv'
Q = convert_csv_to_Q(file_path)

# test
print("Begin testing.")
number_of_games_per_unit_test = 10000
test_accuracy(number_of_games_per_unit_test, Q)
# test_single_moves(10,Q)
print("Done testing.\n")
