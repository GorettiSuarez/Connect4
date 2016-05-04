from random import randint
from games import *

def h0(self):
    return randint(-100,100)

def h1(state):
    #Leer del tablero
    higher = 0
    for x in legal_moves(state):
        k_inVO = k_in_row(state.board,x,'O',(1,0))
        print("AQUI VIENE EL k_inVO")
        print(k_inVO)
        if higher < k_inVO:
            higher = k_inVO
        if state.utility != 0 or len(state.moves) == 0:
            return infinity
    print("AQUI VIENE EL HIGHER: ")
    print(higher)
    return higher
    #Se devuelve en negativo porque la calculas para O, entonces su mejor jugada NO te favoreceria
#Devolver la diferencia de las mejores jugadas de cada uno

def k_in_row(board, move, player, (delta_x, delta_y)):
    "Return true if there is a line through move on board for player."
    x, y = move
    point = 0  # n is number of moves in row
    n = 0
    m = 0
    b = 0
    #Comprobar que no salga del tablerito
    while (board.get((x, y)) == player or board.get((x,y)) == None) and n <= 3:
        if x > 7 or x<0 or y>7 or y<0:
            break

        if board.get((x,y)) == player:
            print(x,m)
            m += 1
            point += 100
        if board.get((x,y)) == None:
            print(x,b)
            b += 1
            point += 20
        # n += 1
        x, y = x + delta_x, y + delta_y
        n+= 1
    x, y = move
    n=0
    while (board.get((x, y)) == player or board.get((x,y)) == None) and n <= 3:
        if x > 7 or x < 0 or y>7 or y<0:
            break

        if board.get((x, y)) == player:
            print(x, m)
            m += 1
            point += 100
        if board.get((x, y)) == None:
            print(x, b)
            b += 1
            point += 20
        #point += 1000
        x, y = x - delta_x, y - delta_y
    #n -= 1  # Because we counted move itself twice
    return point


def legal_moves(state):
    "Legal moves are any square not yet taken."

    return [(x, y) for (x, y) in state.moves
            if y == 1 or (x, y - 1) in state.board]