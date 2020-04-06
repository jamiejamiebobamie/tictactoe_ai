import sys
sys.path.append('../')
from functions.ai import suggest_move
from functions.pickle import convert_csv_to_Q

import unittest


class AITests(unittest.TestCase):
    def test_suggest_move_normal_input(self):
        file_path = 'Q_v1.csv'
        Q = convert_csv_to_Q(file_path)
        assert suggest_move(Q,(False,(0,1,1,0,None,None,None,None,None))) is 6
        assert suggest_move(Q,(True,(0,1,1,0,None,None,None,None,None))) is 6


    def test_suggest_move_incorrect_input(self):
        file_path = 'Q_v1.csv'
        Q = convert_csv_to_Q(file_path)
        assert suggest_move(Q,(False,(0,1,1,0,1,None,1,None,1))) is -1

if __name__ == '__main__':
    unittest.main()
