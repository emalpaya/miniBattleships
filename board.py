# Copyright (C) Eva Malpaya
# #################################################################################################################### 
# Eva Malpaya
# CS 372, Oregon State University
# Programming Project 4
# August 7, 2022
# #################################################################################################################### 

from ipaddress import collapse_addresses

# Board visual for reference:
# columns->  1   2   3   4   5
#          ---------------------
# row: 1   | O | - |   |   |   |
#          ---------------------
# row: 2   |   |   |   | X |   |
#          ---------------------
# row: 3   |   | - |   |   |   |
#          ---------------------
# row: 4   |   | O |   |   | - |
#          ---------------------
# row: 5   |   |   |   |   | - |
#          ---------------------
# Key:
#    O Unsunken ships
#    X Sunken ships
#    - Wrong guesses

class Board():
    BOARD_DIMENSION = 5
    MAX_SHIPS = 3
    UNSUNKEN_CHAR = 'O'
    SUNKEN_CHAR = 'X'
    WRONG_GUESS_CHAR = '-'

    def __init__(self):
        # dicts holding key-value pairs where key is row # and value is col #
        self.myShips = [] # Key symbol when displaying board: O
        self.mySunken = [] # Key symbol when displaying board: X
        self.wrongGuesses = [] # Key symbol when displaying board: -

    # Board getters 
    
    # My Ships - getter, add, remove
    def getMyShips(self):
        return self.myShips
    def addMyShips(self, row, col):
        self.myShips.append([int(row), int(col)])
    def removeMyShips(self, row, col):
        self.myShips.remove([int(row), int(col)]) 

    # My Sunken - getter, add, remove
    def getMySunken(self):
        return self.mySunken 
    def addMySunken(self, row, col):
        self.mySunken.append([int(row), int(col)])
    def removeMySunken(self, row, col):
        self.mySunken.remove([int(row), int(col)])   

    # Wrong Guesses - getter, add, remove
    def getWrongGuesses(self):
        return self.wrongGuesses    
    def addWrongGuesses(self, row, col):
        self.wrongGuesses.append([int(row), int(col)])
    def removeWrongGuesses(self, row, col):
        self.wrongGuesses.remove([int(row), int(col)])             

    # Board piece getters

    def getBoardDimension(self):
        return self.BOARD_DIMENSION

    def getMaxShips(self):
        return self.MAX_SHIPS

    def displayShipsRemaining(self):    
        shipsRemaining = len(self.myShips)
        print("Ships remaining: " + shipsRemaining)
        
    # Board printer

    def printBoard(self):
        inMyShips = False
        inMySunken = False
        inWrongGuesses = False

        # Board header
        print("columns->  1   2   3   4   5")
        print("         ---------------------")

        # Board rows
        for i in range(1, self.BOARD_DIMENSION + 1): 
            print("row: " + str(i) + "   |", end="")

            # Board columns
            for j in range(1, self.getBoardDimension() + 1): 
                print(" ", end="")

                tempRow = i
                tempCol = j

                # Obtain what key symbol to print per space
                inMyShips = [int(tempRow), int(tempCol)] in self.getMyShips()
                inMySunken = [int(tempRow), int(tempCol)] in self.getMySunken()
                inWrongGuesses = [int(tempRow), int(tempCol)] in self.getWrongGuesses()

                if inMyShips:
                    print(self.UNSUNKEN_CHAR, end="")
                elif inMySunken:
                    print(self.SUNKEN_CHAR, end="")
                elif inWrongGuesses:
                    print(self.WRONG_GUESS_CHAR, end="")
                else: # empty spot on board
                    print(" ", end="")

                print(" |", end="")

            print("")
            print("         ---------------------")

        # Display key symbols beneath each board
        print("Key:")
        print("   " + self.UNSUNKEN_CHAR + " Unsunken ships")
        print("   " + self.SUNKEN_CHAR + " Sunken ships")
        print("   " + self.WRONG_GUESS_CHAR + " Wrong guesses\r\n")
