import math
import copy

class chessBoard:
	pieces = [('Empty','No Color'),('Pawn','Black'),
			('Knight','Black'),('Bishop','Black'),('Rook','Black'),('Queen','Black'),('King','Black'),
			('Pawn','White'),('Knight','White'),('Bishop','White'),('Rook','White'),('Queen','White'),
			('King','White')]
	
	grid = [0]*8
	for i in range(len(grid)):
		grid[i]=[0]*8
	viableSpaces = []
	
	
	def __init__(self):
		self.grid[1] = [1]*8; self.grid[6]=[7]*8
		self.grid[0][0] = 4; self.grid[0][1] = 2; self.grid[0][2] = 3; self.grid[0][3] = 5;
		self.grid[0][4] = 6; self.grid[0][5] = 3; self.grid[0][6] = 2; self.grid[0][7] = 4;
		self.grid[7][0] = 10; self.grid[7][1] = 8; self.grid[7][2] = 9; self.grid[7][3] = 11;
		self.grid[7][4] = 12; self.grid[7][5] = 9; self.grid[7][6] = 8; self.grid[7][7] = 10;
		
	def moveValid(self, grid, curPos, endPos):
		ID = grid[curPos[0]][curPos[1]]%6
		currPieceColor = self.pieces[grid[curPos[0]][curPos[1]]][1]
		endPieceColor = self.pieces[grid[endPos[0]][endPos[1]]][1]
		endPoint = grid[endPos[0]][endPos[1]]

		# Pawn rules
		if ID == 1:
			if currPieceColor == 'Black':
				if endPoint == 0 and [curPos[0]+1,curPos[1]] == [endPos[0],endPos[1]]:
					return True
				#Black: Moving two spaces foward
				elif curPos[0] == 1 and [curPos[0]+2,curPos[1]] == [endPos[0],endPos[1]] and grid[curPos[0]+1][curPos[1]] == 0 and endPoint == 0:
					return True
				#Black: Attacking
				elif endPoint != 0 and ([curPos[0]+1,curPos[1]-1] == [endPos[0],endPos[1]] or [curPos[0]+1,curPos[1]+1] == [endPos[0],endPos[1]]) and endPieceColor == 'White':
					return True
			else:
				if endPoint == 0 and [curPos[0]-1,curPos[1]] == [endPos[0],endPos[1]]:
					return True
				#White: Moving two spaces foward
				elif curPos[0] == 6 and [curPos[0]-2,curPos[1]] == [endPos[0],endPos[1]] and grid[curPos[0]-1][curPos[1]] == 0 and endPoint == 0:
					return True
				#White: Attacking
				elif endPoint != 0 and ([curPos[0]-1,curPos[1]-1] == [endPos[0],endPos[1]] or [curPos[0]-1,curPos[1]+1] == [endPos[0],endPos[1]]) and endPieceColor == 'Black':
					return True
		
		#Knight rules
		elif ID == 2:
			distance = math.sqrt((endPos[0]-curPos[0])**2 + (endPos[1]-curPos[1])**2)
			if endPoint == 0 and distance == math.sqrt(5):
				return True
			#Black: Attacking
			elif endPoint != 0 and distance == math.sqrt(2) and currPieceColor == 'Black' and endPieceColor == 'White':
				return True
			#White: Attacking
			elif endPoint != 0 and distance == math.sqrt(2) and currPieceColor == 'White' and endPieceColor == 'Black':
				return True

		# Bishop, Queen or Rook rules  
		elif ID == 3 or ID == 4 or ID == 5:
			if currPieceColor == 'Black':
				color = 'White'
			elif currPieceColor == 'White':
				color = 'Black'
			else:
				color = 'No Color'
			
			allowedSpaces = self.detViableSpaces(ID, grid, curPos, color)
			if endPos in allowedSpaces:
				return True

		#King rules 
		elif ID == 0:
			if grid[curPos[0]][curPos[1]] != 0:
				distance = math.sqrt((endPos[0]-curPos[0])**2 + (endPos[1]-curPos[1])**2)
				if endPoint == 0 and distance < 1.5:
					return True
				#Black: Attacking
				elif endPoint != 0 and distance < 1.5 and currPieceColor == 'Black' and endPieceColor == 'White':
					return True
				#White: Attacking
				elif endPoint != 0 and distance < 1.5 and currPieceColor == 'White' and endPieceColor == 'Black':
					return True
		return False
		
	def detViableSpaces(self, pieceID, grid, curPos, color):
		self.viableSpaces = []
		if pieceID == 5:												# Queen
			for i in range(4):
				self.detViableHorizVertSpaces(grid, curPos, i, color)
				self.detViableDiagSpaces(grid, curPos, i, color)
		elif pieceID == 4:												# Rook
			for i in range(4):
				self.detViableHorizVertSpaces(grid,curPos,i,color)
		elif pieceID == 3:												# Bishop
			for i in range(4):
				self.detViableDiagSpaces(grid,curPos,i,color)
		
		return self.viableSpaces

	def detViableDiagSpaces(self,grid,curPos,i,color):
		if i == 0:
			try:
				if grid[curPos[0]+1][curPos[1]+1] != 0 and self.pieces[grid[curPos[0]+1][curPos[1]+1]][1] != color:
					pass
				else:
					newPos = [curPos[0]+1,curPos[1]+1]
					if newPos[0] >= 0 and newPos[1] >= 0:
						self.viableSpaces.append(newPos)
						if self.pieces[grid[newPos[0]][newPos[1]]][1] != color:
							self.detViableDiagSpaces(grid,newPos,i,color)
			except:
				pass
		elif i == 1:
			try:
				if grid[curPos[0]+1][curPos[1]-1] != 0 and self.pieces[grid[curPos[0]+1][curPos[1]-1]][1] != color:
					pass
				else:
					newPos = [curPos[0]+1,curPos[1]-1]
					if newPos[0] >= 0 and newPos[1] >= 0:
						self.viableSpaces.append(newPos)
						if self.pieces[grid[newPos[0]][newPos[1]]][1] != color:
							self.detViableDiagSpaces(grid,newPos,i,color)
			except:
				pass
		elif i == 2:
			try:
				if grid[curPos[0]-1][curPos[1]+1] != 0 and self.pieces[grid[curPos[0]-1][curPos[1]+1]][1] != color:
					pass
				else:
					newPos = [curPos[0]-1,curPos[1]+1]
					if newPos[0] >= 0 and newPos[1] >= 0:
						self.viableSpaces.append(newPos)
						if self.pieces[grid[newPos[0]][newPos[1]]][1] != color:
							self.detViableDiagSpaces(grid,newPos,i,color)
			except:
				pass
		else:
			try:
				if grid[curPos[0]-1][curPos[1]-1] != 0 and self.pieces[grid[curPos[0]-1][curPos[1]-1]][1] != color:
					pass
				else:
					newPos = [curPos[0]-1,curPos[1]-1]
					if newPos[0] >= 0 and newPos[1] >= 0:
						self.viableSpaces.append(newPos)
						if self.pieces[grid[newPos[0]][newPos[1]]][1] != color:
							self.detViableDiagSpaces(grid,newPos,i,color)
			except:
				pass

	def detViableHorizVertSpaces(self,grid,curPos,i,color):
			if i == 0:
				try:
					if grid[curPos[0]+1][curPos[1]] != 0 and self.pieces[grid[curPos[0]+1][curPos[1]]][1] != color:
						pass
					else:
						newPos = [curPos[0]+1,curPos[1]]
						if newPos[0] >= 0 and newPos[1] >= 0:
							self.viableSpaces.append(newPos)
							if self.pieces[grid[newPos[0]][newPos[1]]][1] != color:
								self.detViableHorizVertSpaces(grid,newPos,i,color)
				except:
					pass
			elif i == 1:
				try:
					if grid[curPos[0]-1][curPos[1]] != 0 and self.pieces[grid[curPos[0]-1][curPos[1]]][1] != color:
						pass
					else:
						newPos = [curPos[0]-1,curPos[1]]
						if newPos[0] >= 0 and newPos[1] >= 0:
							self.viableSpaces.append(newPos)
							if self.pieces[grid[newPos[0]][newPos[1]]][1] != color:
								self.detViableHorizVertSpaces(grid,newPos,i,color)
				except:
					pass
			elif i == 2:
				try:
					if grid[curPos[0]][curPos[1]+1] != 0 and self.pieces[grid[curPos[0]][curPos[1]+1]][1] != color:
						pass
					else:
						newPos = [curPos[0],curPos[1]+1]
						if newPos[0] >= 0 and newPos[1] >= 0:
							self.viableSpaces.append(newPos)
							if self.pieces[grid[newPos[0]][newPos[1]]][1] != color:
								self.detViableHorizVertSpaces(grid,newPos,i,color)
				except:
					pass
			else:
				try:
					if grid[curPos[0]][curPos[1]-1] != 0 and self.pieces[grid[curPos[0]][curPos[1]-1]][1] != color:
						pass
					else:
						newPos = [curPos[0],curPos[1]-1]
						if newPos[0] >= 0 and newPos[1] >= 0:
							self.viableSpaces.append(newPos)
							if self.pieces[grid[newPos[0]][newPos[1]]][1] != color:
								self.detViableHorizVertSpaces(grid,newPos,i,color)
				except:
					pass
					
	def detPawnSpaces(self,grid,curPos,color):
		pawnSpaces = []
		if color == "Black":
			cVal = 1
			currVal = 1
			enemyColor = "White"
		else:
			cVal = -1
			currVal = 6
			enemyColor = "Black"

		if 0 <= curPos[0]+(1 * cVal) < 8 and grid[curPos[0]+(1*cVal)][curPos[1]] == 0:
			pawnSpaces.append([curPos[0]+(1*cVal),curPos[1]])
		if 0 <= curPos[0]+(2*cVal) < 8 and grid[curPos[0]+(2 * cVal)][curPos[1]] == 0 and curPos[0] == currVal and grid[curPos[0]+(1*cVal)][curPos[1]] == 0:
			pawnSpaces.append([curPos[0]+(2*cVal),curPos[1]])
		if 0 <= curPos[0]+(1*cVal) < 8 and 0 <= curPos[1]+1 < 8 and self.pieces[grid[curPos[0]+(1*cVal)][curPos[1]+1]][1] == enemyColor:
			pawnSpaces.append([curPos[0]+(1*cVal),curPos[1]+1])
		if 0 <= curPos[0]+(1*cVal) < 8 and 0 <= curPos[1]-1 < 8 and self.pieces[grid[curPos[0]+(1*cVal)][curPos[1]-1]][1] == enemyColor:
			pawnSpaces.append([curPos[0]+(1*cVal),curPos[1]-1])

		return pawnSpaces
			
	def detKnightSpaces(self,grid,curPos,color):
		return [[curPos[0]+2,curPos[1]+1],[curPos[0]+2,curPos[1]-1],[curPos[0]+1,curPos[1]+2],[curPos[0]+1,curPos[1]-2],[curPos[0]-1,curPos[1]+2],[curPos[0]-1,curPos[1]-2],[curPos[0]-2,curPos[1]+1],[curPos[0]-2,curPos[1]-1]]
		
	def detBishopSpaces(self,grid,curPos,color):
		self.viableSpaces = []
		for i in range(4):
			self.detViableDiagSpaces(grid,curPos,i,color)
		return self.viableSpaces
		
	def detRookSpaces(self,grid,curPos,color):
		self.viableSpaces = []
		for i in range(4):
			self.detViableHorizVertSpaces(grid,curPos,i,color)
		return self.viableSpaces
		
	def detQueenSpaces(self,grid,curPos,color):
		self.viableSpaces = []
		for i in range(4):
			self.detViableDiagSpaces(grid,curPos,i,color)
			self.detViableHorizVertSpaces(grid,curPos,i,color)
		return self.viableSpaces
		
	def detKingSpaces(self,grid,curPos,color):
		return [[curPos[0]+1,curPos[1]],[curPos[0],curPos[1]+1],[curPos[0]-1,curPos[1]],[curPos[0],curPos[1]-1],[curPos[0]+1,curPos[1]+1],[curPos[0]-1,curPos[1]+1],[curPos[0]+1,curPos[1]-1],[curPos[0]-1,curPos[1]-1]]
					
	def inCheck(self, grid, color):
		for r in range(len(grid)):
			for p in range(len(grid[r])):
				if grid[r][p] != 0 and grid[r][p]%6 == 0 and self.pieces[grid[r][p]][1] == color:
					kingPos = [r,p]
		for r in range(len(grid)):
			for p in range(len(grid[r])):
				if grid[r][p] != 0 and self.pieces[grid[r][p]][1] != color:
					if self.moveValid(grid,[r,p],kingPos):
						return True
		return False
	
	def turnValid(self,grid,curPos,endPos,color):
		valid = self.moveValid(grid,curPos,endPos)
		if valid:
			temp = copy.deepcopy(grid)
			temp[endPos[0]][endPos[1]] = temp[curPos[0]][curPos[1]]
			temp[curPos[0]][curPos[1]] = 0
			if not self.inCheck(temp,color):
				return True
		return False