from classes import *
from functions import *

#Main functions of the game
#whitePieces = 16
#blackPieces = 16

#-------------------------------------------------------
def runTurn(team):
  #prints actual state of the board
  printBoard(None)

  #shows the player that have to make the move
  if team == "w":
    print("> WHITES'S Turn <")
  else:
    print("> BLACK'S Turn <")

  print("Insert the position of the piece to move:")
  piecePosition = toSys(input())

  #if the choice is ok, it continues
  #otherwise ask the piece again
  if validateForPiece(piecePosition, team):
    #set piece position [x][y]
    x = piecePosition[0]
    y = piecePosition[1]
    #get the specific piece
    piece = getPieceAtPosition(x, y)
    #find all moves for the piece after finding the piece type with getMoveFunction(piece)
    allPossibleMoves = getMoveFunction(piece)(piece, x, y)
    #prints the board showing the possible moves of the piece chosen as ( )
    printBoard(allPossibleMoves)

    #shows choices for the move of the piece
    print("Chose your next move for the " + chessman_names[piece.chessman] +":")
    for move in allPossibleMoves:
      posX = move[0]
      posY = move[1]
      print(">>> " + toBoard(posX, posY))
    
    #tries to make the move
    spot = toSys(input())
    if [spot[0], spot[1]] in allPossibleMoves:
      movePieceTo(piece, spot[0], spot[1])
    else:
      print("Move not possible")
  else:
    print("Ask again")

#--------------------------------------------------------
#return the getMoves funtions that must be used
#depending on the piece chosen by the user
def getMoveFunction(piece):
  if piece.__class__ == pawn:
    return getPawnMoves
  elif piece.__class__ == rook:
    return getRookMoves
  elif piece.__class__ == knight:
    return getKnightMoves
  elif piece.__class__ == bishop:
    return getBishopMoves
  elif piece.__class__ == king:
    return getKingMoves
  elif piece.__class__ == queen:
    return getQueenMoves

#--------------------------------------------------------------
#return True if the choosen piece to move is able to move
#takes in consideration if there is a piece is that pos and
#if the piece is the same team of the player in turn
def validateForPiece(piecePosition, team):
  x = piecePosition[0]
  y = piecePosition[1]
  if not checkForPiece(x, y):
    return False
  else:
    if getPieceAtPosition(x, y).team != team:
      return False

  return True
  

"""
RUNS BY CYCLES
>Each cycle is when both White and Black make a move.
>Stars the game by a White Move.
>Every move, checks if the game is finished, prints board, and
prints the last move of the game.

>For each move:
>1. Ask the position of the piece to move
>2. Shows all possible move for that piece
>3. User chose one move the his or her turn is over
>4. The same with the next player
"""
def startGame():
  #runs while the game is not over
  gameOver = False
  while not gameOver:
    
    runTurn("w")
    runTurn("b")
    #gameOver = True

"""
printBoard(None)
movePieceTo(wk1, 3, 2)
printBoard(None)
#probitional- to print pieces' moves
a = (getKnightMoves(wk1, wk1.x, wk1.y))
printBoard(a)
for i in a:
  print(toBoard(i[0],i[1]), end=" - ")
"""
movePieceTo(wp1, 2,0)
startGame()