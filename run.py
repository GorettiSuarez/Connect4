# coding=utf-8
import games
import heuristicas

level = raw_input("Elija nivel --> facil(1), medio(2) o dificil(3):  ")
while level != '1' and level != '2' and level != '3':
    level = raw_input("Elija correctamente el nivel --> facil(1), medio(2) o dificil(3):  ")

mode = raw_input("Elija modo de juego -->  Máquina vs Máquina (1) o Jugador vs Máquina (2):")
while mode != '1' and mode != '2':
    mode = raw_input("Elija correctamente el modo de juego -->  Máquina vs Máquina (1) o Jugador vs Máquina (2):)")

if mode == '2':
    first = raw_input("Decide si empieza la maquina(X) o tu(O): ")
    while first != 'X' and first != 'O':
        first = raw_input("Decide correctamente si empieza la maquina(X) o tu(O): ")
    player = first
else:
    player = 'X'

# game = games.TicTacToe(h=3,v=3,k=3)
game = games.ConnectFour(var=player)

state = game.initial


# O siempre es humano y X siempre es maquina

def machineMove(state2, player2, nextPlayer,heuristic):
    print "Thinking..."
    # move = games.minimax_decision(state, game)
    # move = games.alphabeta_full_search(state, game)
    if level == '1':
        move = games.alphabeta_search(state2, game, eval_fn=heuristic, d=1, player=player2)
    elif level == '2':
        move = games.alphabeta_search(state2, game, eval_fn=heuristic, d=2, player=player2)
    else:
        move = games.alphabeta_search(state2, game, eval_fn=heuristic, d=4, player=player2)

    global state
    state = game.make_move(move, state2)
    global player
    player = nextPlayer


while True:
    print "Jugador a mover:", game.to_move(state)
    game.display(state)

    if player == 'O':
        if mode == '2':
            col_str = raw_input("Movimiento: ")
            coor = int(str(col_str).strip())
            while coor < 1 or coor > 7:
                col_str = raw_input("Introduzca un movimiento valido - Movimiento: ")
                coor = int(str(col_str).strip())

            x = coor
            y = -1
            legal_moves = game.legal_moves(state)
            for lm in legal_moves:
                if lm[0] == x:
                    y = lm[1]

            state = game.make_move((x, y), state)
            player = 'X'
        else:

            machineMove(state, player, 'X',heuristicas.mih)
    else:
        machineMove(state, player, 'O',heuristicas.mih)

    print "-------------------"
    if game.terminal_test(state):
        game.display(state)
        print "Final de la partida"
        break
