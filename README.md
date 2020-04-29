# Tic Tac Toe AI

This is an improved version of [an earlier attempt](https://github.com/jamiejamiebobamie/Tic-Tac-Toe-with-Q-Reinforcement-Learning) at building a Tic-Tac-Toe A.I.

The A.I. is trained using [Q reinforcement learning](https://en.wikipedia.org/wiki/Q-learning). The built model is a CSV files of states and actions.

Given the state of the board and the current person's turn, the model returns an array of scores associated with all of the possible actions. The highest score is the ideal move.

The scores are built up slowly over many epochs of training where the AI is playing Tic-Tac-Toe against itself.

To improve my model over last time, I made two simple adjustments while training:
* The first move of every game was chosen at random.
* By rotating the board 90 degrees 3 times, I updated the scores of 4 states instead of one.

Despite my improvements, my model performed about the same as it had previously, with **a 97% win rate** when going first and **an 85% win rate** when going second.

## Getting Started

If you wish to play around with the model, you can clone the repo locally. In your terminal, navigate to the main folder of the cloned repo and type:
* 'pip install -r requirements.txt'
to install the requirements and then to play, type:
* 'python3 play.py'

### Prerequisites

You will need the latest version of Python to play.

## Authors

* **Jamie McCrory**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* https://towardsdatascience.com/simple-reinforcement-learning-q-learning-fcddc4b6fe56
* http://mnemstudio.org/path-finding-q-learning-tutorial.htm
* https://www.learndatasci.com/tutorials/reinforcement-q-learning-scratch-python-openai-gym/
