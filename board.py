from functions import *
from piece import *

"""
PARAMETHER:
board -> Full empty board
legend -> The side text of the board when print
lets -> Letters for the cords
nums -> Numbers for the cords

FUNCTIONS:
print -> print the board on different states,
if sports is not None, it will print the spots 
highlighted by ( )
"""
class Board():
    def __init__(self):
        self.board = [
        ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
        ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
        ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
        ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
        ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
        ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
        ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"],
        ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"]
        ]
        self.legend = legend = [
        "| SYMBOLS:",
        "| W B",
        "| ♔ ♚ KINGS",
        "| ♕ ♛ QUEENS",
        "| ♖ ♜ ROOKS",
        "| ♘ ♞ KNIGHTS",
        "| ♗ ♝ BISHOPS",
        "| ♙ ♟ PAWNS",
        ]
        self.lets = ["(A)","(B)","(C)","(D)","(E)","(F)","(G)","(H)"]
        self.nums = ["(8)","(7)","(6)","(5)","(4)","(3)","(2)","(1)"]


    #------------------------------------------------------
    #prints the board with the actuals positions
    def print(self, spots):
        print("")

        #prints each row
        for i in range(0, 8):
            st = ""
            for j in range(0, 8):
                #if piece at position [x][y], prints Piece
                #otherwise, prints empty space '[ ]'
                if (checkForPiece(i,j)):
                    piece = getPieceAtPosition(i, j)
                    if((spots != None) and ([i, j] in spots)): #checks if move-spot in position to print ()
                        st += "(" + piece.chessman + ")"
                    else: #otherwise, only prints the piece 
                        st += " " + piece.chessman + " "
                else:
                    if((spots != None) and ([i, j] in spots)): #checks if move-spot in position to print ()
                        st += "( )"
                    else: #otherwise, only prints []
                        st += "[ ]"
            
            #print num of row, then the array, and then the part 
            #corresponding to the legend
            print(self.nums[i] + st + " " + self.legend[i])

        #print upper letters
        print("   ", end="")
        for i in self.lets:
            print(i, end="")
        print("")
        print("") #separator lines