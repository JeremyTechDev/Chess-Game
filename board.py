from functions import *

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
                    if((spots != None) and ([i, j] in spots)): #checks if move-spot in position to print ()
                        st += "(" + getSymbol(i, j)[1] + ")"
                    else: #otherwise, only prints the piece 
                        st += getSymbol(i,j)
                else:
                    if((spots != None) and ([i, j] in spots)): #checks if move-spot in position to print ()
                        st += "( )"
                    else: #otherwise, only prints []
                        st += "[ ]"
            
            #print num of row, then the array, and then the part 
            #corresponding to the legend
            print(board.nums[i] + st + " " + self.legend[i])

        #print upper letters
        print("   ", end="")
        for i in board.lets:
            print(i, end="")
        print("")
        print("") #separator lines

board = Board()
board.print(None)