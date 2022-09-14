from pieces import pawn,rook,queen,king,knight,bishop
from inputs import input_sequence
def display_board(board):
	alpha=['  a  ','  b  ','  c  ','  d  ','  e  ','  f  ','  g  ','  h  ']
	display_board=[[None,None,None,None,None,None,None,None] for _ in range(8)]	
	for row in range(8):
		for piece in range(8):
			display_board[row][piece]=str(board[row][piece])
	res="  "
	for i in alpha:
		res+=i.center(23)
	print(res)
	for row in range(8):
		res="|"
		for e in display_board[row]:
			res+=str(" "+str(e).center(20)+" |")
		print(str(8-row)+" "+res) 
		print("-"*23*8+3*"-")
def place_board(board):
	#pawns
	for piece in range(8):
		board[1][piece]=pawn("black")
		board[-2][piece]=pawn("white")
	#rooks
	board[0][0]=board[0][-1]=rook("black")
	board[-1][0]=board[-1][-1]=rook("white")
	#knights
	board[0][1]=board[0][-2]=knight("black")
	board[-1][1]=board[-1][-2]=knight("white")
	#bishops
	board[0][2]=board[0][-3]=bishop("black")
	board[-1][2]=board[-1][-3]=bishop("white")
	#queens
	board[0][3]=queen("black")
	board[-1][3]=queen("white")
	#white
	board[0][4]=king("black")
	board[-1][4]=king("white")
if __name__ =="__main__":
	board =[[None,None,None,None,None,None,None,None] for _ in range(8)]	
	place_board(board)
	display_board(board)
	i=0
	while True:
		if(i%2==0):
			print("Player 1 White Moves.")
		else:
			print("Player 2 Black Moves.")
		input_sequence(board,i%2)
	
		display_board(board)
		i+=1


