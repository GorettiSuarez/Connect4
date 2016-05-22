# coding=utf-8
import games
import heuristicas


level = raw_input("Elija nivel --> facil(1), medio(2) o dificil(3):  ")
level2 = int(str(level))
while(level2 != 1 and level2 != 2 and level2 != 3):
    level = raw_input("Elija BIEN el nivel --> facil(1), medio(2) o dificil(3):  ")
    level2 = int(str(level))

mode = raw_input("Elija modo de juego -->  Máquina vs Máquina (1) o Jugador vs Máquina (2):")
mode2 = int(str(mode))
while(mode2 != 1 and mode2 != 2):
    mode = raw_input("Elija modo de juego -->  Máquina vs Máquina (1) o Jugador vs Máquina (2):)")
    mode2 = int(str(mode))

if(mode2 == 2):
    first = raw_input("Decide si empieza la maquina(X) o tu(O): ")
    first2 = str(first)
    while (first2 != 'X' and first2 != 'O'):
        first = raw_input("Decide si empieza la maquina(X) o tu(O): ")
        first2 = str(first)

    player = first2
else:
    player = 'X'


#game = games.TicTacToe(h=3,v=3,k=3)
game = games.ConnectFour(var=player)

state = game.initial

#O siempre es humano y X siempre es maquina



while True:
    print "Jugador a mover:", game.to_move(state)
    game.display(state)

    if player == 'O':
        if (mode2 == 2):
            col_str = raw_input("Movimiento: ")
            coor = int(str(col_str).strip())
            while(coor < 1 or coor > 7):
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
            print "Thinking..."
            # move = games.minimax_decision(state, game)
            # move = games.alphabeta_full_search(state, game)
            if level2 == 1:
                move = games.alphabeta_search(state, game, eval_fn=heuristicas.mih, d=1,player=player)
            elif level2 == 2:
                move = games.alphabeta_search(state, game, eval_fn=heuristicas.mih, d=2,player=player)
            else:
                move = games.alphabeta_search(state, game, eval_fn=heuristicas.mih, d=4,player=player)

            state = game.make_move(move, state)
            player = 'X'

    else:
        print "Thinking..."
        #move = games.minimax_decision(state, game)
        #move = games.alphabeta_full_search(state, game)
        if level2 == 1:
            move = games.alphabeta_search(state, game, eval_fn=heuristicas.mih, d=1)
        elif level2 == 2:
            move = games.alphabeta_search(state, game, eval_fn=heuristicas.mih, d=2)
        else:
            move = games.alphabeta_search(state, game,eval_fn=heuristicas.mih, d=4)

        state = game.make_move(move, state)
        player = 'O'
    print "-------------------"
    if game.terminal_test(state):
        game.display(state)
        print "Final de la partida"
        break
