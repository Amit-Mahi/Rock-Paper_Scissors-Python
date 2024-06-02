# lets create a rock paper scissors Game 

import random


user_wins= 0
computer_wins = 0

# Ask player permission to play the game
user_input = input("Would you like to play Rock, Paper and Scissors ? ")


options = ["rock", "paper", "scissors"]

if user_input.lower() != "yes":
    quit

else:
    # run the loops as many times you want
    while True:

        #asking for the player options
        player_option = input("Choose one Rock/Paper/Scissors or Q to quit: ")

        # if player wants to end the game just press q or Q
        if player_option.lower() == 'q':
            break

        # generating a random number to create computer options
        random_number = random.randint(0,2)
        computer_choice = options[random_number]

        # check if the player choose the right option
        if player_option in options:
            
            # condition to check the player won the round or not
            if (player_option == 'rock' and computer_choice == 'scissors') or (player_option == "paper" and computer_choice == "rock") or (player_option == 'scissors' and  computer_choice == 'paper'):
                print("you won")
                user_wins += 1  # increment the user wins by 1

            # condition to check if the current round is ties or not
            elif (player_option == 'rock' and computer_choice == 'rock') or (player_option == "paper" and computer_choice == "paper") or (player_option == 'scissors' and  computer_choice == 'scissors'):
                print("It's a Tie") 

            # if ans elif condition are false means computer has won the round
            else: 
                print("Computer Has Won This Round")
                computer_wins += 1 # increment the computer wins by 1

        else: 
            print("Invalid Choice!")

# printing the stats of the game
print(f'You have won {user_wins} Times')
print(f'Computer have won {computer_wins} Times')
print("Goodbye!")