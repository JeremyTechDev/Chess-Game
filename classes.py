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

    #remove piece from corresponding list
    if self in all_black_pieces:
      all_black_pieces.remove(self)
    
    if self in all_white_pieces:
      all_white_pieces.remove(self)

  def moveTo(self, x, y):
    self.x = x
    self.y = y

  #------------------------------------------------------
  #Discards all imposible moves for any piece
  def discardImMoves(self, moves):
    toDelete = []

    #check if piece on move spot
    for move in moves:
      if checkForPiece(move[0], move[1]):
        pieceAtSpot = getPieceAtPosition(move[0], move[1])
        if self.team == pieceAtSpot.team:
          #if piece is the same team, remove that move
          toDelete.append(move)

    #identifies moves outside of the board
    for move in moves:
      for cord in move:
        if cord < 0 or cord > 7:
          toDelete.append(move)

    #deletes moves outside the board
    for i in toDelete:
      if i in moves:
        moves.remove(i)

    #identifies repeated moves and discard them
    finalMoves = []
    for move in moves:
      if move not in finalMoves:
        finalMoves.append(move)

    return finalMoves #returns all posible moves for a piece

#CHILD OBJECTS
class pawn(Piece):
  def __init__(self, x, y, team):
    #get symbol from symbols.py
    if team == "w":
      chessman = swp
    else:
      chessman = sbp

    Piece.__init__(self, x, y, team, chessman)
    self.userMoves = 0 
  
  #return pawn's possible moves
  def getMoves(self):
    moves = [] #the return item
    a = self.x
    b = self.y

    #check move direction by team
    if (self.team == "w"):
      a -= 1
      if not checkForPiece(a, b): #if front is empty
        moves.append([a, b]) #one step up

        if (self.userMoves == 0 and not checkForPiece(a-1, b)):
          self.firstMove = False
          moves.append([a-1,b]) #two steps up
    else:
      a += 1
      if not checkForPiece(a, b): #if front is empty
        moves.append([a, b]) #one step down

        if (self.userMoves == 0 and not checkForPiece(a+1, b)):
          self.firstMove = False
          moves.append([a+1,b])  #two step down
    
    #check if piece can eat an other
    possEat1 = [a,b-1] #possible Eat 1
    possEat2 = [a,b+1] #possible Eat 1
    if (checkForPiece(possEat1[0], possEat1[1]) == True): #if there is a piece
      if (getPieceAtPosition(possEat1[0], possEat1[1]).team != self.team): 
        moves.append(possEat1) #if is different team, add move
    #same with second piece
    if (checkForPiece(possEat2[0], possEat2[1]) == True):
      if (getPieceAtPosition(possEat2[0], possEat2[1]).team != self.team):
        moves.append(possEat2)

    return self.discardImMoves(moves)

class rook(Piece):   
  def __init__(self, x, y, team):
    #get symbol from symbols.py
    if team == "w":
      chessman = swr
    else:
      chessman = sbr

    Piece.__init__(self, x, y, team, chessman) 

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

class knight(Piece):   
  def __init__(self, x, y, team):
    #get symbol from symbols.py
    if team == "w":
      chessman = swk
    else:
      chessman = sbk

    Piece.__init__(self, x, y, team, chessman)

class bishop(Piece):   
  def __init__(self, x, y, team):
    #get symbol from symbols.py
    if team == "w":
      chessman = swb
    else:
      chessman = sbb

    Piece.__init__(self, x, y, team, chessman) 

class king(Piece):
  def __init__(self, x, y, team):
    #get symbol from symbols.py
    if team == "w":
      chessman = swki
    else:
      chessman = sbki

    Piece.__init__(self, x, y, team, chessman) 

class queen(Piece):  
  def __init__(self, x, y, team):
    #get symbol from symbols.py
    if team == "w":
      chessman = swq
    else:
      chessman = sbq
    
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
wp1 = pawn(6,0,"w")
wp2 = pawn(6,1,"w")
wp3 = pawn(6,2,"w")
wp4 = pawn(6,3,"w")
wp5 = pawn(6,4,"w")
wp6 = pawn(6,5,"w")
wp7 = pawn(6,6,"w")
wp8 = pawn(6,7,"w")
wr1 = rook(7,0,"w")
wr2 = rook(7,7,"w")
wk1 = knight(7,1,"w")
wk2 = knight(7,6,"w")
wb1 = bishop(7,2,"w")
wb2 = bishop(7,5,"w")
wki = king(7,4,"w")
wqu = queen(7,3,"w")

#BLACKS
bp1 = pawn(1,0,"b")
bp2 = pawn(1,1,"b")
bp3 = pawn(1,2,"b")
bp4 = pawn(1,3,"b")
bp5 = pawn(1,4,"b")
bp6 = pawn(1,5,"b")
bp7 = pawn(1,6,"b")
bp8 = pawn(1,7,"b")
br1 = rook(0,0,"b")
br2 = rook(0,7,"b")
bk1 = knight(0,1,"b")
bk2 = knight(0,6,"b")
bb1 = bishop(0,2,"b")
bb2 = bishop(0,5,"b")
bki = king(0,4,"b")
bqu = queen(0,3,"b")

all_white_pieces = [wp1,wp2,wp3,wp4,wp5,wp6,wp7,wp8,wr1,wr2,wk1,wk2,wb1,wb2,wki,wqu]
all_black_pieces = [bp1,bp2,bp3,bp4,bp5,bp6,bp7,bp8,br1,br2,bk1,bk2,bb1,bb2,bki,bqu]
all_pieces = [wp1,wp2,wp3,wp4,wp5,wp6,wp7,wp8,wr1,wr2,wk1,wk2,wb1,wb2,wki,wqu,bp1,bp2,
bp3,bp4,bp5,bp6,bp7,bp8,br1,br2,bk1,bk2,bb1,bb2,bki,bqu]



#------------------------------------------------------
#Returns True if there is a piece in [x][y]
#otherwise, returns False
def checkForPiece(x, y):
  for piece in all_pieces:
    if piece.onGame == True:
      if piece.x == x and piece.y == y:
        return True 
  return False

#------------------------------------------------------
#Returns the piece at given position [x][y]
#Return None if there is no piece at position [x][y]
def getPieceAtPosition(x,y):
  for piece in all_pieces:
    if piece.onGame == True:
      if piece.x == x and piece.y == y:
        return piece
  return None
