#from classes import all_pieces
from symbols import nums, lets, legend, chessman_names


from symbols import *
#from functions import *

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



board = [
  ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
  ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
  ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
  ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
  ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
  ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
  ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
  ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"]
]
#------------------------------------------------------
#prints the board with the actuals positions
def print_board():
  print("")

  #prints each row
  for i in range(0, 8):
    st = ""
    for j in range(0, 8):
      #if piece at position [x][y], prints Piece
      #otherwise, prints empty space '[ ]'
      if (checkForPiece(i,j)):
        st += getSymbol(i,j)
      else:
        st += board[i][j]
    
    #print num of row, then the array, and then the part 
    #corresponding to the legend
    print(nums[i] + st + " " + legend[i])

  #print upper letters
  print("   ", end="")
  for i in lets:
    print(i, end="")
  print("")
  
  space()

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
#Return the type of piece that there is in
#[x][y]. Ex: bp1 --> white pawn 
#To print the right symbol 
def getSymbol(x,y):
  for piece in all_pieces:
    if piece.onGame == True:
      if piece.x == x and piece.y == y:
        return " " + piece.chessman + " "
  return "[ ]"

#------------------------------------------------------
#Returns the piece at given position [x][y]
#Return None if there is no piece at position [x][y]
def getPieceAtPosition(x,y):
  for piece in all_pieces:
    if piece.onGame == True:
      if piece.x == x and piece.y == y:
        return piece
  return None

#------------------------------------------------------
def movePieceTo(piece, x, y):
  if not checkForPiece(x,y):
    #print the piece that moved
    moved = chessman_names[piece.chessman]
    position = toBoard(x,y) #gets boards position
    print(moved + " moved to " + position)
    piece.moveTo(x, y)
  else:
    pieceOnSpot = getPieceAtPosition(x, y)
    if pieceOnSpot.team != piece.team:
      #to print kill message
      killed = chessman_names[pieceOnSpot.chessman]
      killer = chessman_names[piece.chessman]
      print(killed + " killed by a " + killer)
      pieceOnSpot.kill()
      piece.moveTo(x, y)
    else:
      print("Spot occupied by your chessman")

#------------------------------------------------------
#returns [x][y] position on board style [ch][#]
def toBoard(x, y):
  listX = [8,7,6,5,4,3,2,1]
  listY = ["A","B","C","D","E","F","G","H"]

  return listY[y] + str(listX[x])

#------------------------------------------------------
#returns [ch][#] position on sys style [x][y]
def toSys(pos):
  let = (pos[0]).upper()
  num = pos[1]

  listY = ["A","B","C","D","E","F","G","H"]
  listX = [8,7,6,5,4,3,2,1]

  if (let in listY) and 1 <= int(num) <= 8:
    return listX.index(int(num)), listY.index(let)

#------------------------------------------------------
#prints space to separe content
def space():
  print("")
  print("")
  print("")
  print("")


"""
            GETTERS OF PIECE MOVES
    returns a list if ALL the moves a piece can make
    LATER, we remove the impossible moves
    needs the position of the piece [x][y] and the piece
    [a][b] == [x][y] used not to change any data
"""

#------------------------------------------------------
#Discards all imposible moves for any piece
def discardImMoves(piece, moves):
  toDelete = []

  #check if piece on move spot
  for move in moves:
    if checkForPiece(move[0], move[1]):
      pieceAtSpot = getPieceAtPosition(move[0], move[1])
      if piece.team == pieceAtSpot.team:
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

  return moves #returns all posible moves for a piece

#------------------------------------------------------
#Return ALL the moves for pawns
def getAllPawnMoves(pawn, x, y):
  moves = [] #the return item
  a = x
  b = y

  #check move direction by team
  if (pawn.team == "w"):
    a -= 1
    moves.append([a, b]) #one step up

    if (pawn.firstMove == True):
      pawn.firstMove = False
      moves.append([a-1,b]) #two steps up
  else:
    a += 1
    moves.append([a, b]) #one step down
    if (pawn.firstMove == True):
      pawn.firstMove = False
      moves.append([a+1,b])  #two step down
  
  #check if piece can eat an other
  possEat1 = [a,b-1] #possible Eat 1
  possEat2 = [a,b+1] #possible Eat 1
  if (checkForPiece(possEat1[0], possEat1[1]) == True): #if there is a piece
    if (getPieceAtPosition(possEat1[0], possEat1[1]).team != pawn.team): 
      moves.append(possEat1) #if is different team, add move
  #same with second piece
  if (checkForPiece(possEat2[0], possEat2[1]) == True):
    if (getPieceAtPosition(possEat2[0], possEat2[1]).team != pawn.team):
      moves.append(possEat2)

  return discardImMoves(pawn, moves)

#----------------------------------------------------
#Returns ALL the moves for knights
def getAllKnightMoves(knight, x, y):
  moves = [] #the return item
  a = x
  b = y

  #there are just 8 moves for every knight
  moves.append([a-2, b+1])
  moves.append([a-1, b+2])
  moves.append([a+1, b+2])
  moves.append([a+2, b+1])
  moves.append([a+2, b-1])
  moves.append([a+1, b-2])
  moves.append([a-1, b-2])
  moves.append([a-2, b-1])

  return discardImMoves(knight, moves)

#----------------------------------------------------
#Returns ALL the moves for king
def getAllKingMoves(king, x, y):
  moves = [] #the return item
  a = x
  b = y

  #there are just 8 moves for every king
  moves.append([a-1, b])
  moves.append([a-1, b+1])
  moves.append([a, b+1])
  moves.append([a+1, b+1])
  moves.append([a+1, b])
  moves.append([a+1, b-1])
  moves.append([a, b-1])
  moves.append([a-1, b-1])

  return discardImMoves(king, moves)


