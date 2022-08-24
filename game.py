# Copyright (C) Eva Malpaya
# #################################################################################################################### 
# Eva Malpaya
# CS 372, Oregon State University
# Programming Project 4
# August 7, 2022
# #################################################################################################################### 

from re import S
from player import *
from input_validator import *

class Game():

    def __init__(self):
        self.player = Player()
        self.roundCount = 0

    def getPlayer(self):
        return self.player

    def getRoundCount(self):
        return self.roundCount

    def setRoundCount(self, newRound):
        self.roundCount = newRound

    ### Status Checkers ###

    def checkMyWin(self): # Win status : Found all enemy ships
        sunkenEnemyShips = len(self.getPlayer().getEnemyBoard().getMySunken())
        maxShips = self.getPlayer().getMyBoard().getMaxShips()
        return sunkenEnemyShips == maxShips

    def checkEnemyWin(self): # Lose status : Enemy sunk all my ships 
        mySunken =  len(self.getPlayer().getMyBoard().getMySunken())
        maxShips = self.getPlayer().getMyBoard().getMaxShips()
        return mySunken == maxShips

    def isGameInPlay(self):
        if self.checkMyWin():
            self.displayEndingBoards()
            print("!!!\r\nThe game is over!!!!")
            print("You've sunken all of your opponent's battleships!")
            print("Congratulations!")
            return False
        elif self.checkEnemyWin():
            self.displayEndingBoards()
            print("!!!\r\nThe game is over!!!!")
            print("Your opponent has sunken all of your battleships!")
            print("Better luck next time!")    
            return False
        else:
            return True   

    ### Print game-related info ###

    def displayRules(self):
        print("\r\n!!!\r\n--- RULES ---")
        print("\r\nTo win, you must find and sink all of your opponent's remaining ships")
        print("before they find and sink all of yours.")
        print("\r\nThe boards are 5x5 spaces, and each ship occupies ONE 1x1 space.")
        print("\r\nLet the game begin!\r\n")    

    def displayRoundHeader(self):
        print(' ---------------------------')
        print(' -------- ROUND ' + str(self.getRoundCount()) + ' ---------')
        print(' ---------------------------\r\n')
        self.getPlayer().displayBothBoards()            

    def displayEndingBoards(self):
        print(' ---------------------------')
        print(' -------- GAME OVER --------')
        print(' ---------------------------\r\n')
        print("Total Rounds: " + str(self.getRoundCount()) + "\r\n")
        self.getPlayer().displayBothBoards()

    ### User Interactors ###        

    def getMyGuess(self):
        self.displayRoundHeader()
        print("!!!\r\nWhat space on your opponent's board would you like to guess?")   

        rowPromptMsg = 'Enter ROW number #'
        getRow = Input_validator(1, self.getPlayer().getMyBoard().getBoardDimension(), rowPromptMsg)
        row = getRow.getInput()
        if row.upper() == 'QUIT':
            return row

        colPromptMsg = 'Enter COLUMN number #'
        getCol = Input_validator(1, self.getPlayer().getMyBoard().getBoardDimension(), colPromptMsg)
        col = getCol.getInput()
        if col.upper() == 'QUIT':
            return col

        return row + ',' + col # Pack Guesses

    def processEnemysGuess(self, enemyGuess):
        unpackGuess = enemyGuess.split(',')
        guessRow = unpackGuess[0]
        guessCol = unpackGuess[1]

        if [int(guessRow), int(guessCol)] in self.getPlayer().getMyBoard().getMyShips():
            print("!!!\r\nIt's a hit! They've sunken one of your battleships!")
            self.getPlayer().getMyBoard().addMySunken(int(guessRow), int(guessCol))
            self.getPlayer().getMyBoard().removeMyShips(int(guessRow), int(guessCol))
            return "!!!\r\nIt's a hit! You've sunken one of their battleships!\r\n"
        else:
            print("!!!\r\nIt's a miss! Remaining ships are intact for now...")
            self.getPlayer().getMyBoard().addWrongGuesses(int(guessRow), int(guessCol))
            return "!!!\r\nIt's a miss! Their remaining ships are intact for now...\r\n"

    def processEnemyResponseToMyGuess(self, myGuess, enemyResponse):
        unpackGuess = myGuess.split(',')
        guessRow = unpackGuess[0]
        guessCol = unpackGuess[1]

        if enemyResponse == "!!!\r\nIt's a hit! You've sunken one of their battleships!\r\n":
            self.getPlayer().getEnemyBoard().addMySunken(int(guessRow), int(guessCol))
        elif enemyResponse == "!!!\r\nIt's a miss! Their remaining ships are intact for now...\r\n":
            self.getPlayer().getEnemyBoard().addWrongGuesses(int(guessRow), int(guessCol))

        self.getPlayer().displayBothBoards()  

    def getContinue(self):  
        print("!!!\r\nWould you like to keep playing?")   
        while True:
            print("Type 'continue' to continue (without quotes)")
            print("Type 'quit' to quit (without quotes)")
            userInput = input ( '>')

            if (userInput.upper() == 'CONTINUE'):
                return userInput  
            elif (userInput.upper() == 'QUIT'):
                return userInput  
            else:
                print('!!!\r\nOops! Invalid choice selected. Please try again.')              