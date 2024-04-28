name: ahmed gaffar
pnumber: p437907
course module: IY499
I confirm that this assignment is my own work.  
Where I have referred to online sources, I have provided comments detailing the reference and included a link to the source. 
The code starts by importing the necessary modules, tkinter for the GUI, and random for generating random choices.
Dictionaries are defined to represent the game logic. 'beats' contains the winning moves for each choice, 'loses' contains the losing moves for each choice, and 'state' keeps track of the game state.
Three strategies are defined for the computer player:
always_same(): Always returns the same default choice.
random_strategy(): Chooses a random move.
beat_last(): Chooses the move that beats the player's last move or a random move if it's a draw.
A list of strategies and a variable 'strategy' are defined, with one strategy randomly chosen for each game.
The 'update_game' function is defined to update the game state based on the player's choice. It compares the player's choice with the computer's choice and updates the state accordingly.
The 'save_result' function is defined to save the outcome of each game to a text file.
The tkinter GUI is created with buttons for each move and labels to display the result and points.
Event handlers are defined for each button to call the 'update_game' function with the corresponding choice.
Finally, the tkinter event loop is started to run the GUI.
overall, this code creates a functional Rock, Paper, Scissors game with a graphical interface, allowing the player to play against the computer with different strategies. The game state is displayed in real-time, and the outcome of each game is saved to a file for record-keeping.





