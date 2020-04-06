from functions.pickle import convert_csv_to_Q
from functions.tests.test_accuracy import test_accuracy

# load a.i.
file_path = 'Q_v1.csv'
Q = convert_csv_to_Q(file_path)

# test
print("Begin testing.")
number_of_games_per_unit_test = 10000
test_accuracy(number_of_games_per_unit_test, Q)
print("Done testing.\n")
