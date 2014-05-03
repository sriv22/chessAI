import chessBoard as cb
import unittest

class chessTest(unittest.TestCase):
    def testPawn(self):
        self.board = cb.chessBoard()
        currPos = []
        currPos.append(1)                 # (1,1)
        currPos.append(1)
        pieceType = 1                     # Pawn
        color = "Black"
        self.board.grid[currPos[0]][currPos[1]] = pieceType

        endPos1 = []                      # (2,4) : False
        endPos1.append(2)
        endPos1.append(4)

        endPos2 = []                      # (1,2) : False
        endPos2.append(1)
        endPos2.append(2)

        endPos3 = []                      # (1,2) : True
        endPos3.append(2)
        endPos3.append(1)


        self.assertFalse(self.board.turnValid(self.board.grid, currPos, endPos1, color))
        self.assertFalse(self.board.turnValid(self.board.grid, currPos, endPos2, color))
        self.assertTrue(self.board.turnValid(self.board.grid, currPos, endPos3, color)) 

    def testKnight(self):
        self.board = cb.chessBoard()
        currPos = []
        currPos.append(1)                 # (1,1)
        currPos.append(1)
        pieceType = 2                     # Knight
        color = "Black"
        self.board.grid[currPos[0]][currPos[1]] = pieceType

        endPos1 = []                      # (7,7) : False
        endPos1.append(7)
        endPos1.append(7)

        endPos2 = []                      # (2,1) : False
        endPos2.append(1)
        endPos2.append(2)

        endPos3 = []                      # (3,2) : True
        endPos3.append(2)
        endPos3.append(3)


        self.assertFalse(self.board.turnValid(self.board.grid, currPos, endPos1, color))
        self.assertFalse(self.board.turnValid(self.board.grid, currPos, endPos2, color))
        self.assertTrue(self.board.turnValid(self.board.grid, currPos, endPos3, color))


    def testBishop(self):
        self.board = cb.chessBoard()
        currPos = []
        currPos.append(1)                 # (1,1)
        currPos.append(1)
        pieceType = 3                     # Bishop
        color = "Black"
        self.board.grid[currPos[0]][currPos[1]] = pieceType

        endPos1 = []                      # (1,2) : False
        endPos1.append(1)
        endPos1.append(2)

        endPos2 = []                      # (4,5) : False
        endPos2.append(4)
        endPos2.append(5)

        endPos3 = []                      # (3,3) : True
        endPos3.append(3)
        endPos3.append(3)


        self.assertFalse(self.board.turnValid(self.board.grid, currPos, endPos1, color))
        self.assertFalse(self.board.turnValid(self.board.grid, currPos, endPos2, color))
        self.assertTrue(self.board.turnValid(self.board.grid, currPos, endPos3, color)) 

    def testRook(self):
        self.board = cb.chessBoard()
        currPos = []
        currPos.append(1)                 # (1,1)
        currPos.append(1)
        pieceType = 4                     # Rook
        color = "Black"
        self.board.grid[currPos[0]][currPos[1]] = pieceType

        endPos1 = []                      # (2,5) : False
        endPos1.append(2)
        endPos1.append(5)

        endPos2 = []                      # (7,2) : False
        endPos2.append(7)
        endPos2.append(2)

        endPos3 = []                      # (5,1) : True
        endPos3.append(5)
        endPos3.append(1)


        self.assertFalse(self.board.turnValid(self.board.grid, currPos, endPos1, color))
        self.assertFalse(self.board.turnValid(self.board.grid, currPos, endPos2, color))
        self.assertTrue(self.board.turnValid(self.board.grid, currPos, endPos3, color)) 

    def testQueen(self):
        self.board = cb.chessBoard()
        currPos = []
        currPos.append(1)                 # (1,1)
        currPos.append(1)
        pieceType = 5                     # Queen
        color = "Black"
        self.board.grid[currPos[0]][currPos[1]] = pieceType

        endPos1 = []                      # (2,5) : False
        endPos1.append(2)
        endPos1.append(5)

        endPos2 = []                      # (7,2) : False
        endPos2.append(7)
        endPos2.append(2)

        endPos3 = []                      # (1,2) : True
        endPos3.append(2)
        endPos3.append(1)


        self.assertFalse(self.board.turnValid(self.board.grid, currPos, endPos1, color))
        self.assertFalse(self.board.turnValid(self.board.grid, currPos, endPos2, color))
        self.assertTrue(self.board.turnValid(self.board.grid, currPos, endPos3, color)) 

    def testKing(self):
        self.board = cb.chessBoard()
        currPos = []
        currPos.append(1)                 # (1,1)
        currPos.append(1)
        pieceType = 0                     # King
        color = "Black"
        self.board.grid[currPos[0]][currPos[1]] = pieceType

        endPos1 = []                      # (2,5) : False
        endPos1.append(2)
        endPos1.append(5)

        endPos2 = []                      # (7,2) : False
        endPos2.append(7)
        endPos2.append(2)

        endPos3 = []                      # (2,1) : True
        endPos3.append(1)
        endPos3.append(1)


        self.assertFalse(self.board.turnValid(self.board.grid, currPos, endPos1, color))
        self.assertFalse(self.board.turnValid(self.board.grid, currPos, endPos2, color))
        self.assertFalse(self.board.turnValid(self.board.grid, currPos, endPos3, color)) 



if __name__ == '__main__':
  unittest.main()
