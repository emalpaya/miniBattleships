# Copyright (C) Eva Malpaya
# #################################################################################################################### 
# Eva Malpaya
# CS 372, Oregon State University
# Programming Project 4
# August 7, 2022
#
# Description:
#   EXTRA CREDIT VERSION.
#   This program utilizes a server socket connection to initialize a multiplayer (2-player) ascii game of Mini 
#   Battleships, waits for a client connection, then plays the game.
#
#   The game cycles through different 'game phases' to follow the server socket connection flow of receiving 
#   then sending. It cycles through the 'Setup' phase once, then the remaining game phases until someone wins.
#
#   The game is considered "mini" battleships in the sense that the board size, ship count, and ship sizes have been 
#   scaled down from the typical Battleship game.
#
#   If this project were to be expanded upon further, I would update it to utilize the full standard board size, 
#   ship count, and ship sizes/shapes of a typical Battleship game.
#
# In: None
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
import random

# Game Phases:
# These are the 4 main phases of the game.
# Server's socket flow here is receive-then-send.
# Data to receive and Message to send differ
# depending on which game phase it is, but the
# Server's socket flow remains the same.
isSetup = True
isClientGuess = False
isServerGuess = False
isRoundResults = False

################################################################
### 1. Create a socket and bind to 'localhost' and port xxxx ###
################################################################

# Citation for the following code to generate random number:
# Date: 7/03/2022
# Adapted from:
# Source URL: https://pynative.com/python-random-randrange/
serverPort = random.randint(1024, 65535)
serverSocket = socket(AF_INET, SOCK_STREAM)
#serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSocket.bind(('localhost', serverPort))

##################################
### 2. Listen for a connection ###
##################################

print('Initiating Game of Mini Battleships...')
print('Server awaiting new challengers on: localhost on port: ' + str(serverPort))
serverSocket.listen(1)
connectionSocket, addr = serverSocket.accept()
print('\r\n!!!\r\nA new challenger appeared! Connected by ' + str(addr) + '')

# Begin Game and print Game rules
me = Game()
me.displayRules()

# Begin Server's Socket Flow of Receive-then-Send
while True:

    if not isSetup: # game not in-play yet
        if not me.isGameInPlay(): # Check game status
            break
        else: # Update round counter
            me.setRoundCount(me.getRoundCount() + 1)
    
    ####################################################
    ### 3. When connected, call recv to receive data ###
    ####################################################

    # Print 'waiting' messages
    if isSetup:
        print('!!!\r\nWaiting for challenger on ' + str(addr) + ' to set up their board...') 
    elif isClientGuess:
        print('!!!\r\nWaiting for challenger on ' + str(addr) + ' to send their guess...') 
    elif isServerGuess:
        print('!!!\r\nWaiting whether challenger on ' + str(addr) + ' would like to continue...') 
    elif isRoundResults:
        print('!!!\r\nWaiting on challenger on ' + str(addr) + ' whether hit or miss...') 
      
    # Receive data
    data = connectionSocket.recv(1024).decode()

    ##################################################
    ### 4. Print the data, then prompt for a reply ###
    ##################################################

    print(data) 

    # If client wanted to quit
    if data.upper() == 'QUIT':
        print('!!!\r\nChallenger on ' + str(addr) + ' has decided to quit.')      
        break    

    # Prompt for reply
    if isSetup:
        reply = me.getPlayer().initMyBoard() # Setup my ships
    elif isClientGuess:
        reply = me.processEnemysGuess(data)
    elif isServerGuess:
        reply = me.getMyGuess()
    elif isRoundResults:
        me.processEnemyResponseToMyGuess(reply, data)
        reply = me.getContinue()
     
    #######################################
    ### 5. If reply is /q, server quits ###
    #######################################

    # If server wanted to quit
    if reply.upper() == 'QUIT':
        connectionSocket.send(reply.encode()) # Let client know we've quit
        break

    ################################
    ### 6. Otherwise, send reply ###
    ################################

    connectionSocket.send(reply.encode())

    #########################
    ### 7. Back to step 3 ###
    #########################

    # Cycle game phases
    if isSetup:
        isSetup = False
        isClientGuess = True 
    elif isClientGuess:
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

connectionSocket.close()   