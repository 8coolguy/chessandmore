#file that deals with the input sequuence 
	#asks to select a piece from the board with letters and numbers ex : D4
	# then prompts to where 
from pieces import pawn,rook,queen,king,knight,bishop
def input_sequence(board,turn):
	print(turn)
	selecting=True
	row=None
	column=None
	while selecting:
		selected =input("Which piece do you want to select?(Column(A-H),Row(1-8))(include comma)").lower().strip()
		selected=selected.split(",")
		selected_column=ord(selected[0].strip())-97
		selected_row=int(selected[-1].strip())
		selected_row = 8- selected_row
		
		if selected_column >7 or selected_column < 0 or selected_row <0 or selected_row>7:
			print("Invalid Input.")
			continue
		print([selected_row,selected_column])
		#selected row in arr format [0-7]
		if board[selected_row][selected_column]!=None and board[selected_row][selected_column].valid_turn(turn):
			column=selected_column
			row=selected_row
			selecting=False
		else:
			print("No piece is here or wrong piece.")
			continue

	selecting=True
	while selecting:
		selected =input("Where do you want to move the piece to?(Column(A-H),Row(1-8))(include comma)").lower().strip() 

		selected=selected.split(",")
		selected_column=ord(selected[0].strip())-97
		selected_row=int(selected[-1].strip())
		selected_row = 8- selected_row

		
		if selected_column >7 or selected_column < 0 or selected_row <0 or selected_row>7:
			print("Invalid Input.")
			continue
		print([selected_row,selected_column])
		#selected row in arr format [0-7]
		if board[row][column].valid_move(column,row,selected_column,selected_row,board):
			piece=board[row][column]
			board[selected_row][selected_column]=piece
			board[row][column]=None
			selecting=False
		else:
			print("Invalid Move")
			continue