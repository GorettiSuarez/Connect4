#Práctica de Fundamentos de Sistemas Inteligentes

Desarrollo de una heurística y funcionalidades varias sobre un código básico del juego Conecta 4.

##Introduccion

  En esta primera práctica de la asignatura, se efectuan los cambios necesarios en el codigo suministrado por el profesor para el correcto funcionamiento del juego Conecta 4. Asimismo, se efectuan las modificaciones opcionales pedidas en el enunciado de la práctica para un funcionamiento más adecuado del juego. 

##Apartados obligatorios
####Heuristicas

  Se han implementado dos heuristicas:
  1. Una heuristica random, llamada *h_random*, que es capaz de detectar posibles cuatro en rayas del adversario y cortarlos, y el resto de movimientos los efectua de manera aleatoria.
  2. Una heuristica más elaborada, llamada *mih*, que contabiliza el numero de casillas blancas y del jugador actual, sumando 5 por las casillas blancas y 15 por las casillas propias. Esto se efectua tanto para mis posibles cuatro en rayas como para los del adversario, y el valor devuelto será la resta de ambos. Esta funcion de puntaje de casillas se hace en vertical,horizontal y en diagonal con respecto a las posibles tiradas.

####Modos de seleccion
  Se permite seleccionar el nivel de dificultad en el que se quiere jugar (fácil,medio o difícil), lo cual se consigue gracias a que aumentamos el nivel de profundidad de la busqueda alfa-beta, y también permitimos la selección de que usuario comienza la partida (máquina o humano).

##Apartados opcionales

####Memoize
  Se implementa el patrón de diseño Memoize en base a lo explicado en clases de laboratorio de la propia asignatura. Se cogio el codigo de ejemplo que proporcionaba el profesor y se adaptó a la heuristica *mih* para ahorrarnos calculos en la heuristica y aumentar la velocidad de juego.

####Maquina vs Maquina
  Se permite seleccionar el modo de juego *Maquina vs Maquina* para que puedan competir dos heuristicas diferentes (o iguales). Estas heuristicas deben estar definidas en el archivo *heuristica.py* y se debe especificar en *run.py* que heuristica se pasa para cada uno de los jugadores (línea 69 para jugador 'O' y línea 71 para jugador 'X').
