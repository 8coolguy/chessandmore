from abc import abstractmethod,ABC

#the class of all the pieces 
class piece(ABC):
	def __init__(self,color):
		self.color =color
		self.title =" "
	@abstractmethod
	def valid_move(self,xi,yi,xf,yf,board):
		pass

	def __str__(self):
		return "{}_{}".format(self.color,self.title)
#for the valid move the x is across the alphabet and the y is across the numbers
class pawn(piece):
	def __init__(self,color):
		super().__init__(color)
		self.title ="pawn"
	
	def valid_move(self,xi,yi,xf,yf,board):
		if self.color=='black':
			if (xi==xf and ((yi+1 ==yf) or (yi==1 and yi+2==yf))):
				if board[yf][xf]==None or board[yf][xf].color!='black':
					return True
			return False
		else:#white
			if (xi==xf and ((yi-1 ==yf) or (yi==6 and yi-2==yf))):
				print(board[yf][xf])
				if board[yf][xf]==None or board[yf][xf].color!='white':
					return True
			return False


class bishop(piece):
	def __init__(self,color):
		super().__init__(color)
		self.title ="bishop"

	def valid_move(self,xi,yi,xf,yf,board):
		pass

class rook(piece):
	def __init__(self,color):
		super().__init__(color)
		self.title ="rook"

	def valid_move(self,xi,yi,xf,yf,board):
		pass

class knight(piece):
	def __init__(self,color):
		super().__init__(color)
		self.title ="knight"
	def valid_move(self,xi,yi,xf,yf,board):
		pass

class queen(piece):
	def __init__(self,color):
		super().__init__(color)
		self.title ="queen"
	def valid_move(self,xi,yi,xf,yf,board):
		pass

class king(piece):
	def __init__(self,color):
		super().__init__(color)
		self.title ="king"
	def valid_move(self,xi,yi,xf,yf,board):
		pass
