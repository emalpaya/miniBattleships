# Copyright (C) Eva Malpaya
# #################################################################################################################### 
# Eva Malpaya
# CS 372, Oregon State University
# Programming Project 4
# August 7, 2022
# #################################################################################################################### 

from board import *
from input_validator import *

class Player():
    
    def __init__(self):
        self.myBoard = Board()
        self.enemyBoard = Board()

    ### Getters ###
    def getMyBoard(self):
        return self.myBoard

    def getEnemyBoard(self):
        return self.enemyBoard

    ### Board Interactors ###

    def initMyBoard(self):
        print("!!!\r\nLet's set up your board!")
        maxShips = self.getMyBoard().getMaxShips()

        while len(self.getMyBoard().getMyShips()) < maxShips:
            print("\r\n!!!\r\nYour board:")
            self.getMyBoard().printBoard()  
            currentShipCount = len(self.getMyBoard().getMyShips()) + 1
            print('!!!\r\nPlacing ship ' + str(currentShipCount) + ' of ' + str(maxShips) +'...')     

            rowPromptMsg = 'Enter ROW number #'
            getRow = Input_validator(1, self.getMyBoard().getBoardDimension(), rowPromptMsg)
            row = getRow.getInput()
            if row.upper() == 'QUIT':
                return row

            colPromptMsg = 'Enter COLUMN number #'
            getCol = Input_validator(1, self.getMyBoard().getBoardDimension(), colPromptMsg)
            col = getCol.getInput()
            if col.upper() == 'QUIT':
                return col

            if [int(row), int(col)] in self.getMyBoard().getMyShips(): # spot already chosen
                print("\r\n!!!\r\nOops! You've already placed a ship there. Try again.")
            else: # Add ship to my board
                self.getMyBoard().addMyShips(int(row), int(col))

        self.getMyBoard().printBoard()  
        return "Done!\r\n"

    def displayBothBoards(self):  
        print('--- YOUR BOARD ---')
        print('Ships remaining: ' + str(len(self.getMyBoard().getMyShips())))
        self.getMyBoard().printBoard()

        print("--- OPPONENT'S BOARD ---")
        sunkenEnemy = len(self.getEnemyBoard().getMySunken())
        maxShips = self.getEnemyBoard().getMaxShips()
        print('Ships remaining: ' + str(maxShips - sunkenEnemy))
        self.getEnemyBoard().printBoard()
   