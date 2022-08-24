# Copyright (C) Eva Malpaya
# #################################################################################################################### 
# Eva Malpaya
# CS 372, Oregon State University
# Programming Project 4
# August 7, 2022
#
# Description:
#   EXTRA CREDIT VERSION.
#   This program utilizes a client socket connection to connect to a server-initialized multiplayer (2-player) 
#   ascii game of Mini Battleships, then plays the game.
#
#   The game cycles through different 'game phases' to follow the client socket connection flow of sending 
#   then receiving. It cycles through the 'Setup' phase once, then the remaining game phases until someone wins.
#
#   The game is considered "mini" battleships in the sense that the board size, ship count, and ship sizes have been 
#   scaled down from the typical Battleship game.
#
#   If this project were to be expanded upon further, I would update it to utilize the full standard board size, 
#   ship count, and ship sizes/shapes of a typical Battleship game.
#
# In: Port number of server program initializing the game.
#
# Out: None; console output only
#
# #################################################################################################################### 

# Citation for overall socket connection code:
# Date: 8/7/2022
# Adapted from:
# Kurose and Ross, Computer Networking: A Top-Down Approach, 8th Edition,Pearson, p. 205

from socket import *
from game import *
from input_validator import *
import sys

# Game Phases:
# These are the 4 main phases of the game.
# Client's socket flow here is send-then-receive.
# Message to send and Data to receive differ
# depending on which game phase it is, but the
# Client's socket flow remains the same.
isSetup = True
isClientGuess = False
isServerGuess = False
isRoundResults = False

# Citation for missing command line argument check:
# Date: 8/7/2022
# Adapted from:
# https://stackoverflow.com/questions/57359271/how-handle-sys-argv-if-null-argument-is-given
if len(sys.argv) != 2:
    print("Error: Missing port number to connect to")
    print("Usage: sudo python3 client_ec.py 25403")
    quit()

# Citation for command line argument usage:
# Date: 8/7/2022
# Adapted from:
# https://machinelearningmastery.com/command-line-arguments-for-your-python-script/
serverPort = int(sys.argv[1])
# serverPort = 65282

################################################################
### 1. Create a socket and bind to 'localhost' and port xxxx ###
################################################################

# Connection == acceptance of game
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(("localhost", serverPort))
print('Connected to: localhost on port: ' + str(serverPort))
print('\r\n!!!\r\nlocalhost on port: ' + str(serverPort) + ' has challenged you to a Game of Mini Battleships!')

# Begin Game and print Game rules
me = Game()
me.displayRules()

# Begin Client's Socket Flow of Send-then-Receive
while True:

    if not isSetup: # game not in-play yet
        if not me.isGameInPlay(): # Check game status
            break
        else: # Update round counter
            me.setRoundCount(me.getRoundCount() + 1)

    #######################################################
    ### 2. When connected, prompt for a message to send ###
    #######################################################
 
    # Get message required per game phase
    if isSetup:
        message = me.getPlayer().initMyBoard()
    elif isClientGuess:
        message = me.getMyGuess()
    elif isServerGuess:
        message = me.getContinue()
    elif isRoundResults:
        message = me.processEnemysGuess(data.decode())

    #########################################
    ### 3. If message is /q, client quits ###
    #########################################

    # If client wanted to quit
    if message.upper() == 'QUIT':
        clientSocket.send(message.encode()) # Let server know we've quit
        break        

    ######################################
    ### 4. Otherwise, send the message ###
    ######################################

    clientSocket.send(message.encode())

    ####################################
    ### 5. Call recv to receive data ###
    ####################################

    # Print 'waiting' messages
    if isSetup:
        print('!!!\r\nWaiting for localhost on port: ' + str(serverPort) + ' to set up their board...') 
    elif isClientGuess:
        print('!!!\r\nWaiting on localhost on port: ' + str(serverPort) + ' whether hit or miss...') 
    elif isServerGuess:
        print('!!!\r\nWaiting for localhost on port: ' + str(serverPort) + ' to send their guess...') 
    elif isRoundResults:
        print('!!!\r\nWaiting whether localhost on port: ' + str(serverPort) + ' would like to continue...') 

    # Receive data
    data = clientSocket.recv(1024)

    # If server wanted to quit
    if data.decode().upper() == 'QUIT':
        print('!!!\r\nlocalhost on port: ' + str(serverPort) + ' has decided to quit.')      
        break 

    #########################
    ### 6. Print the data ###
    #########################

    print(data.decode())

    #########################
    ### 7. Back to Step 2 ###
    #########################

    # Cycle game phases
    if isSetup:
        isSetup = False
        isClientGuess = True 
    elif isClientGuess:
        me.processEnemyResponseToMyGuess(message, data.decode())
        isClientGuess = False
        isServerGuess = True
    elif isServerGuess:
        isServerGuess = False
        isRoundResults = True     
    elif isRoundResults:
        isRoundResults = False
        isClientGuess = True      

#############################
### 8. Sockets are closed ###
#############################

clientSocket.close()