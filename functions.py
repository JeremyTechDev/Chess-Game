from symbols import nums,lets
from classes import *

#------------------------------------------------------
#prints the board with the actuals positions
def print_board(board):
  print("")
  #print upper letters
  print("   ", end="")
  for i in lets:
    print(i, end="")
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