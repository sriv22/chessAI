import Tkinter as tk
from Tkinter import *
import chessBoard as cb
import chessAI as com
import itertools
	
class App:
	board = cb.chessBoard()                                                             ## Creates new chessBoard
	turnCount = 0                                                                       ## Global turn variable
	itemClicked = False                                                                 ## Determines if item is clicked/selected
	colors = ['White','Black']                                                          ## Set of colors
	missingPiecesBlack = []                                                             ## Array of missing black pieces
	missingPiecesWhite = []                                                             ## Array of missing white pieces
	
	def __init__(self,master):
          self.Master = master
          master.title("Chess")
          self.canvas = Canvas(self.Master)
          ## Creates pieces
          self.pieces = [tk.PhotoImage(file='images/SquareWhite.gif'), tk.PhotoImage(file='images/PawnBlack.gif'),tk.PhotoImage(file='images/KnightBlack.gif'), 
              tk.PhotoImage(file='images/BishopBlack.gif'), tk.PhotoImage(file='images/RookBlack.gif'), tk.PhotoImage(file='images/QueenBlack.gif'),
              tk.PhotoImage(file='images/KingBlack.gif'), tk.PhotoImage(file='images/PawnWhite.gif'), tk.PhotoImage(file='images/KnightWhite.gif'), 
              tk.PhotoImage(file='images/BishopWhite.gif'),tk.PhotoImage(file='images/RookWhite.gif'), tk.PhotoImage(file='images/QueenWhite.gif'), 
              tk.PhotoImage(file='images/KingWhite.gif')]

          ## Designates look of active pieces
          self.activePieces = [tk.PhotoImage(file='images/SquareWhite.gif'), tk.PhotoImage(file='images/PawnBlackAct.gif'),
              tk.PhotoImage(file='images/KnightBlackAct.gif'), tk.PhotoImage(file='images/BishopBlackAct.gif'), tk.PhotoImage(file='images/RookBlackAct.gif'),
              tk.PhotoImage(file='images/QueenBlackAct.gif'), tk.PhotoImage(file='images/KingBlackAct.gif'), tk.PhotoImage(file='images/PawnWhiteAct.gif'), 
              tk.PhotoImage(file='images/KnightWhiteAct.gif'), tk.PhotoImage(file='images/BishopWhiteAct.gif'),tk.PhotoImage(file='images/RookWhiteAct.gif'), 
              tk.PhotoImage(file='images/QueenWhiteAct.gif'), tk.PhotoImage(file='images/KingWhiteAct.gif')]
          
          ## Designates empty spots
          self.emptySpaces = [tk.PhotoImage(file='images/SquareWhite.gif'), tk.PhotoImage(file='images/SquareGrey.gif'),
              tk.PhotoImage(file='images/SquareActive.gif'), tk.PhotoImage(file='images/SquareClicked.gif')]
          
          self.frame = Frame(master)
          self.frame.grid()
          self.play = Label(self.frame, text = "Single player or two players?")
          self.play.grid(row=0, column =0, columnspan = 6)
          self.compGame = Button(self.frame, text = "Single Player", command = self.compGameSetup)            ## Designates computer game (inactive as of now)
          self.compGame.grid(row=1,column=0)                                                                  ## Inactive button
          self.multGame = Button(self.frame, text='Two Players', command=self.multGameSetUp)                  ## Designates multiplayer game and calls set up
          self.multGame.grid(row=1,column =1)
		
	def compGameSetup(self):
          self.comOp = True
          self.computer = com.chessCom()
          self.frame.destroy()
          self.startGame()
		
	def multGameSetUp(self):
          """
          Sets up intial state of game
          """
          self.comOp = False
          self.frame.destroy()
          self.startGame()
		
	def startGame(self):
          """
          Sets up game
          """
          self.Master.minsize(874,778)                                # Minimum width and height it could possibly be.
          self.canvas.config(height=778,width=874,bg = 'black')       # Configures width, height and background color
	  self.canvas.pack()
	  self.Master.update()
	  self.displayBoard()
		
	def displayBoard(self):
          """
          Display the board, including epty spots, active pieces and pieces
          """
          for i, j in itertools.product(range(8),range(8)):       ## Sets up empty spots
                      lW = 10 + 96*i
                      lH = 10 + 96*j
                      emptySpace = self.emptySpaces[(i+j)%2]
                      activeEmptySpace = self.emptySpaces[2]
                      self.canvas.create_image(lW,lH,image=self.emptySpaces[(i+j)%2],anchor=NW,activeimage = activeEmptySpace)
          
          for r, c in itertools.product(range(8), range(8)):     ## Sets up active pieces
                      lH = 10 + 96*r
                      lW = 10 + 96*c
                      if self.board.grid[r][c] != 0:
                              piece = self.pieces[self.board.grid[r][c]]
                              activeImage = self.activePieces[self.board.grid[r][c]]
                              self.canvas.create_image(lW,lH,image = piece, anchor=NW, activeimage = activeImage)
          for k in range(12):                       ## Creates empty spots near "dead" lane
                      lH = 10 + 61*k
                      self.canvas.create_image(779,lH,image=self.emptySpaces[0],anchor=NW)
          for l in range(len(self.missingPiecesBlack)):         ## Sets up black dead pieces
                      lH = 10 + 96*l
                      self.canvas.create_image(779,lH,image=self.pieces[self.missingPiecesBlack[l]],anchor=NW)
          for n in range(len(self.missingPiecesWhite)):         ## Sets up white dead pieces
                      lH = 394 + 96*n
                      self.canvas.create_image(779,lH,image=self.pieces[self.missingPiecesWhite[n]],anchor=NW)

          self.Master.update()

        def missingPieces (self, finPosPiece, color):
          """ Adds missing pieces"""
          """ getatttr(self.missingPieces{}.format(color)) """
          if (finPosPiece%6) > 0:
            if color == 'White':
              self.missingPiecesBlack.append(finPosPiece)
              if len(self.missingPiecesBlack) > 4:
                      self.missingPiecesBlack.remove(min(self.missingPiecesBlack))
            if color == 'Black':
              self.missingPiecesWhite.append(finPosPiece)
              if len(self.missingPiecesWhite) > 4:
                      self.missingPiecesWhite.remove(min(self.missingPiecesWhite))

        def pawnPromotion (self, finPosPiece, color, index):
          """ Promotes the pawn accordingly """
          if (finPosPiece == 1 and index == 7) or (finPosPiece == 7 and index == 0):
            if color == 'White' and len(self.missingPiecesWhite) > 0:
              finPosPiece = max(self.missingPiecesWhite)
              self.missingPiecesWhite.remove(max(self.missingPiecesWhite))
            elif color == "Black" and len(self.missingPiecesBlack) > 0:
                                finPosPiece = max(self.missingPiecesBlack)
                                self.missingPiecesBlack.remove(max(self.missingPiecesBlack))

	def callback(self,event):
          """
          Basic game loop that accounts for selected pieces and turn validation.
          """
          color = self.colors[self.turnCount%2]
          if self.itemClicked == False:
            for r, c in itertools.product(range(len(self.board.grid[0])), range(len(self.board.grid))):
              lH = 10 + 96*r
              lW = 10 + 96*c
              piece = self.board.grid[r][c]                               ## Piece Selected
              pieceColor = self.board.pieces[self.board.grid[r][c]][1]    ## Color of piece selected
              if event.x in range(lW,lW+90) and event.y in range(lH,lH+90) and piece != 0 and pieceColor == color:      ## Valid piece
                self.canvas.create_image(lW,lH,image=self.emptySpaces[3],anchor=NW)
                self.canvas.create_image(lW,lH,image=self.pieces[self.board.grid[r][c]],anchor=NW)
                self.itemClicked = True
                self.curPos = [r,c]
          else:
            for r, c in itertools.product(range(len(self.board.grid[0])), range(len(self.board.grid))):
              lH = 10 + 96*r
              lW = 10 + 96*c
              if event.x in range(lW,lW+90) and event.y in range(lH,lH+90):
                if r == self.curPos[0] and c == self.curPos[1]:
                        piece = self.pieces[self.board.grid[r][c]]
                        activePiece = self.activePieces[self.board.grid[r][c]]
                        self.canvas.create_image(lW,lH,image=self.emptySpaces[(r+c)%2],anchor=NW)
                        self.canvas.create_image(lW,lH,image=piece,anchor=NW,activeimage = activePiece)
                        self.itemClicked = False
                else:
                  self.finPos = [r,c]

                  if self.board.turnValid(self.board.grid,self.curPos,self.finPos,color):               ## Validates move
                    self.itemClicked = False
                    self.turnCount += 1
                    finPosPiece = self.board.grid[self.finPos[0]][self.finPos[1]]
                    #Add to missing pieces list
                    self.missingPieces (finPosPiece, color)

                    self.board.grid[self.finPos[0]][self.finPos[1]] = self.board.grid[self.curPos[0]][self.curPos[1]]
                    self.board.grid[self.curPos[0]][self.curPos[1]] = 0

                    #Pawn promotion
                    self.pawnPromotion (finPosPiece, color, r)

                    self.canvas.delete(ALL)
                    self.displayBoard()

                  if self.comOp == True and self.turnCount % 2 == 1:                                  ## Computer Move
                    color = self.colors[self.turnCount%2]
                    choice = self.computer.makeMove(self.board,color)
                    finPosPiece = self.board.grid[choice[2][0]][choice[2][1]]

                    #Add to missing pieces list
                    self.missingPieces(finPosPiece, color)

                    self.board.grid[choice[2][0]][choice[2][1]] = self.board.grid[choice[1][0]][choice[1][1]]
                    self.board.grid[choice[1][0]][choice[1][1]] = 0

                    #Pawn promotion
                    self.pawnPromotion (finPosPiece, color, r)

                    self.turnCount += 1
                    self.canvas.delete(ALL)
                    self.displayBoard()

          self.Master.update()
		
root = tk.Tk()
app = App(root)
app.canvas.bind("<Button-1>", app.callback)
root.mainloop()