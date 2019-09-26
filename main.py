from classes import *
from functions import *

displayMenu() #start od the program

#FUNCTIONS
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

          #if piece is a king, discard check moves
          if piece.__class__ == king:
            allPossibleMoves = discardCheckMoves(piece, allPossibleMoves)

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
def runProtectKingTurn(king, oppositeTeam):
  print("Move it to a saving position, shown below:")
 
  #get saving moves:
  savingMoves = protectKing(king, oppositeTeam)

  #print board showing saving moves
  printBoard(savingMoves)

  #show moves
  for move in savingMoves:
    posX = move[0]
    posY = move[1]
    print(">>> " + toBoard(posX, posY))
  
  while True:
    positionTo = input()

    if len(positionTo) == 0 or len(positionTo) == 1:
      print("The input should be one letter and one digit, try again")
    else:
      if toSys(positionTo):
        positionTo = toSys(positionTo)

        if [positionTo[0], positionTo[1]] in savingMoves:
          movePieceTo(king, positionTo[0], positionTo[1])
          break
        else:
          print("That move is not possible, check the list and try again")

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
  
#----------------------------------
#get the name of the players
#avoids blank space inputs
def getPlayers():
  print("Insert a nickname for the WHITES PLAYER:")
  while True:
    wPlayer = input()
    if wPlayer != "" and wPlayer != " ":
      break
    else:
      print("Please, insert a valid name")

  print("Insert a nickname for the BLACKS PLAYER:")
  while True:
    bPlayer = input()
    if bPlayer != "" and bPlayer != " ":
      break
    else:
      print("Please, insert a valid name")
    
  return wPlayer, bPlayer

#-----------------------------------
#print how to play messages
def howToPlay():
  print(">>> HOW TO PLAY")
  print("This is how the board looks like:")
  printBoard(None)

  print("> This is the chess board, the black pieces are shown")
  print("  at the top and the white pieces, at the bottom.")
  print("")
  print("> Also, you have a legend of the pieces at the right")
  print("")
  print("> To play, the player on turn will have to choose the")
  print("  piece he or she wants to move by typing its cords.")
  print("> The cords are given by a letter and a number that are")
  print("  both at the left and bottom of the board. Ex: G3")
  print("")
  print("> Then, the possible moves for the chosen piece will be")
  print("  displayed. You only have to choose one of the shown cord")
  print("  the same way as before. Then your turn is over and your")
  print("  rival will play")
  print("")
  print("> Now you guys are all good to start playing!")
  print("")
  print(">>> Press any key to go back to the main menu")
  input()
  print("")
  displayMenu()

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
#parameter are the name of the players
def startGame(wPlayer, bPlayer):
  lastTurn = "b"
  while True: #set turn info
    if lastTurn == "b":
      lastTurn = "w" 
      opTeam = "b" #oppsite team
      teamKing = wki
      player = wPlayer
      opPlayer = bPlayer
      teamName = "WHITE"
      opTeamName = "BLACK"
    else:
      lastTurn = "b"
      opTeam = "w" #oppsite team
      teamKing = bki
      player = bPlayer
      opPlayer = wPlayer
      teamName = "BLACK"
      opTeamName = "WHITE"
    
    printBoard(None) #prints actual state of the board
    #if king is on check, player must protect it
    if isOnCheck(teamKing, lastTurn, opTeam):      
      #if there are no saving moves, its a check mate and game is over
      savingMoves = protectKing(teamKing, opTeam)
      if len(savingMoves) == 0:
        print("+++++++++++++++++++++++++++++++++++++")
        print("              GAME OVER   ")
        print("       " + opTeamName + "S ARE THE WINNERS")
        print("     CHECK MAKE ON " + teamName + "'S KING")
        print("")
        print("Congratulations, " + opPlayer + "!")
        print("+++++++++++++++++++++++++++++++++++++")
        exit() #ends program
      else:
        print(teamName + " KING IS ON CHECK, PROTECT IT")
        #run protect king to take him out of the check position
        runProtectKingTurn(teamKing, opTeam)
    else:
      print(">>> " + teamName + "'S TURN (" + player + ")")
      runTurn(lastTurn)

#---------------------------------------------
#           START OF THE PROGRAM
#---------------------------------------------
def displayMenu():
  print("++++++++++++++++++++++++++++++++++++")
  print("             CHESS GAME")
  print("")
  print("           1. Start Game")
  print("           2. How to Play")
  print("")
  print("              3. Exit")
  print("++++++++++++++++++++++++++++++++++++")
  print("Choose an option:")

  while True:
    choice = input()

    if choice != "" and int(choice):
      choice = int(choice)
      
      if choice == 1:
        #get players names
        players = getPlayers()
        print("")
        print(">>> GAME STARTED!")
        print("Good luck, " + players[0] + " and " + players[1] + "!")
        startGame(players[0], players[1])
      elif choice == 2:
        howToPlay()
      elif choice == 3:
        print(">>> THANKS FOR PLAYING, COME BACK SOON!")
        break
      else:
        print("Your choice must be a number between 1 and 3")
    else:
      print("Your choice must be a number [1-3]")