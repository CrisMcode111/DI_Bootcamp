# Part I - game.py
# game.py – this file/module should contain a class called Game. It should have 4 methods:
# get_user_item(self) – Ask the user to select an item (rock/paper/scissors). Keep asking until the user has selected one of the items – use data validation and looping. Return the item at the end of the function.

# get_computer_item(self) – Select rock/paper/scissors at random for the computer. Return the item at the end of the function. Use python’s random.choice() function (read about it online).

# get_game_result(self, user_item, computer_item) – Determine the result of the game.
# Parameters:
# user_item – the user’s chosen item (rock/paper/scissors)
# computer_item – the computer’s chosen (random) item (rock/paper/scissors)
# Return either win, draw, or loss. Where win means that the user has won, draw means the user and the computer got the same item, and loss means that the user has lost.

# play(self) – the function that will be called from outside the class (ie. from rock-paper-scissors.py). It will do 3 things:
# Get the user’s item (rock/paper/scissors) and remember it

# Get a random item for the computer (rock/paper/scissors) and remember it

# Determine the results of the game by comparing the user’s item and the computer’s item
# Print the output of the game; something like this: “You selected rock. The computer selected paper. You lose”, “You selected scissors. The computer selected scissors. You drew!”

# Return the results of the game as a string: win;draw;loss;, where win means that the user has won, draw means the user and the computer got the same item, and loss means that the user has lost.



# game.py
import random

class Game:
    VALID_CHOICES = ("rock", "paper", "scissors")

    def get_user_item(self) -> str:
        
        while True:
            choice = input("Choose [rock/paper/scissors]: ").strip().lower()
            if choice in self.VALID_CHOICES:
                return choice
            print(" Invalid choice. Please type exactly: rock, paper, or scissors.")

    def get_computer_item(self) -> str:
        
        return random.choice(self.VALID_CHOICES)

    def get_game_result(self, user_item: str, computer_item: str) -> str:
        
        if user_item == computer_item:
            return "draw"

        wins_against = {
            "rock": "scissors",
            "paper": "rock",
            "scissors": "paper",
        }

        if wins_against[user_item] == computer_item:
            return "win"
        else:
            return "loss"

    def play(self) -> str:
        
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)

        outcome_text = {
            "win": "You win!",
            "loss": "You lose.",
            "draw": "It's a draw.",
        }[result]

        print(f"You selected {user_item}. The computer selected {computer_item}. {outcome_text}")

        return result
