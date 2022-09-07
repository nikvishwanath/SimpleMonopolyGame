# SimpleMonopolyGame
A simplified Monopoly game that two or more users can play in the command line.  

## The Game ##
Players start at the "GO" space on the circular board and take turns moving between 1-6 spaces around the board.  At the start of the game, players will have the option to choose how many spaces the board will contain, the starting balance for each player, the rental price for each of the spaces, and the amount received each time that the "GO" space is passed.  Be sure to carefully consider the rental prices of the spaces in relation to the starting balance and the pass "GO" amount so as to avoid an unwinnable game.       

Each space on the board may be purchased except for "GO".  Once purchased, the owner charges rent to the other 
players that land on the space.  When a player runs out of money, that player becomes inactive and cannot move or own 
spaces.  The game continues until all but one player have run out of money, at which point the remaining player is 
declared the winner.


## How to Run ##
To play, first download the code.  Then open the Terminal or Command Prompt and navigate to the directory.  Ensure that you have Python 3 installed, then run the following command 

python main.py

The game will be launched and you will be prompted to enter in the number/names of players, the starting balance, the number/rental prices of the board spaces, and the amount that each player receives upon passing the "GO" space.  The game will then start and continue until a winner is declared.    
