# -*- coding: utf-8 -*-
"""FutureIntern_Py_02.ipynb"""

#Rock, paper, Scissors game
#We import the random module to generate the computer's random selection.
import random

#This function randomly selects the computer's selection from the list of options.
def generate_computer_selection():
  options = ["rock","paper", "scissors"]
  return random.choice(options)

#This is to enter their selection and checks if it is valid. It will ask until a valid choice is entered.
def generate_user_selection():
  user_selection = input("Enter your choice (rock, paper, scissors: )").lower()
  return user_selection

#This function compares the user's selection with the computer's selection and evaluate the winner based on the game rules.
def evaluate_result(user_selection, computer_selection):
  if user_selection == computer_selection:
    return "It's a tie !!"
  elif(user_selection == "rock" and computer_selection == "scissors") or \
        (user_selection == "paper" and computer_selection == "rock") or \
        (user_selection == "scissors" and computer_selection == "paper"):
        return "You Win !!"

  else:
    return "Computer Wins !!"

#This is the main function of the game. It gets the selections, displays them, and prints the result.
def start_game():
  print("Welcome to Rock, Paper, Scissors game")

  while True:
    user_selection = input("Enter rock, paper, or scissors( or 'quit' to exit)").lower()

    user_selection = generate_user_selection()
    computer_selection = generate_computer_selection()
    outcome = evaluate_result(user_selection, computer_selection)
    print(outcome)

    if user_selection == "quit":
      print("Thanks for playing!")
      break

    if user_selection not in ["rock", "paper", "scissors"]:
      print("Invalid selection. please choose rock,or paper, or scissors.")
      continue

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
      print("Thanks for playing!!")
      break

#This ensures that the play_game() function is called only when the script is run directly, not when imported as a module.
if __name__ == "__main__":
  start_game()

