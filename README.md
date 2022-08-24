# Description:
This program utilizes a client-server socket connection to allow 2 players to play an ascii game of Mini Battleships. 

The game is considered "mini" battleships in the sense that the board size, ship count, and ship sizes have been scaled down from the typical Battleship game. If this project were to be expanded upon further, I would update it to utilize the full standard board size, ship count, and ship sizes/shapes of a typical Battleship game.
# Files:
This programming project contains six (6) total source code files: 
* board.py
* client.py
* game.py
* input_validator.py
* player.py
* server.py

# How to run:

These instructions assume the users are running the code on a Linux environment and that Python3 is installed. The code in the screenshots below were run in Ubuntu on Windows 10 in administrator mode.
### To run:
1. Clone this repo and ensure you have Python3 installed, and are running it in a Linux environment.
2.	In an instance of a Linux command line, have player 1 navigate to the folder where the source files are located, and run the server program as follows to initiate a connection:
    * Enter ‘sudo python3 server.py‘. 
    * Enter your password if prompted, then hit enter to run the program.
3.	Note the randomly generated port number that the server will be listening on once run. It will be output to the console as such:
    * ‘Server listening on: localhost on port: **27339**’
4.	In a new instance of a Linux command line, have player 2 navigate to the folder where the source files are located, and run the client program as follows, supplying the earlier-noted port number as a command line argument:
    * Enter ‘sudo python3 client.py **27339**‘. 
    * Enter your password if prompted, then hit enter to run the program.
5.	The port number used when running the client program **must** match the port number output to the console after initiating the server program.
6.	Follow the rules and prompts output to the console during the program to play the game to completion, or to quit when prompted.

# Screenshots of running code
##### How to run server
![alt text](https://github.com/emalpaya/miniBattleships/screenshots/001_how_run_server.PNG?raw=true)
Screenshot 1. Server program after running and no connections made yet.
##### How to run client
![alt text](https://github.com/emalpaya/miniBattleships/screenshots/002_how_run_client.PNG?raw=true)
Screenshot 2. Client program (right) after connecting to Server program (left). Server program auto-updates once connection is made.
##### Running code - Gameplay - Post-board setup (Similar output whether Server or Client)
![alt text](https://github.com/emalpaya/miniBattleships/screenshots/003_gameplay_post_board_setup.PNG?raw=true)
Screenshot 3. Server program (left) and Client program (right) after board setup phase.
##### Running code - Gameplay - Guessing Phase (Similar output whether Server or Client)
![alt text](https://github.com/emalpaya/miniBattleships/screenshots/004_gameplay_guessing_phase.PNG?raw=true)
Screenshot 4. Server program (left) and Client program (right) during back-and-forth guessing phase.
##### Running code - Gameplay - Game Over (Similar output whether Server or Client)
![alt text](https://github.com/emalpaya/miniBattleships/screenshots/005_gameplay_game_over.PNG?raw=true)
Screenshot 5. Server program (left) and Client program (right) after game is over and one has won.
##### Numeric input validation ![alt text](https://github.com/emalpaya/miniBattleships/screenshots/006_numeric_input_val.PNG?raw=true)
Screenshot 6. Numeric input validation
##### Case-insensitive alpha input validation
![alt text](https://github.com/emalpaya/miniBattleships/screenshots/007_alpha_input_val.PNG?raw=true)
Screenshot 7. Case-insensitive alpha input validation.
##### Exception handling for missing command line argument in Client program
![alt text](https://github.com/emalpaya/miniBattleships/screenshots/008_client_arg_val.PNG?raw=true)
Screenshot 8. Exception handling for missing command line argument, Client program.

# Comments/observations
The game I chose to utilize a client-server socket connection is a multiplayer (2-player) ascii game of Mini Battleships. The game is considered "mini" battleships in the sense that the board size, ship count, and ship sizes have been scaled down from the typical Battleship game (in my game, the board is only 5x5 squares, utilizes only 3 ships per player, and each ship only takes up one 1x1 space). 

If this project were to be expanded upon further, I would update it to utilize the full standard board size, ship count, and ship sizes/shapes of a typical Battleship game.

The game cycles through different 'game phases' to follow the socket connection flow established by the homework prompt for server and client, respectively. It cycles through the 'Setup' phase once, then the remaining game phases until someone wins.

I needed to add the question asking each user if they would like to continue the game after each makes a guess to maintain the wait-then-receive rhythm between server and client. 


