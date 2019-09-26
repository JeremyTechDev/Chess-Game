from classes import *
from symbols import nums, lets, legend, chessman_names

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
def printBoard(spots):
  print("")

  #prints each row
  for i in range(0, 8):
    st = ""
    for j in range(0, 8):
      #if piece at position [x][y], prints Piece
      #otherwise, prints empty space '[ ]'
      if (checkForPiece(i,j)):
        if((spots != None) and ([i, j] in spots)): #checks if move-spot in position to print ()
          st += "(" + getSymbol(i, j)[1] + ")"
        else: #otherwise, only prints the piece 
          st += getSymbol(i,j)
      else:
        if((spots != None) and ([i, j] in spots)): #checks if move-spot in position to print ()
          st += "( )"
        else: #otherwise, only prints []
          st += board[i][j]
    
    #print num of row, then the array, and then the part 
    #corresponding to the legend
    print(nums[i] + st + " " + legend[i])

  #print upper letters
  print("   ", end="")
  for i in lets:
    print(i, end="")
  print("")
  print("") #separator lines

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

      """
      #decrease by one the number of pieces
      if pieceOnSpot.team == "w":
        whitePieces -= 1
      else:
        blackPieces -= 1
      """
    else:
      print("Spot occupied by your chessman")

  if piece.__class__ == pawn:
    piece.userMoves += 1

  #check if pawn is on the other side to ask
  #for the piece to add and replace the pawn
  #for white piece
  if (piece.__class__ == pawn) and (piece.team == "w") and (piece.x == 0):
    replacePawn(piece, x, y)
  #for black piece
  if (piece.__class__ == pawn) and (piece.team == "b") and (piece.x == 7):
    replacePawn(piece, x, y)

#------------------------------------------------------
#when pawn reaches the other edge, asks the user with
#which piece wants to replace the pawn
def replacePawn(pawn, x, y):
  print("")
  print("Choose one piece (number) to replace your pawn:")
  print("1. " + swq,sbq + "  Queen")
  print("2. " + swki,sbki + "  King")
  print("3. " + swb,sbb + "  Bishop")
  print("4. " + swk,sbk + "  Knight")
  print("5. " + swr,sbr + "  Rook")
  print("6. " + swp,sbp + "  Pawn")

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
        pawn.kill()
        addedQueen = queen(x, y, pawn.team)
        all_pieces.append(addedQueen)
        print("Pawn replaced by a Queen")
      elif choice == 2:
        pawn.kill()
        addedKing = king(x, y, pawn.team)
        all_pieces.append(addedKing)
        print("Pawn replaced by a King")
      elif choice == 3:
        pawn.kill()
        addedBishop = bishop(x, y, pawn.team)
        all_pieces.append(addedBishop)
        print("Pawn replaced by a Bishop")
      elif choice == 4:
        pawn.kill()
        addedKnight = knight(x, y, pawn.team)
        all_pieces.append(addedKnight)
        print("Pawn replaced by a Knight")
      elif choice == 5:
        pawn.kill()
        addedRook = rook(x, y, pawn.team)
        all_pieces.append(addedRook)
        print("Pawn replaced by a Rook")

      break
    else:
      print("Invalid input, please try again")

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

"""
  POSITION TRANSLATE FUNCTIONS
"""
#------------------------------------------------------
#returns [x][y] position on board style [ch][#]
def toBoard(x, y):
  listX = [8,7,6,5,4,3,2,1]
  listY = ["A","B","C","D","E","F","G","H"]

  return listY[y] + str(listX[x])

#------------------------------------------------------
#returns [ch][#] position on sys style [x][y]
#accepts either values like a8 or 8a
def toSys(pos):
  if pos[0].isnumeric():
    num = pos[0]
    let = (pos[1]).upper()
  else:
    let = (pos[0]).upper()
    num = pos[1]

  listY = ["A","B","C","D","E","F","G","H"]
  listX = [8,7,6,5,4,3,2,1]

  if (let in listY) and 1 <= int(num) <= 8:
    return listX.index(int(num)), listY.index(let)

"""
  END GAME FUNTIONS
"""
#-----------------------------------------------------
#return a team's all possible moves, ignoring the pawns
def getTeamMoves(team):
  result = [] #return item

  #get the team's pieces
  if team == "w":
    teamList = all_white_pieces
  else:
    teamList = all_black_pieces

  for piece in teamList:
    #ignore pawn up and down moves
    if piece.__class__ != pawn:
      moves = getMoveFunction(piece)(piece, piece.x, piece.y)
    else: #consider pawns kill moves
      moves = getKillerPawnMoves(piece, piece.x, piece.y) 

    for move in moves:
      #check if move is not repeated and piece is not temporaly there
      if move not in result and checkForPiece(piece.x, piece.y):
        result.append(move)
  
  return result

#-----------------------------------------------------
#Returns True is the king of the given team is on check
#Otherwise, returns False
def isOnCheck(king, team, oppositeTeam):
  #get kings postiion [x][y]
  posKing = [king.x, king.y]

  #if there is a piece different that the king in that position,
  #temporaly move it to out of the board because it is virtualy killed
  tPiece = None
  actTX = None
  actTY = None
  for piece in all_pieces:
    piecePos = [piece.x, piece.y]
    if piecePos == posKing and piece != king:
      tPiece = piece
      actTX = piece.x
      actTY = piece.y
      #move piece to temporal new position
      piece.moveTo(9, 9)
      break

  #get all rival possible moves
  rivalMoves = getTeamMoves(oppositeTeam)

  #get piece back to its position
  if tPiece != None:
    tPiece.moveTo(actTX, actTY)

  if posKing in rivalMoves:
    return True
  else:
    return False

#----------------------------------------------------
#return all the attacker of the king at position [x][y],
#all the pieces that can kill the king on the next move
def getKingsAttackers(king, oppositeTeam):
  kingsAttackers = [] #return item
  posKing = [king.x, king.y]
  allKingMoves = getKingMoves(king, king.x, king.y)

  #get the team's pieces
  if oppositeTeam == "w":
    teamList = all_white_pieces
  else:
    teamList = all_black_pieces

  for piece in teamList:
    moves = getMoveFunction(piece)(piece, piece.x, piece.y)
    for move in moves:
      if move in allKingMoves or move == posKing:
        kingsAttackers.append(piece)
  
  return kingsAttackers

#Return all moves of the king's attackers
def getKingsAttackersMoves(kingsAttackers):
  result = [] #return item

  for piece in kingsAttackers:
    moves = getMoveFunction(piece)(piece, piece.x, piece.y)
    for move in moves:
      if move not in result:
        result.append(move)
  
  return result

#-------------------------------------------------------
#shows all the pieces that can move to protect the king
#return a list of moves that can save the king
def protectKing(king, oppositeTeam):
  savingKingMoves = [] #return item

  #get king's moves
  kingMoves = getKingMoves(king, king.x, king.y)

  #save king's actual positions to return to it later
  actKingX = king.x
  actKingY = king.y

  #consider moves in the king's next position
  #given by the kingMoves
  for kingM in kingMoves:
    possX = kingM[0] #possible next X
    possY = kingM[1] #possible next Y
    #move the king to the possible next move
    king.moveTo(possX, possY)
    #if king is on check in that position, in not savingMove
    if not isOnCheck(king, king.team, oppositeTeam):
      savingKingMoves.append([king.x, king.y])
  
  #return king to its original possition
  king.moveTo(actKingX, actKingY)

  return savingKingMoves

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

  #identifies repeated moves and discard them
  finalMoves = []
  for move in moves:
    if move not in finalMoves:
      finalMoves.append(move)

  return finalMoves #returns all posible moves for a piece

#-------------------------------------------------------
#return a list of the kings moves with no moves that can
#cause a check mate
def discardCheckMoves(king, moves):
  toDelete = [] #add check mate moves here to delete later
  #save king's real position
  a = king.x 
  b = king.y

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
    king.moveTo(move[0], move[1])
    if king.team == "w":
      opTeam = "b"
    else:
      opTeam = "w"
    if isOnCheck(king, king.team, opTeam):
      toDelete.append(move) #to delete later

    #move piece on spot back to real place
    if pieceOnSpot != None:
      pieceOnSpot.moveTo(posX, posY)
  
    #move king back to its real position
    king.moveTo(a, b)
  
  #delete check mete moves
  for rem in toDelete:
    if rem in moves:
      moves.remove(rem)

  return moves #king's moves with no check mate moves

#------------------------------------------------------
#Return ALL the moves for pawns
def getPawnMoves(pawn, x, y):
  moves = [] #the return item
  a = x
  b = y

  #check move direction by team
  if (pawn.team == "w"):
    a -= 1
    if not checkForPiece(a, b): #if front is empty
      moves.append([a, b]) #one step up

      if (pawn.userMoves == 0 and not checkForPiece(a-1, b)):
        pawn.firstMove = False
        moves.append([a-1,b]) #two steps up
  else:
    a += 1
    if not checkForPiece(a, b): #if front is empty
      moves.append([a, b]) #one step down

      if (pawn.userMoves == 0 and not checkForPiece(a+1, b)):
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
def getKnightMoves(knight, x, y):
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
def getKingMoves(king, x, y):
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

#----------------------------------------------------
#Returns ALL the moves for rook
def getRookMoves(rook, x, y):
  moves = [] #the return item
  a = x
  b = y  

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
      if(getPieceAtPosition(a-i-1, b).team != rook.team):
        moves.append([a-i-1, b])
    i += 1

  i = 1
  #GOING DOWN THE BOARD
  while(not checkForPiece(a+i, b) and (a+i <= 7)):
    moves.append([a+i, b])

    if(checkForPiece(a+i+1, b)):
      if (getPieceAtPosition(a+i+1, b).team != rook.team):
        moves.append([a+i+1, b])
    i += 1
  
  i = 1
  #GOING LEFT THE BOARD
  while(not checkForPiece(a, b-i) and (b-i >= 0)):
    moves.append([a, b-i])

    if(checkForPiece(a, b-i-1)):
      if (getPieceAtPosition(a, b-i-1).team != rook.team):
        moves.append([a, b-i-1])
    i += 1

  i = 1
  #GOING RIGHT THE BOARD
  while(not checkForPiece(a, b+i) and (b+i <= 7)):
    moves.append([a, b+i])

    if(checkForPiece(a, b+i+1)):
      if (getPieceAtPosition(a, b+i+1).team != rook.team):
        moves.append([a, b+i+1])
    i += 1

  return discardImMoves(rook, moves)

#----------------------------------------------------
#Returns ALL the moves for bishop
def getBishopMoves(bishop, x, y):
  moves = [] #the return item
  a = x
  b = y  

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
      if(getPieceAtPosition(a-i-1, b+i+1).team != bishop.team):
        moves.append([a-i-1, b+i+1])
        
    i += 1


  i = 1
  #GOING DOWN-RIGHT THE BOARD
  while(not checkForPiece(a+i, b+i) and (a+i <= 7) and (b+i <= 7)):
    moves.append([a+i, b+i])
    
    if(checkForPiece(a+i+1, b+i+1)):
      if (getPieceAtPosition(a+i+1, b+i+1).team != bishop.team):
        moves.append([a+i+1, b+i+1])
        
    i += 1
  
  i = 1
  #GOING UP-LEFT THE BOARD
  while(not checkForPiece(a-i, b-i) and (b-i >= 0) and (a-i >= 0)):
    moves.append([a-i, b-i])
    
    if(checkForPiece(a-i-1, b-i-1)):
      if (getPieceAtPosition(a-i-1, b-i-1).team != bishop.team):
        moves.append([a-i-1, b-i-1])
        
    i += 1

  i = 1
  #GOING DOWN-LEFT THE BOARD
  while(not checkForPiece(a+i, b-i) and (b+i >= 0) and (a+i <= 7)):
    moves.append([a+i, b-i])
    
    if(checkForPiece(a+i+1, b-i-1)):
      if (getPieceAtPosition(a+i+1, b-i-1).team != bishop.team):
        moves.append([a+i+1, b-i-1])
        
    i += 1

  return discardImMoves(bishop, moves)

#---------------------------------------------------
#Returns Queen moves
"""
As queen moves are equal to all the moves of the king, bishop and rook
This function adds together all those moves from that position
"""
def getQueenMoves(queen, x, y):
  moves = [] #return item
  a = x
  b = y

  #Get all moves
  kingMoves = getKingMoves(queen, x, y)
  rookMoves = getRookMoves(queen, x, y)
  bishopMoves = getBishopMoves(queen, x, y)

  #add them to moves
  allMoves = [kingMoves, rookMoves, bishopMoves]
  for pieceMoves in  allMoves:
    for move in pieceMoves:
      moves.append(move)

  return discardImMoves(queen, moves)

#----------------------------------------------------
#Returns ALL the killer pawn moves
def getKillerPawnMoves(pawn, x, y):
  moves = [] #the return item
  a = x
  b = y
  #if it is up or down move
  if pawn.team == "w":
    a -= 1
  else: 
    a += 1

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

  #print(discardImMoves(pawn, moves))
  return discardImMoves(pawn, moves) 