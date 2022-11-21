from random import randrange

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print("""
+-------+-------+-------+
|       |       |       |""")
    print("|   ", board[0], "   |   ", board[1], "   |   ", board[2], "   |", sep="", end="")
    print("""
|       |       |       |
+-------+-------+-------+
|       |       |       |""")
    print("|   ", board[3], "   |   ", board[4], "   |   ", board[5], "   |", sep="", end="")
    print("""
|       |       |       |
+-------+-------+-------+
|       |       |       |""")
    print("|   ", board[6], "   |   ", board[7], "   |   ", board[8], "   |", sep="", end="")
    print("""
|       |       |       |
+-------+-------+-------+""")

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    make_list_of_free_fields(board)
    
    new_move = int(input("Enter your move: "))
    if new_move not in list_of_free_fields or new_move < 1 or new_move >9:
        print("That field is not available, try again.")
        enter_move(board)
    else:
        board[new_move-1] = "O"
    
    display_board(board)
    draw_move(board)
        

list_of_free_fields = []
def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    list_of_free_fields.clear()
    for field in board:
        if field != "X" and field != "O":
            list_of_free_fields.append(field)
    if list_of_free_fields == []:
        print("It's a tie")
        exit()
    print(list_of_free_fields)
    victory_for(board)

def victory_for(board):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    for i in range(0, 7, 3):
        if board[i] == board[i+1] == board[i+2]:
            print(board[i], " wins")
            exit()
    for i in range(3):
        if board[i] == board[i+3] == board[i+6]:
            print(board[i], " wins")
            exit()
    if board[0] == board[4] == board[8] or board[2] == board[4] == board[6]:
        print(board[4], " wins")
        exit()
        

def draw_move(board):
    # The function draws the computer's move and updates the board.
    make_list_of_free_fields(board)
    
    shot = randrange(9)
    if shot in list_of_free_fields:
        board[shot - 1] = "X"
    else: draw_move(board)
    display_board(board)
    enter_move(board)
    

board = [i for i in range(1,10)]
board[4] = "X"

display_board(board)
enter_move(board)
