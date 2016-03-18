#Skeleton Program for the AQA AS1 Summer 2016 examination
#this code should be used in conjunction with the Preliminary Material
#written by the AQA AS1 Programmer Team
#developed in a Python 3 programming environment

#Version Number 1.0

import random

def GetRowColumn():
  Column, Row = 11, 11

  while not -1 < Column < 10:
    while not -1 < Row < 10:
      Column = int(input("Please enter column: "))
      Row = int(input("Please enter row: "))

  return Row, Column
            
def MakePlayerMove(Board, Ships):
  Row, Column = GetRowColumn() #Gets the chosen row and column from the GetRowColumn function
  if Board[Row][Column] == "m" or Board[Row][Column] == "h": #If the square selected is has already been verified as a miss or hit then
    print("Sorry, you have already shot at the square (" + str(Column) + "," + str(Row) + "). Please try again.") #Tell the player this square has been shot already
  elif Board[Row][Column] == "-": #If the selected square has nothing in it then
    print("Sorry, (" + str(Column) + "," + str(Row) + ") is a miss.") #Tell the player this square is a miss
    Board[Row][Column] = "m" #Change that square to a miss
  else: #If the selected square is occupied by a ship then
    print("Hit at (" + str(Column) + "," + str(Row) + ").") #Tell the player this square is a hit
    Board[Row][Column] = "h" #Change that square to a hit
        
def SetUpBoard():
  Board = [] #Set up the board array
  for Row in range(10): #Loop around this code 10 times
    BoardRow = [] #Set up the board row array for each pass
    for Column in range(10): #Loop around this code for 10 times
      BoardRow.append("-") #Add a dash in all 10 available places in the board row
    Board.append(BoardRow) #Add the completed board row to the board array
  return Board #Return the completed board

def LoadGame(Filename, Board):
  BoardFile = open(Filename, "r") #Open the filename in read form
  for Row in range(10): #Loop around this code 10 times
    Line = BoardFile.readline() #Set the line variable to the current line in the file
    for Column in range(10): #Loop around this code 10 times
      Board[Row][Column] = Line[Column] #Sets the boats position on the board to the same as in the file
  BoardFile.close() #Close the file
    
def PlaceRandomShips(Board, Ships):
  for Ship in Ships: #For every ship in the ships 2D array
    Valid = False #Sets the variable valid to false
    while not Valid: #While the result is not valid
      Row = random.randint(0, 9) #Sets the Row variable to a random character between 0 and 9
      Column = random.randint(0, 9) #Sets the Column variable to a random character between 0 and 9
      HorV = random.randint(0, 1) #Sets the HorV variable to either 0 or 1
      if HorV == 0: #If the HorV variable is 0 then
        Orientation = "v" #Set the orientation of the ship to v
      else: #Otherwise
        Orientation = "h" #Set the orientation of the ship to h
      Valid = ValidateBoatPosition(Board, Ship, Row, Column, Orientation) #Validate the boats position on the board
    print("Computer placing the " + Ship[0]) #Tells the player what ship is currently being placed on the board
    PlaceShip(Board, Ship, Row, Column, Orientation) #Places the boat on the board

def PlaceShip(Board, Ship, Row, Column, Orientation):
  if Orientation == "v": #If the boats orientation is v then
    for Scan in range(Ship[1]): #Loop around this code the amount of times stated in the ships array
      Board[Row + Scan][Column] = Ship[0][0] #Places the ship vertically
  elif Orientation == "h": #If the boats orientation is h then
    for Scan in range(Ship[1]): #Loop around this code the amount of times stated in the ships array
      Board[Row][Column + Scan] = Ship[0][0] #Places the ship horizontally

def ValidateBoatPosition(Board, Ship, Row, Column, Orientation):
  if Orientation == "v" and Row + Ship[1] > 10:
    return False
  elif Orientation == "h" and Column + Ship[1] > 10:
    return False
  else:
    if Orientation == "v":
      for Scan in range(Ship[1]):
        if Board[Row + Scan][Column] != "-":
          return False
    elif Orientation == "h":
      for Scan in range(Ship[1]):
        if Board[Row][Column + Scan] != "-":
          return False
  return True

def CheckWin(Board):
  for Row in range(10):
    for Column in range(10):
      if Board[Row][Column] in ["A","B","S","D","P"]:
        return False
  return True
 
def PrintBoard(Board):
  print()
  print("The board looks like this: ")  
  print()
  print (" ", end="")
  for Column in range(10):
    print(" " + str(Column) + "  ", end="")
  print()
  for Row in range(10):
    print (str(Row) + " ", end="")
    for Column in range(10):
      if Board[Row][Column] == "-":
        print(" ", end="")
      elif Board[Row][Column] in ["A","B","S","D","P"]:
        print(" ", end="")                
      else:
        print(Board[Row][Column], end="")
      if Column != 9:
        print(" | ", end="")
    print()
       
def DisplayMenu():
  print("MAIN MENU")
  print()
  print("1. Start new game")
  print("2. Load training game")
  print("9. Quit")
  print()
    
def GetMainMenuChoice():
  print("Please enter your choice: ", end="")
  Choice = int(input())
  print()
  return Choice

def PlayGame(Board, Ships):
  GameWon = False
  while not GameWon:
    PrintBoard(Board)
    MakePlayerMove(Board, Ships)
    GameWon = CheckWin(Board)
    if GameWon:
      print("All ships sunk!")
      print()

if __name__ == "__main__":
  TRAININGGAME = "Training.txt"
  MenuOption = 0
  while not MenuOption == 9:
    Board = SetUpBoard()
    Ships = [["Aircraft Carrier", 5], ["Battleship", 4], ["Submarine", 3], ["Destroyer", 3], ["Patrol Boat", 2]]
    DisplayMenu()
    MenuOption = GetMainMenuChoice()
    if MenuOption == 1:
      PlaceRandomShips(Board, Ships)
      PlayGame(Board,Ships)
    if MenuOption == 2:
      LoadGame(TRAININGGAME, Board)
      PlayGame(Board, Ships)   