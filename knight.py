from piece import Piece

class knight(Piece):   
  def __init__(self, x, y, team):
    #get symbol from symbols.py
    if team == "w":
      chessman = "♘"
      name = "White Knight"
    else:
      chessman = "♞"
      name = "Black Knight"

    Piece.__init__(self, x, y, team, name, chessman)

  #----------------------------------------------------
  #Returns ALL the moves for knights
  def getMoves(self):
    moves = [] #the return item
    a = self.x
    b = self.y

    #there are just 8 moves for every knight
    moves.append([a-2, b+1])
    moves.append([a-1, b+2])
    moves.append([a+1, b+2])
    moves.append([a+2, b+1])
    moves.append([a+2, b-1])
    moves.append([a+1, b-2])
    moves.append([a-1, b-2])
    moves.append([a-2, b-1])

    return self.discardImMoves(moves)