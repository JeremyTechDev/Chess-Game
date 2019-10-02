from piece import Piece

class bishop(Piece):   
  def __init__(self, x, y, team):
    #get symbol from symbols.py
    if team == "w":
      chessman = "♗"
      name = "White Bishop"
    else:
      chessman = "♝"
      name = "Black Bishop"

    Piece.__init__(self, x, y, team, name, chessman) 

  #----------------------------------------------------
  #Returns ALL the moves for bishop
  def getMoves(self):
    moves = [] #the return item
    a = self.x
    b = self.y

    #stats adding the four next-moves
    moves.append([a+1, b+1])
    moves.append([a+1, b-1])
    moves.append([a-1, b+1])
    moves.append([a-1, b-1])

    i = 1
    #while pos[a,b] is on board
    #GOING UP-RIGHT THE BOARD
    while(not checkForPiece(a-i, b+i) and (a-i >= 0) and (b+i <= 7)):
      moves.append([a-i, b+i])
      
      #checks if rook can eat a piece and add that move as possible
      if (checkForPiece(a-i-1, b+i+1)):
        if(getPieceAtPosition(a-i-1, b+i+1).team != self.team):
          moves.append([a-i-1, b+i+1])
          
      i += 1


    i = 1
    #GOING DOWN-RIGHT THE BOARD
    while(not checkForPiece(a+i, b+i) and (a+i <= 7) and (b+i <= 7)):
      moves.append([a+i, b+i])
      
      if(checkForPiece(a+i+1, b+i+1)):
        if (getPieceAtPosition(a+i+1, b+i+1).team != self.team):
          moves.append([a+i+1, b+i+1])
          
      i += 1
    
    i = 1
    #GOING UP-LEFT THE BOARD
    while(not checkForPiece(a-i, b-i) and (b-i >= 0) and (a-i >= 0)):
      moves.append([a-i, b-i])
      
      if(checkForPiece(a-i-1, b-i-1)):
        if (getPieceAtPosition(a-i-1, b-i-1).team != self.team):
          moves.append([a-i-1, b-i-1])
          
      i += 1

    i = 1
    #GOING DOWN-LEFT THE BOARD
    while(not checkForPiece(a+i, b-i) and (b+i >= 0) and (a+i <= 7)):
      moves.append([a+i, b-i])
      
      if(checkForPiece(a+i+1, b-i-1)):
        if (getPieceAtPosition(a+i+1, b-i-1).team != self.team):
          moves.append([a+i+1, b-i-1])
          
      i += 1

    return self.discardImMoves(moves)