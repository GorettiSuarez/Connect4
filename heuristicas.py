from random import randint
from games import *


def memoize(f):
    memo = {}

    # x es el state del board
    def helper(state, player):
        key_and_value = tuple(state.board.items())
        if key_and_value not in memo:
            memo[key_and_value] = f(state, player)
        return memo[key_and_value]

    return helper


def h_random(state, player):
    if state.utility != 0:
        if player == 'X':
            return state.utility * infinity
        else:
            return -state.utility * infinity

    return randint(0, 100)


def number_in_row(board, move, player, delta):
    value = 0
    n = 0
    x, y = move
    while board.get((x, y)) == player or board.get((x, y)) is None:
        if x > 7 or x < 0 or y > 6 or y < 0:
            break
        if board.get((x, y)) == player:
            value += 15
        if board.get((x, y)) is None:
            value += 5
        x, y = x + delta[0], y + delta[1]
        n += 1

    x, y = move
    while board.get((x, y)) == player or board.get((x, y)) is None:
        if x > 7 or x < 0 or y > 6 or y < 0:
            break
        if board.get((x, y)) == player:
            value += 15
        if board.get((x, y)) is None:
            value += 5
        x, y = x - delta[0], y - delta[1]
        n += 1

    n -= 1

    # Si se llega aqui es hay mas de 4 posiciones recorridas y es una heuristica valida
    if n >= 4:
        return value
    else:
        return 0


def sum_heuristic(state, move, player):
    sumH = 0
    sumH += number_in_row(state.board, move, player, (1, 0))
    sumH += number_in_row(state.board, move, player, (0, 1))
    sumH += number_in_row(state.board, move, player, (1, 1))
    sumH += number_in_row(state.board, move, player, (1, -1))
    return sumH


@memoize
def mih(state, player):
    if state.utility != 0:
        if player == 'X':
            return state.utility * infinity
        else:
            return -state.utility * infinity

    h_X = 0

    for move in legal_moves(state):
        h_X += sum_heuristic(state, move, 'X')

    h_O = 0
    for move in legal_moves(state):
        h_O += sum_heuristic(state, move, 'O')

    return h_X - h_O


def legal_moves(state):
    "Legal moves are any square not yet taken."
    return [(x, y) for (x, y) in state.moves
            if y == 1 or (x, y - 1) in state.board]
