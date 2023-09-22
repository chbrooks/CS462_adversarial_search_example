import copy

### State representing a Tic-Tac-Toe board. ' ' is used for unfilled squares.
### An abstract class that other states will inherit from.
class State:
    def __init__(self):
        pass
    def is_goal(self):
        pass
    def successors(self):
        pass
    def __repr__(self):
        pass


class TicTacToeState(State):
    def __init__(self, board=None):
        self.score = 0
        if board:
            self.board = board
        else:
            self.board = [[' ', ' ', ' '],
                          [' ', ' ', ' '],
                          [' ', ' ', ' ']]


    def is_goal(self):
        ### we have a win
        if row_win(self.board) or col_win(self.board) or diagonal_win(self.board):
            return True
        elif board_full(self.board):
            return True
        else:
            return False

    ## move is either 'x' or 'o'
    def successors(self, move='x'):
        successorStates = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    newBoard = copy.deepcopy(self.board)
                    newBoard[i][j] = move
                    successorStates.append(TicTacToeState(newBoard))

        return successorStates

    ### player is either x or o
    def scoreSelf(self, player):
        winner = row_win(self.board)
        if not winner:
            winner = col_win(self.board)
        if not winner:
            winner = diagonal_win(self.board)
        if winner:
            if winner == player:
                self.score = 1
            else:
                self.score = -1
        else :
            self.score = 0

    def __repr__(self):
        return " %s\n %s\n %s\n" % (self.board[0], self.board[1], self.board[2])




#############
## TicTacToeState

### Helper functions to determine whether we are at a leaf node.

def row_win(board):
    for row in board:
        if len(set(row)) == 1 and row[0] != ' ':
            return row[0]
    return False


def col_win(board):
    for i in range(3):
        col = [item[i] for item in board]
        if len(set(col)) == 1 and col[0] != ' ' :
            return col[0]
    return False


def diagonal_win(board):
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[1][1] != ' ':
        return board[1][1]
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[1][1] != ' ':
        return board[1][1]
    else:
        return False


def board_full(board):
    if any(x == ' ' for x in board[0]) or any(x == ' ' for x in board[1]) or any(x == ' ' for x in board[2]):
        return False
    else:
        return True
