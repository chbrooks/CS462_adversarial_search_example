from unittest import TestCase
from TicTacToeState import TicTacToeState
from search import minimax

class Test(TestCase):
    def test_minimax(self):
        t = TicTacToeState()
        b1 =    [['x', 'o', 'o'],
                 [' ', 'o', 'x'],
                 [ 'x', 'x', 'o']]
        t.board = b1
        score = minimax(t, 'x')
        print(score)
