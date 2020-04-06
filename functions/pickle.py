import pandas as pd
import csv

def convert_Q_to_csv(Q, filepath):
    pd.DataFrame.from_dict(data=Q, orient='index').to_csv(filepath, header=False)

def convert_csv_to_Q(file_path):
    with open(file_path) as csv_file:
        reader = csv.reader(csv_file)
        Q = dict()
        for row in reader:
            turn = row[0][1]
            if turn == "T":
                turn = True
            else:
                turn = False
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
            board_state = tuple(board)
            key = (turn, board_state)
            value = list()
            i = 1
            while i < len(row):
                new_value = float(row[i])
                value.append(new_value)
                i+=1
            Q.update( {key: value} )
    return Q

def get_Q_version_number(filepath):
    with open(filepath, "r+") as vers_var:
        print(vers_var.read()[0])

def increment_Q_version_number(filepath, incrementedNum):
    with open(filepath, "w") as vers_var:
        vers_var.write(incrementedNum)
