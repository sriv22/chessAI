import math
import chessBoard as cb
from random import choice
import copy
import itertools

class chessCom:
  
  def getOpponentColor (self, color):
     return "White" if color == "Black" else "Black"

  def makeMove(self,guiBoard,color):
    board = copy.deepcopy(guiBoard.grid)
    antiColor = self.getOpponentColor (color)
      
    firstMoves = self.simulateTurn(board,color,guiBoard)[:]           # Moves for current color (Black)

    for second in firstMoves:                    # second contains: [moveGrid, piece[0], move, pieceValue,[]]
      second[4] = self.simulateTurn(second[0],antiColor,guiBoard)[:]    # Moves for opponent (White)
      for third in second[4]:
        third[4] = self.simulateTurn(third[0],color,guiBoard)[:]    # Moves for current color (Black)
    
    sPieceVal = 0                                                     # Second Iteration pieceValue
    tPieceVal = 0                                                     # Third iteration pieceValue
    for i in firstMoves:                                              # Traverses through Black moves 
      for j in i[4]:                                                  # Traverses through moves of opponent - White
        for k in j[4]:                                                # Traverses through moves of Black based on White
          if k[3] > tPieceVal:
            tPieceVal = k[3]                                          # kth move is beneficial to Black
        j[3] = j[3] - tPieceVal                # Therefore, not a worthwile move for White -  possibility of not taking it
        if j[3] > sPieceVal:                   
          sPieceVal = j[3]                                            # Worthwile move for White
      i[3] = i[3] - sPieceVal                                         # Therefore, not worthwile for Black
    
    bestMoves = []
    maxValue = 0
    for move in firstMoves:                                           # Piece Values are updated
      if move[3] > maxValue or move[3] == maxValue:                                
        bestMoves.append(move)                                        # Append most worthwile move
        maxValue = move[3]

    try:
      return choice(bestMoves)                                        # Randomly picks best move
    except:
      return choice(firstMoves)                                       # Else choose from firstMoves
    
  def simulateTurn(self,temp,color,guiBoard):
    """Returns array of valid moves
         temp - board copy
         color - color of current turn
         guiBoard - chessBoard
    """
    antiColor = self.getOpponentColor (color)                                     # Opposing color identified
    self.myPieces = []                                                            # location, value (type)
 
    for r,c in itertools.product(range(len(temp[0])), range(len(temp))):   
      if temp[r][c] != 0:
        if color == guiBoard.pieces[temp[r][c]][1]:                           # If color of piece at the spot is equivalent to color of piece, then append
          self.myPieces.append([[r,c],temp[r][c]])

    validMoves = []                                                               # Array of valid moves
    for piece in self.myPieces:                                                   # Traverses through pieces and determines valid move based on piece
        if piece[1]%6 == 1:
            possibleMoves = guiBoard.detPawnSpaces(temp,piece[0],color)[:]
        elif piece[1]%6 == 2:
            possibleMoves = guiBoard.detKnightSpaces(temp,piece[0],color)[:]
        elif piece[1]%6 == 3:
            possibleMoves = guiBoard.detBishopSpaces(temp,piece[0],antiColor)[:]
        elif piece[1]%6 == 4:
            possibleMoves = guiBoard.detRookSpaces(temp,piece[0],antiColor)[:]
        elif piece[1]%6 == 5:
            possibleMoves = guiBoard.detQueenSpaces(temp,piece[0],antiColor)[:]
        else:
            possibleMoves = guiBoard.detKingSpaces(temp,piece[0],color)[:]

        for move in possibleMoves:
            if 0 <= move[0] < 8 and  0 <= move[1] < 8 and guiBoard.turnValid(temp,piece[0],move,color):      # Valid move
                moveGrid = copy.deepcopy(temp)                                      # Copies entire board
                pieceValue = moveGrid[move[0]][move[1]] % 6                         # value of the piece on the grid

                if guiBoard.inCheck(moveGrid, color):                               # If Black is in check,
                  pieceValue += 10                                                  # Increase urgency of the move
                
                moveGrid[move[0]][move[1]] = piece[1]; 
                moveGrid[piece[0][0]][piece[0][1]] = 0

                if not guiBoard.inCheck(moveGrid,color):                            # if current color Black is not in check
                  if guiBoard.inCheck(moveGrid,antiColor):                          # White is in check, pieceValue is greater
                      pieceValue += 3
                  if piece[1]%6 == 1 and (move[0] == 8 or move[0] == 0):            # If piece is a pawn and is in the last row (8 or 0 y coord)
                      pieceValue += 5                                               # Because it is close to promotion
                  validMoves.append([moveGrid, piece[0], move, pieceValue,[]])
    return validMoves