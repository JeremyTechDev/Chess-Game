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