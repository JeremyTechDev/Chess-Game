from classes import *
from functions import *

#Main functions of the game
"""
RUNS BY CYCLES
>Each cycle is when both White and Black make a move.
>Stars the game by a White Move.
>Every move, checks if the game is finished, prints board, and
prints the last move of the game.

>For each move:
>1. Ask the position of the piece to move
>2. Shows all possible move for that piece
>3. User chose one move the his or her turn is over
>4. The same with the next player
"""
def startGame():
  pass

printBoard(None)
movePieceTo(wk1, 3, 2)
printBoard(None)
#probitional- to print pieces' moves
a = (getKnightMoves(wk1, wk1.x, wk1.y))
printBoard(a)
for i in a:
  print(toBoard(i[0],i[1]), end=" - ")