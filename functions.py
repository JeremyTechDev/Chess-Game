from piece import *

#returns [x][y] position on board style [ch][#]
def toBoard(x, y):
  listX = [8,7,6,5,4,3,2,1,0,0,0,0]
  listY = ["A","B","C","D","E","F","G","H","0","0","0","0"]

  return listY[y] + str(listX[x])

#returns [ch][#] position on sys style [x][y]
#accepts either values like a8 or 8a
#second paramether to set is def can print a message
def toSys(pos, tell):
  #if len(pos) longer then 3, tell it only takes firts two chars to pos[x][y]
  if len(pos) >= 3 and tell == True:
    print("")
    print('>>> Only "' + pos[:2] + '" in consideration.')

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