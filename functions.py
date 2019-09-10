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