from piece import Piece

class queen(Piece):  
  def __init__(self, x, y, team):
    #get symbol from symbols.py
    if team == "w":
      chessman = "♕"
      name = "White Queen"
    else:
      chessman = "♛"
      name = "Black Queen"
    
    Piece.__init__(self, x, y, team, name, chessman) 

  #---------------------------------------------------
  #Returns Queen moves
  #As queen moves are equal to all the moves of the king, bishop and rook
  #This function adds together all those moves from that position
  def getMoves(self):
    moves = [] #return item
    a = self.x
    b = self.y

    #Get moves like king's
    moves.append([a-1, b])
    moves.append([a-1, b+1])
    moves.append([a, b+1])
    moves.append([a+1, b+1])
    moves.append([a+1, b])
    moves.append([a+1, b-1])
    moves.append([a, b-1])
    moves.append([a-1, b-1])

    #get moves like rook's
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

    #get moves like bishop's
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