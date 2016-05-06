from random import randint
from games import *

def h0(self):
    return randint(-100,100)



def number_in_row(board, move, player, delta):
    value = 0
    n = 0
    m = 0
    x, y = move
    while (board.get((x, y)) == player or board.get((x, y)) is None):
        if x > 7 or x < 0 or y > 6 or y < 0:
            break
        if board.get((x, y)) == player:
            m +=1
            value += 5
        if board.get((x, y)) is None:
            value += 1
        x, y = x + delta[0], y + delta[1]
        n += 1

    x, y = move
    while (board.get((x, y)) == player or board.get((x, y)) is None):
        if x > 7 or x < 0 or y > 6 or y < 0:
            break
        if board.get((x, y)) == player:
            m += 1
            value += 5
        if board.get((x, y)) is None:
            value += 1
        x, y = x - delta[0], y - delta[1]
        n += 1

    n -= 1

    if  m == 3:
        return -55555555555

    if n>=4:
        return value
    else:
        return 0


def mih(state):
    h_X = 0

    for move in legal_moves(state):
        h_X += number_in_row(state.board, move, 'X', (1, 0))
        h_X += number_in_row(state.board, move, 'X', (0, 1))
        h_X += number_in_row(state.board, move, 'X', (1, 1))
        h_X += number_in_row(state.board, move, 'X', (1, -1))

    h_O = 0
    for move in legal_moves(state):
        h_O += number_in_row(state.board, move, 'O', (1, 0))
        h_O += number_in_row(state.board, move, 'O', (0, 1))
        h_O += number_in_row(state.board, move, 'O', (1, 1))
        h_O += number_in_row(state.board, move, 'O', (1, -1))

    return h_X - h_O

#ESTO NO SIRVE
def h1(state):
    #Leer del tablero
    higher = 0
    higher2 = 0
    for move in legal_moves(state):

        k_inVO = k_in_row(state.board,move,'O',(1,0))
        k_inVX = k_in_row(state.board, move, 'X', (1,0))

        k_inHO = k_in_row(state.board, move, 'O', (0,1))
        k_inHX = k_in_row(state.board, move, 'X', (0,1))

        resultado= k_inVO - k_inVX
        resultado2= k_inHO - k_inHX

        if higher < resultado:
            higher = resultado
        if higher < resultado2:
            higher2 = resultado2

        if state.utility != 0 or len(state.moves) == 0:
            return infinity

    return higher2 - higher



    #Se devuelve en negativo porque la calculas para O, entonces su mejor jugada NO te favoreceria
#Devolver la diferencia de las mejores jugadas de cada uno

def k_in_row(board, move, player, (delta_x, delta_y)):
    "Return true if there is a line through move on board for player."
    x, y = move
    point = 0  # n is number of moves in row
    n = 0
    #Comprobar que no salga del tablerito
    while (board.get((x, y)) == player or board.get((x,y)) is None) and n <= 3:
        if x > 7 or x < 0 or y > 7 or y < 0:
            break
        if board.get((x,y)) == player:
            point += 100
        if board.get((x,y)) is None:
            point += 20

        x, y = x + delta_x, y + delta_y
        n+= 1
    x, y = move
    n=0
    while (board.get((x, y)) == player or board.get((x,y)) is None) and n <= 3:
        if x > 7 or x < 0 or y > 7 or y < 0:
            break
        if board.get((x, y)) == player:
            point += 100
        if board.get((x, y)) is None:
            point += 20

        x, y = x - delta_x, y - delta_y
    return point


def legal_moves(state):
    "Legal moves are any square not yet taken."

    return [(x, y) for (x, y) in state.moves
            if y == 1 or (x, y - 1) in state.board]