"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = 0
    o_count = 0
    for row in board:
        x_count += row.count(X)
        o_count += row.count(O)
    if (x_count + o_count) % 2 == 0:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                actions.append((i,j))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    turn = player(board)
    new_board = copy.deepcopy(board)
    i = action[0]
    j = action[1]

    if board[i][j] == None:
        new_board[i][j] = turn
        return new_board

    raise Exception("Invalid Move")


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for j in range(3):
        if board[0][j] != None:
            if j == 0:
                if board[0][0] == board[1][0] and board[0][0] == board[2][0]:
                    return board[0][0]
                elif board[0][0] == board[0][1] and board[0][0] == board[0][2]:
                    return board[0][0]
                elif board[0][0] == board[1][1] and board[0][0] == board[2][2]:
                    return board[0][0]
            if j == 1:
                if board[0][1] == board[1][1] and board[0][1] == board[2][1]:
                    return board[0][1]
            if j == 2:
                if board[0][2] == board[1][2] and board[0][2] == board[2][2]:
                    return board[0][2]
                elif board[0][2] == board[1][1] and board[0][2] == board[2][0]:
                    return board[0][2]
    for i in range(1,3):
        if board[i][0] != None:
            if i == 1:
                if board[1][0] == board[1][1] and board[1][0] == board[1][2]:
                    return board[1][0]
            if i == 2:
                if board[2][0] == board[2][1] and board[2][0] == board[2][2]:
                    return board[2][0]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True

    for i in range(3):
        for j in range(3):
            if board[i][j] != None:
                continue
            else:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)

    if w == X:
        return 1
    elif w == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None

    if board == [[EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY]]:
        return (1,1)

    p = player(board)
    a = (None, None)

    if p == X:
        v = -math.inf
        for action in actions(board):
            new_board = result(board, action)
            v_new = min_value(new_board)
            if v_new > v:
                v = v_new
                a = action

    else:
        v = math.inf
        for action in actions(board):
            new_board = result(board, action)
            v_new = max_value(new_board)
            if v_new < v:
                v = v_new
                a = action

    return a


def min_value(board):
    if terminal(board):
        return utility(board)

    v = math.inf

    for action in actions(board):
        v = min(v, max_value(result(board, action)))

    return v


def max_value(board):
    if terminal(board):
        return utility(board)

    v = -math.inf

    for action in actions(board):
        v = max(v, min_value(result(board, action)))

    return v