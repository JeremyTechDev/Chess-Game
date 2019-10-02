from piece import Piece

class rook(Piece):   
  def __init__(self, x, y, team):
    #get symbol from symbols.py
    if team == "w":
      chessman = "♖"
      name = "White Rook"
    else:
      chessman = "♜"
      name = "Black Rook"

    Piece.__init__(self, x, y, team, name, chessman) 

  #----------------------------------------------------
  #Returns ALL the moves for rook
  def getMoves(self):
    moves = [] #the return item
    a = self.x
    b = self.y

    #stats adding the four next-moves
    moves.append([a+1, b])
    moves.append([a-1, b])
    moves.append([a, b+1])
    moves.append([a, b-1])

    i = 1
    #while pos[a,b] is on board
    #GOING UP THE BOARD
    while(not checkForPiece(a-i, b) and (a-i >= 0)):
      moves.append([a-i, b])

      #checks if rook can eat a piece and add that move as possible
      if (checkForPiece(a-i-1, b)):
        if(getPieceAtPosition(a-i-1, b).team != self.team):
          moves.append([a-i-1, b])
      i += 1

    i = 1
    #GOING DOWN THE BOARD
    while(not checkForPiece(a+i, b) and (a+i <= 7)):
      moves.append([a+i, b])

      if(checkForPiece(a+i+1, b)):
        if (getPieceAtPosition(a+i+1, b).team != self.team):
          moves.append([a+i+1, b])
      i += 1
    
    i = 1
    #GOING LEFT THE BOARD
    while(not checkForPiece(a, b-i) and (b-i >= 0)):
      moves.append([a, b-i])

      if(checkForPiece(a, b-i-1)):
        if (getPieceAtPosition(a, b-i-1).team != self.team):
          moves.append([a, b-i-1])
      i += 1

    i = 1
    #GOING RIGHT THE BOARD
    while(not checkForPiece(a, b+i) and (b+i <= 7)):
      moves.append([a, b+i])

      if(checkForPiece(a, b+i+1)):
        if (getPieceAtPosition(a, b+i+1).team != self.team):
          moves.append([a, b+i+1])
      i += 1

    return self.discardImMoves(moves)