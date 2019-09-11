from symbols import *
from functions import *

"""
PARAMETHERS:
X -> number of the List
Y -> index on the List Y
team -> black or white
chessman -> variable with the name of the symbol

FUNCTIONS:
kill -> set the piece out of the game
moveTo -> move given piece to the position [x][y]
"""

class Piece():
  def __init__(self,x,y,team,chessman):
    self.x = x
    self.y = y
    self.team = team
    self.chessman = chessman
    self.onGame = True

  def kill(self):
    self.onGame = False

  def moveTo(self, x, y):
      self.x = x
      self.y = y

#CHILD OBJECTS
class pawn(Piece):
  def __init__(self, x, y, team, chessman):
    Piece.__init__(self, x, y, team, chessman)
    self.firstMove = True 

class rook(Piece):
  def __init__(self, x, y, team, chessman):
    Piece.__init__(self, x, y, team, chessman) 

class knight(Piece):
  def __init__(self, x, y, team, chessman):
    Piece.__init__(self, x, y, team, chessman)

class bishop(Piece):
  def __init__(self, x, y, team, chessman):
    Piece.__init__(self, x, y, team, chessman) 

class king(Piece):
  def __init__(self, x, y, team, chessman):
    Piece.__init__(self, x, y, team, chessman) 

class queen(Piece):
  def __init__(self, x, y, team, chessman):
    Piece.__init__(self, x, y, team, chessman) 

"""
INITIAL POSITIONS
Position are set by the index of each list,
NOT by a matrix. "X" is number of the list and
"Y" is the index of the listX.
Position [0][0] is the top left spot
Position [7][7] is the bottom right spot
"""

#WHITES
wp1 = pawn(6,0,"w", swp)
wp2 = pawn(6,1,"w", swp)
wp3 = pawn(6,2,"w", swp)
wp4 = pawn(6,3,"w", swp)
wp5 = pawn(6,4,"w", swp)
wp6 = pawn(6,5,"w", swp)
wp7 = pawn(6,6,"w", swp)
wp8 = pawn(6,7,"w", swp)
wr1 = rook(7,0,"w", swr)
wr2 = rook(7,7,"w", swr)
wk1 = knight(7,1,"w", swk)
wk2 = knight(7,6,"w", swk)
wb1 = bishop(7,2,"w", swb)
wb2 = bishop(7,5,"w", swb)
wki = king(7,3,"w", swki)
wqu = queen(7,4,"w", swq)

#BLACKS
bp1 = pawn(1,0,"b", sbp)
bp2 = pawn(1,1,"b", sbp)
bp3 = pawn(1,2,"b", sbp)
bp4 = pawn(1,3,"b", sbp)
bp5 = pawn(1,4,"b", sbp)
bp6 = pawn(1,5,"b", sbp)
bp7 = pawn(1,6,"b", sbp)
bp8 = pawn(1,7,"b", sbp)
br1 = rook(0,0,"b", sbr)
br2 = rook(0,7,"b", sbr)
bk1 = knight(0,1,"b", sbk)
bk2 = knight(0,6,"b", sbk)
bb1 = bishop(0,2,"b", sbb)
bb2 = bishop(0,5,"b", sbb)
bki = king(0,3,"b", sbki)
bqu = queen(0,4,"b", sbq)

all_pieces = [wp1,wp2,wp3,wp4,wp5,wp6,wp7,wp8,wr1,wr2,wk1,wk2,wb1,wb2,wki,wqu,bp1,bp2,bp3,bp4,bp5,bp6,bp7,bp8,br1,br2,bk1,bk2,bb1,bb2,bki,bqu]