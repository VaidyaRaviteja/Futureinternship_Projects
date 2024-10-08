# -*- coding: utf-8 -*-
"""FutureIntern_PD_01.ipynb"""

#Task 1 of part 1 of 2
#Claculator
#Function is about multiplication of two numbers

def Multiplication(i,j):
  return i*j

#Function is about division of two numbers
def Division(i,j):
  if j==0:
    return "Division by Zero is not possible"
  else:
    return i/j

#Function is about subtraction of two numbers
def Subtraction(i,j):
  return i-j

#Function is about addition of two numbers
def Addition(i,j):
  return i+j

print("Welcome to Dynamic Calculator")
print("Select the required operation: ")
print("a.Multiplication")
print("b.Division")
print("c.Subtraction")
print("d.Addition")

while True:
  choose = input("Enter your required operation index from above: ")
  if choose in ('a', 'b', 'c', 'd'):
     try:
       num1 = float(input("Enter the first number: "))
       num2 = float(input("Enter the second number: "))
     except ValueError:
       print("Invalid input. Please enter a valid numeric input.")
       continue

     if choose == 'a':
        print("Multiplication of num1 and num2 is",num1, '*' , num2, "=", Multiplication(num1, num2))
     elif choose == 'b':
        print("Division of num1 and num2 is",num1, '/', num2, "=", Division(num1, num2))
     elif choose == 'c':
        print("Subtraction of num1 and num2 is", num1, '-', num2,"=", Subtraction(num1, num2))
     elif choose == 'd':
        print("Addition of num1 and num2 is", num1, '+', num2,"=", Addition(num1, num2))

     other_operation = input("Do you want to perform another operation? (Yes/No)")
     if other_operation.lower() != 'yes':
       print("Calculation Operation got ended.")
       break
  else:
    print("Given input is invalid operation index. Please enter a valid operation index!")



# Task 1 part 2 of 2
# Number Guessing Game
import random
#Function is about number guess
def Number_Guess_Game():
  number_to_be_guessed = random.randint(1,100)
  Guess = None

  print("Welcome to the Number Guessing Game..!")
  print("I'm thinking of a number between 1 and 100")
  print("Can you guess it?")

  while Guess != number_to_be_guessed:
    try:
      Guess = int(input("Enter your guess number: "))

      if Guess < number_to_be_guessed:
        print("Sorry your guess is not upto the mark. Try again ")
      elif Guess > number_to_be_guessed:
        print("Sorry your guess is above the mark. Try again ")
      else:
        print("Congrats! Your guess is the correct one. ")
    except ValueError:
      print("Invalid input please enter an integer between 1 and 100.")

print(Number_Guess_Game())
