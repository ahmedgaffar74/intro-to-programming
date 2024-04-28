import tkinter as tk
import random

# Define beats, loses, and other game logic as before
beats = {'r': 's', 'p': 'r', 's': 'p'}
loses = {value: key for key, value in beats.items()}
state = {'player': 0, 'computer': 0, 'ties': 0}
guesses = []
default = random.choice('rps')

def always_same():
    return default

def random_strategy():
    return random.choice('rps')

def beat_last():
    global strategy  # Add this line to access the global strategy variable
    
    if not guesses:
        return default
    last_choice, last_result = guesses[-1]
    if last_result == 'Draw!':
        # If the last round was a draw, choose the winning move against the user's last choice
        last_user_choice = last_choice
        new_strategy = beats[last_user_choice]
        if new_strategy == last_choice:
            # If the new strategy would result in a draw again, switch to a random strategy
            strategy = random_strategy
            return random_strategy()
        else:
            return new_strategy
    else:
        # If the last round wasn't a draw, follow the usual strategy of beating the user's last choice
        return loses[last_choice]

strategies = [always_same, random_strategy, beat_last]
strategy = random.choice(strategies)

def update_game(choice):
    if choice not in ['r', 'p', 's']:  # Check if choice is valid
        result_text.set('Invalid choice! Please choose again.')
        return
    
    computer = strategy()
    guess = (choice, computer)
    guesses.append(guess)

    if choice == computer:
        state['ties'] += 1
        result_text.set('Draw!')
    elif beats[choice] == computer:
        state['player'] += 1
        result_text.set('Victory - (Player Won!)')  # Updated text for player win
    else:
        state['computer'] += 1
        result_text.set('Defeat - (Computer Won)')  # Updated text for computer win

    player_points.set('Player points: {}'.format(state['player']))
    computer_points.set('Computer points: {}'.format(state['computer']))

    if state['player'] == 5:
        result_text.set('PLAYER WINS!')
        root.quit()
        save_result('Victory - (Player Won!)')

    if state['computer'] == 5:
        result_text.set('COMPUTER WINS!')
        root.quit()
        save_result('Defeat - (Computer Won)')

def save_result(outcome):
    with open('file.txt', 'a') as file:
        file.write(outcome + '\n')

# Create tkinter GUI
root = tk.Tk()
root.title("Rock Paper Scissors")
root.configure(bg="#D2B48C")

# Function to handle button click
def handle_rock():
    update_game("r")

def handle_paper():
    update_game("p")

def handle_scissors():
    update_game("s")

# GUI elements
label = tk.Label(root, text="Select your move:", width=20, height=2)
label.pack()

button_rock = tk.Button(root, text="Rock", command=handle_rock, width=10, height=2, bg="gray")
button_rock.pack()

button_paper = tk.Button(root, text="Paper", command=handle_paper, width=10, height=2, bg="white")
button_paper.pack()

button_scissors = tk.Button(root, text="Scissors", command=handle_scissors, width=10, height=2, bg="red")
button_scissors.pack()

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, width=20, height=2)
result_label.pack()

player_points = tk.StringVar()
player_points_label = tk.Label(root, textvariable=player_points, width=20, height=2)
player_points_label.pack()

computer_points = tk.StringVar()
computer_points_label = tk.Label(root, textvariable=computer_points, width=20, height=2)
computer_points_label.pack()

# Run the tkinter event loop
root.mainloop()
 