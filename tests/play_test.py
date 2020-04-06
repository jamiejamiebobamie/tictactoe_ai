# play_tictactoe_turn

import sys
sys.path.append('../')
from functions.play import play_tictactoe_turn

import unittest

class AITests(unittest.TestCase):
    def test_play_tictactoe_turn(self):
        state = (False, (0,1,1,None,None,None,None,None,0))
        action = 3
        return_state = (False, (0,1,1,0,None,None,None,None,0))
        assert play_tictactoe_turn(action,state) is return_state


    # def test_suggest_move_incorrect_input(self):
    #     file_path = 'Q_v1.csv'
    #     Q = convert_csv_to_Q(file_path)
    #     assert suggest_move(Q,(False,(0,1,1,0,1,None,1,None,1))) is -1

if __name__ == '__main__':
    unittest.main()
