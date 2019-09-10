from symbols import *
from functions import *

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