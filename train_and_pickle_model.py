from variables.constants import EPOCHS

from functions.train import generate_initial_Q, train
from functions.pickle import convert_Q_to_csv, get_Q_version_number, increment_Q_version_number


# initialize
print("Initializing Q.")
Q = generate_initial_Q()
print("Done initializing Q.\n")

filepath = "Q_with_errors.csv"
convert_Q_to_csv(Q, filepath)

# train
print("Begin training.")
train(EPOCHS, Q)
print("Done training.\n")

# pickle
print('Pickling model.')

# where the version number is stored.
filepath = './variables/version_variable.md'
version_num = get_Q_version_number(filepath)

incremented_version_num = int(version_q) + 1
incremented_version_num = str(incremented_version_num)

# save the incremented version number for next training
increment_Q_version_number(filepath, incremented_version_num)
version_q = incremented_version_num

# where the Q is stored.
filepath = 'Q_v%s.csv' % (version_q)

# save the Q.
convert_Q_to_csv(Q, filepath)
print("Done pickling.")
