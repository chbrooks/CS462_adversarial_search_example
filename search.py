from TicTacToeState import TicTacToeState



def BFS(initialState) :
    searchQueue = [initialState]

    while len(searchQueue) > 0 :
        currentNode = searchQueue.pop(0)
        if currentNode.isGoal() :
            return currentNode
        else :
            successorStates = currentNode.successors()
            searchQueue.extend(successorStates)
    return None


def flipPlayer(player) :
    if player == 'x' :
        return 'o'
    else :
        return 'x'

##  x is maximizing, o is minimizing

def minimax(current_state, is_x=True) :
    if current_state.is_goal() :
        current_state.scoreSelf('x')
        return current_state.score
    else :
        if is_x :
            best_val = -2
            next_moves = current_state.successors(move='x')
            for move in next_moves :
                best_val = max(best_val, minimax(move, False))
            return best_val
        else :
            best_val = 2
            next_moves = current_state.successors(move='o')
            for move in next_moves :
                best_val = min(best_val, minimax(move, True))
            return best_val




