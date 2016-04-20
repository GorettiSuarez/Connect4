import games
import heuristicas

aux1 = raw_input("Quien empiezaX-O: ")
aux2 = str(aux1).strip()
while(aux2 != 'X' and aux2 != 'O'):
    aux1 = raw_input("Quien empieza X-O: ")
    aux2 = str(aux1).strip()

player = aux2

#game = games.TicTacToe(h=3,v=3,k=3)
game = games.ConnectFour(var=player)

state = game.initial

#O siempre es humano y X siempre es maquina



while True:
    print "Jugador a mover:", game.to_move(state)
    game.display(state)

    if player == 'O':
        col_str = raw_input("Movimiento: ")
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
        #move = games.minimax_decision(state, game)
        #move = games.alphabeta_full_search(state, game)
        move = games.alphabeta_search(state, game,eval_fn=heuristicas.h0)

        state = game.make_move(move, state)
        player = 'O'
    print "-------------------"
    if game.terminal_test(state):
        game.display(state)
        print "Final de la partida"
        break