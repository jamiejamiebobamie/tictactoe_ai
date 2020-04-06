



import sys
sys.path.append('../')
from functions.play import play_tictactoe_turn


state = (False, (0,1,1,None,None,None,None,None,0))
action = 3
return_state = (True, (0,1,1,0,None,None,None,None,0))

print(play_tictactoe_turn(action,state))
