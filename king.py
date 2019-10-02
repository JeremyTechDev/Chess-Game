from piece import Piece

class king(Piece):
  def __init__(self, x, y, team):
    #get symbol from symbols.py
    if team == "w":
      chessman = "♔"
      name = "White King"
    else:
      chessman = "♚"
      name = "Black King"

    Piece.__init__(self, x, y, team, name, chessman) 
  
  #----------------------------------------------------
  #Returns ALL the moves for king
  def getMoves(self):
    moves = [] #the return item
    a = self.x
    b = self.y

    #there are just 8 moves for every king
    moves.append([a-1, b])
    moves.append([a-1, b+1])
    moves.append([a, b+1])
    moves.append([a+1, b+1])
    moves.append([a+1, b])
    moves.append([a+1, b-1])
    moves.append([a, b-1])
    moves.append([a-1, b-1])
    
    return self.discardImMoves(moves)