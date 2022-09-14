#file that deals with the input sequuence 
	#asks to select a piece from the board with letters and numbers ex : D4
	# then prompts to where 
from pieces import pawn,rook,queen,king,knight,bishop
def input_sequence(board):
	selecting=True
	row=None
	column=None
	while selecting:
		selected =input("Which piece do you want to select?(Column(A-H),Row(1-8))").lower() 
		selected_column=selected[0]
		selected_row=int(selected[-1])
		if selected_column=='a':
			selected_column=0
		elif selected_column=='b':
			selected_column=1
		elif selected_column=='c':
			selected_column=2
		elif selected_column=='d':
			selected_column=3
		elif selected_column=='e':
			selected_column=4
		elif selected_column=='f':
			selected_column=5
		elif selected_column=='g':
			selected_column=6
		elif selected_column=='h':
			selected_column=7
		else:
			print("Invalid Column Input.")
			continue
		if selected_row-1>-1 and selected_row-1<9:
			if board[selected_row-1][selected_column]!=None:
				row=selected_row-1
				column=selected_column
				selecting=False
			else:print("No piece is here.")
		else:print("Invalid Row Input.")

	selecting=True
	while selecting:
		selected =input("Where do you want to move the piece to?(Column(A-H),Row(1-8))").lower() 
		selected_column=selected[0]
		selected_row=int(selected[-1])
		if selected_column=='a':
			selected_column=0
		elif selected_column=='b':
			selected_column=1
		elif selected_column=='c':
			selected_column=2
		elif selected_column=='d':
			selected_column=3
		elif selected_column=='e':
			selected_column=4
		elif selected_column=='f':
			selected_column=5
		elif selected_column=='g':
			selected_column=6
		elif selected_column=='h':
			selected_column=7
		else:
			print("Invalid Column Input.")
			continue
		if selected_row-1>-1 and selected_row<9:
			if board[row][column].valid_move(column,row,selected_column,selected_row-1,board):
				piece=board[row][column]
				board[selected_row-1][selected_column]=piece
				board[row][column]=None
				selecting=False
			else:print("Invalid Move")
		else:print("Invalid Row Input.")