import csv
from collections import Counter

def check_Q_for_incorrect_boards(file_path):
    with open(file_path) as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            turn = row[0][1]
            if turn == "T":
                turn = 1
            else:
                turn = 0
            key_list = row[0][2:-1].split(",")
            board = []
            for i, entry in enumerate(key_list):
                for char in entry:
                    if char == '1':
                        board.append(1)
                        break
                    elif char == '0':
                        board.append(0)
                        break
                    elif char == 'N':
                        board.append(None)
                        break
            # checking to see if the correct
                # number of turns have not been played.
            histogram = Counter(board)
            countOfZeroes = histogram.get(0,0)
            countOfOnes = histogram.get(1,0)

            if abs(countOfZeroes - countOfOnes) > 1:
                print(board)




check_Q('Q_with_errors.csv')
