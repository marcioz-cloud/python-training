import random

# input to customer be able to select the option he wants
player = input("What is your choice? ")

# make all letters of string lower to avoid problems in capital leters
player1 = player.lower()

# creating the list with option
list = ['rock', 'paper', 'scissors']

# select a choice from the list
pc = random.choice(list)

# Concidtions and print
if player1== "rock" and pc== "rock": print("Tie")
elif player1== "rock" and pc== "paper": print(f"PC Won, robot selected {pc}.")
elif player1 == "rock" and pc == "scissors": print(f"Player 1 Won, robot selected {pc}.")

elif player1== "paper" and pc== "paper": print("Tie")
elif player1== "paper" and pc== "scissors": print(f"PC Won, robot selected {pc}.")
elif player1 == "paper" and pc == "rock": print(f"Player 1 Won, robot selected {pc}.")

elif player1== "scissors" and pc== "scissors" : print("Tie")
elif player1== "scissors" and pc== "paper": print(f"Player 1 Won, robot selected {pc}.")
elif player1== "scissors" and pc== "rock": print(f"PC Won, robot selected {pc}.")

#Finishing with else.
else: print("Not a valid option. Try again.")