## Imports

## Functions & Methods

# updateBoard method reflects all list changes into board
def updateBoard():
   global board, board_list

   board =f'''
   |      |   
 {board_list[0]} |  {board_list[1]}   | {board_list[2]} 
   |      |   
----------------
   |      |   
 {board_list[3]} |  {board_list[4]}   | {board_list[5]}
   |      |   
----------------
   |      |   
 {board_list[6]} |  {board_list[7]}   | {board_list[8]}
   |      |   
   '''

# TurnsLogic function handles turns logic and checks
def TurnsLogic(user_input, player):
   global board_list

   if board_list[int(user_input)-1] == "X" or board_list[int(user_input)-1] == "O":
      print(f"Sorry! Please Try Again! Which number you selected already have selected!")

   else:
      board_list[int(user_input)-1] = player
      updateBoard()
      print(f"\n{board}\n")


# Winner Function Check the boardList and Declares the Winner
def Winner(board_list, winnername, loosername):
   if board_list[0] == board_list[1] == board_list[2] or board_list[3] == board_list[4] == board_list[5] or board_list[6] == board_list[7] == board_list[8] or board_list[0] == board_list[3] == board_list[6] or board_list[1] == board_list[4] == board_list[7] or board_list[2] == board_list[5] == board_list[8] or board_list[0] == board_list[4] == board_list[8] or board_list[2] == board_list[4] == board_list[6]:
      print(f"Congrautulations! {winnername}, You defeated {loosername}!! & You are the Winner!")
      exit()
   
   # Code for Game Draw
   true_count = 1
   for i in range(9):
      if board_list[i] != i+1:
         true_count += 1
      else:
         true_count = 1
      
      if true_count == 9:
         print(f"Game Drawn! Well Played {winnername} & {loosername}, No one wins!")
         exit()

## Main Code
if __name__ == "__main__":
   
# Global Variables
   board_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

   # Creating Board structure
   board =f'''
   |      |   
 1 |  2   | 3 
   |      |   
----------------
   |      |   
 4 |  5   | 6
   |      |   
----------------
   |      |   
 7 |  8   | 9
   |      |   
   '''

   # Taking username inputs
   playerX = input("Enter the Name of Player X : ")
   playerO = input("Enter the Name of Player O : ")

   print(board)

   while True:
      # Taking User choices
      x_input = input(f"It's {playerX} Turn means X! Enter the number according to the board : ")
      TurnsLogic(x_input, player="X")
      Winner(board_list, playerX, playerO)

      o_input = input(f"It's {playerO} Turn means O! Enter the number according to the board : ")
      TurnsLogic(o_input, player="O")
      Winner(board_list, playerO, playerX)

