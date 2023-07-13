import random

userWins = 0
computerWins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Press Q to quit: ").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        print("Please type the correct option!")
        continue

    random_number = random.randint(0,2)
    # rock: 0, paper: 1, scissors: 2

    computer_picks = options[random_number]
    print("The Computer picked", computer_picks + ".")

    if user_input == "rock" and computer_picks == "scissors":
        print("You Won!!")
        userWins += 1
    

    elif user_input == "paper" and computer_picks == "rock":
        print("You Won!!")
        userWins += 1
        

    elif user_input == "scissors" and computer_picks == "paper":
        print("You Won!!")
        userWins += 1
        
    else:
        print("You Lost!!")
        computerWins += 1
    
print("You won", userWins, "times.")
print("The computer won", computerWins, "times.")
print("Thank You for Playing and Goodbye!")
