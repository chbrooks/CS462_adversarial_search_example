from unittest import TestCase
from TicTacToeState import TicTacToeState

class TestTicTacToeState(TestCase):
    def test_is_goal(self):
        t = TicTacToeState()
        t.board =   [['x', ' ', ' '],
                    [' ', 'x', ' '],
                    [' ', ' ', 'x']]
        self.assertTrue(t.is_goal())

        t.board = [['x', ' ', ' '],
                   [' ', 'o', ' '],
                   [' ', ' ', 'x']]
        self.assertFalse(t.is_goal())


    def test_score_self(self):
        t = TicTacToeState()
        t.board = [['x', ' ', ' '],
                   [' ', 'x', ' '],
                   [' ', ' ', 'x']]
        t.scoreSelf('x')
        self.assertEqual(t.score, 1)
        t.scoreSelf('o')
        self.assertEqual(t.score, -1)