from classes import *
from functions import *

print_board()
#probitional- to print pieces' moves
a = (getAllKingMoves(wki, wki.x, wki.y))
for i in a:
  print(toBoard(i[0],i[1]), end=" - ")