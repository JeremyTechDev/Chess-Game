from piece import Piece

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
    print("")
    print("Choose one piece (number) to replace your pawn:")
    print("1. ♕ ♛  Queen")
    print("2. ♔ ♚  King")
    print("3. ♗ ♝  Bishop")
    print("4. ♘ ♞  Knight")
    print("5. ♖ ♜  Rook")
    print("6. ♙ ♟ Pawn")

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