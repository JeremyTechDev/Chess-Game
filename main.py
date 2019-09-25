from classes import *
from functions import *

#Main functions of the game
#whitePieces = 16
#blackPieces = 16

#-------------------------------------------------------
def runTurn(team):
  #checks that the user's choice is ok and that there are moves for that piece
  while True:
    print("")
    print("Insert the position of the piece to move:")
    piecePosition = input()

    #make sure input is not only one character or digit
    if len(piecePosition) == 0 or len(piecePosition) == 1:
      print("The input should be one letter and one digit, try again")
    else:
      if toSys(piecePosition):
        #the position in this variable is ok
        piecePosition = toSys(piecePosition)

        #check that there are possible moves,
        #otherwive, asks again for position
        if validateForPiece(piecePosition, team):
          #set piece position [x][y]
          x = piecePosition[0]
          y = piecePosition[1]
          #get the specific piece
          piece = getPieceAtPosition(x, y)
          #find all moves for the piece after finding the piece type with getMoveFunction(piece)
          allPossibleMoves = getMoveFunction(piece)(piece, x, y)

          if len(allPossibleMoves) == 0:
            print("No possible moves for " + chessman_names[piece.chessman] + ", try another one")
          else:
            #prints the board showing the possible moves of the piece chosen as ( )
            printBoard(allPossibleMoves)

            #shows choices for the move of the piece
            print("Chose your next move for the " + chessman_names[piece.chessman] +":")
            for move in allPossibleMoves:
              posX = move[0]
              posY = move[1]
              print(">>> " + toBoard(posX, posY))
            #shows a option in case user what to change piece
            print("")
            print('Insert "0" if you want to chose another piece')
            
            #read the position to
            while True:
              positionTo = input()
              #make sure input is not only one character or digit
              if len(positionTo) == 0 or len(positionTo) == 1:
                print("The input should be one letter and one digit, try again")
              else:
                if positionTo == "0":
                  printBoard(None)
                  runTurn(team)
                  break

                if toSys(positionTo):
                  positionTo = toSys(positionTo)

                  if [positionTo[0], positionTo[1]] in allPossibleMoves:
                    movePieceTo(piece, positionTo[0], positionTo[1])
                    break
                  else:
                    print("That move is not possible, check the list and try again")

                else:
                  print("Invaid position, try another one")

            break #finishes the while with all success by the user

        else:
          print("Empty spot, try another one")

      else:
        print("Invaid position, try another one")

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
#runs while the game is not over
def startGame():
  lastTurn = "b"
  while True:
    if lastTurn == "b":
      lastTurn = "w" 
      opTeam = "b" #oppsite team
      teamKing = wki
      teamName = "WHITE"
    else:
      lastTurn = "b"
      opTeam = "w" #oppsite team
      teamKing = bki
      teamName = "BLACK"
    
    printBoard(None) #prints actual state of the board
    #if king is on check, player must protect it
    if isOnCheck(teamKing, lastTurn, opTeam):
      print(teamName + " KING IS ON CHECK, PROTECT IT")
      
      a = protectKing(teamKing, opTeam)
      for i in a:
        print(toBoard(i[0], i[1]))
    else:
      print(">>>" + teamName + "'S TURN")
      runTurn(lastTurn)

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
movePieceTo(bki, 5, 2)
startGame()
#movePieceTo(bki, 5, 2)
#printBoard(None)
#print(ifCheck(bki, "b", "w"))
#protectKing(bki, "w")