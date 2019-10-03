from functions import *
"""
PARAMETHERS:
X -> number of the List
Y -> index on the List Y
team -> black or white
name -> name of the piece
chessman -> variable with the name of the symbol
onGame -> True if piece has not been killed yet
"""

class Piece():
  def __init__(self,x,y,team,name,chessman):
    self.x = x
    self.y = y
    self.team = team
    self.name = name
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
    #x and y are the new position

    #if the move is to empty spot, there is no kill
    if not checkForPiece(x,y):
      #print the piece that moved
      rtMessage = self.name + " moved to " + toBoard(x, y)
      #move the piece to new position
      self.x = x
      self.y = y
    else: #if it is to occupied spot, its a kill
      pieceOnSpot = getPieceAtPosition(x, y)
      if pieceOnSpot.team != self.team:
        #print kill message
        rtMessage = pieceOnSpot.name + " killed by a " + self.name
        pieceOnSpot.kill()
        #move the piece to new position
        self.x = x
        self.y = y

    #increment pawn moves to discard the posibility of doble jump on first move
    if self.__class__ == pawn:
      self.userMoves += 1

    #check if pawn is on the other side to ask for the piece to add and replace the pawn
    #for white piece
    if (self.__class__ == pawn) and (self.team == "w") and (self.x == 0):
      self.replace()
    #for black piece
    if (self.__class__ == pawn) and (self.team == "b") and (self.x == 7):
      self.replace()
    
    return rtMessage #to print the move 

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

#-----------------------------------------------------------------------
#>>>>>>>>>>>>>>>>>>>>>>>>>  CLASS PAWN
class pawn(Piece):
  def __init__(self, x, y, team):
    #get symbol from symbols.py
    if team == "w":
      chessman = "♙"
      name = "White Pawn"
    else:
      chessman = "♟"
      name = "Black Pawn"

    Piece.__init__(self, x, y, team, name, chessman)
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

  #----------------------------------------------------
  #Returns ALL the killer pawn moves
  def getKillerMoves(self):
    moves = [] #the return item
    a = self.x
    b = self.y
    #if it is up or down move
    if self.team == "w":
      a -= 1
    else: 
      a += 1

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
  
  #------------------------------------------------------
  #when pawn reaches the other edge, asks the user with
  #which piece wants to replace the pawn
  def replace(self):
    x = self.x
    y = self.y
    printMes = """
    Choose one piece (number) to replace your pawn:
    1. ♕ ♛  Queen
    2. ♔ ♚  King
    3. ♗ ♝  Bishop
    4. ♘ ♞  Knight
    5. ♖ ♜  Rook
    6. ♙ ♟ Pawn
    """
    print(printMes)

    #read the input, dont accept strings
    while True:  
      while True:
        try:
          choice = int(input())
          break
        except:
          print("Insert a number")

      #makes sure the num is on range of options
      if 1 <= int(choice) <= 5:
        choice = int(choice)
        print("") #space
        
        #create the new piece
        if choice == 1:
          self.kill()
          addedQueen = queen(x, y, self.team)
          all_pieces.append(addedQueen)
          print("Pawn replaced by a Queen")
        elif choice == 2:
          self.kill()
          addedKing = king(x, y, self.team)
          all_pieces.append(addedKing)
          print("Pawn replaced by a King")
        elif choice == 3:
          self.kill()
          addedBishop = bishop(x, y, self.team)
          all_pieces.append(addedBishop)
          print("Pawn replaced by a Bishop")
        elif choice == 4:
          self.kill()
          addedKnight = knight(x, y, self.team)
          all_pieces.append(addedKnight)
          print("Pawn replaced by a Knight")
        elif choice == 5:
          self.kill()
          addedRook = rook(x, y, self.team)
          all_pieces.append(addedRook)
          print("Pawn replaced by a Rook")

        break
      else:
        print("Invalid input, please try again")

#-----------------------------------------------------------------------
#>>>>>>>>>>>>>>>>>>>>>>>>>  CLASS ROOK
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

#-----------------------------------------------------------------------
#>>>>>>>>>>>>>>>>>>>>>>>>>  CLASS KNIGHT
class knight(Piece):   
  def __init__(self, x, y, team):
    #get symbol from symbols.py
    if team == "w":
      chessman = "♘"
      name = "White Knight"
    else:
      chessman = "♞"
      name = "Black Knight"

    Piece.__init__(self, x, y, team, name, chessman)

  #----------------------------------------------------
  #Returns ALL the moves for knights
  def getMoves(self):
    moves = [] #the return item
    a = self.x
    b = self.y

    #there are just 8 moves for every knight
    moves.append([a-2, b+1])
    moves.append([a-1, b+2])
    moves.append([a+1, b+2])
    moves.append([a+2, b+1])
    moves.append([a+2, b-1])
    moves.append([a+1, b-2])
    moves.append([a-1, b-2])
    moves.append([a-2, b-1])

    return self.discardImMoves(moves)

#-----------------------------------------------------------------------
#>>>>>>>>>>>>>>>>>>>>>>>>>  CLASS BISHOP
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

#-----------------------------------------------------------------------
#>>>>>>>>>>>>>>>>>>>>>>>>>  CLASS KING
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

  #-----------------------------------------------------
  #return a team's all possible moves, ignoring the pawns
  def getOpponetMoves(self):
    result = [] #return item

    #get the team's pieces
    if self.team == "w":
      teamList = all_black_pieces
    else:
      teamList = all_white_pieces

    for piece in teamList:
      #ignore pawn up and down moves
      if piece.__class__ != pawn:
        moves = piece.getMoves()
      else: #consider pawns kill moves
        moves = piece.getKillerMoves() 

      for move in moves:
        #check if move is not repeated
        if move not in result:
          result.append(move)
    
    return result

  #-----------------------------------------------------
  #Returns True is the king of the given team is on check
  #Otherwise, returns False
  def isOnCheck(self):
    #get kings postiion [x][y]
    posKing = [self.x, self.y]
    if self.team == "w":
      oppositeTeam = "b"
    else:
      oppositeTeam = "w"

    #if there is a piece different that the king in that position,
    #temporaly move it to out of the board because it is virtualy killed
    tPiece = None
    actTX = None
    actTY = None
    for piece in all_pieces:
      piecePos = [piece.x, piece.y]
      if piecePos == posKing and piece != self:
        tPiece = piece
        actTX = piece.x
        actTY = piece.y
        #move piece to temporal new position
        piece.moveTo(9, 9)
        break

    #get all rival possible moves
    rivalMoves = self.getOpponetMoves()

    #get piece back to its position
    if tPiece != None:
      tPiece.moveTo(actTX, actTY)

    if posKing in rivalMoves:
      return True
    else:
      return False

  #-------------------------------------------------------
  #shows all the pieces that can move to protect the king
  #return a list of moves that can save the king
  def getSavingMoves(self):
    savingKingMoves = [] #return item

    #set opposite team
    if self.team == "w":
      oppositeTeam = "b"
    else:
      oppositeTeam = "w"

    #get king's moves
    kingMoves = self.getMoves()

    #save king's actual positions to return to it later
    actKingX = self.x
    actKingY = self.y

    #consider moves in the king's next position
    #given by the kingMoves
    for kingM in kingMoves:
      possX = kingM[0] #possible next X
      possY = kingM[1] #possible next Y
      #move the king to the possible next move
      self.moveTo(possX, possY)
      #if king is on check in that position, in not savingMove
      if not self.isOnCheck():
        savingKingMoves.append([self.x, self.y])
    
    #return king to its original possition
    self.moveTo(actKingX, actKingY)

    return self.discardCheckMoves(savingKingMoves)

  #-------------------------------------------------------
  #return a list of the kings moves with no moves that can
  #cause a check mate
  def discardCheckMoves(self, moves):
    toDelete = [] #add check mate moves here to delete later
    #save king's real position
    a = self.x 
    b = self.y

    #discard move is there is check there, to avoid check mate
    for move in moves:
      #if piece at move spot, move it kill it temporaly to check check
      pieceOnSpot = None
      posX = None
      posY = None
      if checkForPiece(move[0], move[1]):
        pieceOnSpot = getPieceAtPosition(move[0], move[1])
        #save piece on spot real position
        posX = pieceOnSpot.x
        posY = pieceOnSpot.y

        #temporaly move the piece out of board
        pieceOnSpot.moveTo(9, 9)

      #move king to possible next move to check is chesk mate
      self.moveTo(move[0], move[1])
      if self.team == "w":
        opTeam = "b"
      else:
        opTeam = "w"
      if self.isOnCheck():
        toDelete.append(move) #to delete later

      #move piece on spot back to real place
      if pieceOnSpot != None:
        pieceOnSpot.moveTo(posX, posY)
    
      #move king back to its real position
      self.moveTo(a, b)
    
    #delete check mete moves
    for rem in toDelete:
      if rem in moves:
        moves.remove(rem)

    return moves #king's moves with no check mate moves
  
  #--------------------------------------------------------------
  def protect(self):
    print("Move it to a saving position, shown below:")

    #get opposite team
    opTeam = "b" if self.team == "w" else "w"

    #get saving moves:
    savingMoves = king.getSavingMoves()

    #print board showing saving moves
    board.print(savingMoves)

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
        if toSys(positionTo, False):
          positionTo = toSys(positionTo, True)

          if [positionTo[0], positionTo[1]] in savingMoves:
            movePieceTo(king, positionTo[0], positionTo[1])
            break
          else:
            print("That move is not possible, check the list and try again")

        else:
          print("Invaid position, try another one")

#-----------------------------------------------------------------------
#>>>>>>>>>>>>>>>>>>>>>>>>>  CLASS QUEEN
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