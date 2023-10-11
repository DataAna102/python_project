import random

computer_score = 0
player_score = 0

# List of containing choices
list_opt = ["Rock", "Paper", "Scissor"]

# Define the game structure
def game_str():
    global player_score
    global computer_score

    while True:

        player = input("rock, paper or scissor ?").capitalize()
        computer = random.choice(list_opt) # Using random.choice() to select an item from the list
        print(f"You got {player} vs {computer}")

        if player == computer:
            print("It's a tie")
        elif (player == "Rock" and computer == "Scissor") or (player == "Paper" and computer == "Rock") or (player == "Scissor" and computer == "Paper"):
            print("Player won")
            player_score += 1
        else:
            print("Computer won")
            computer_score += 1

        play_again = input("Play again? (yes/no): ").lower()
        if play_again != "yes":
            break

# Start the game
game_str()

# Print the final scores
print("Game Over")
print(f"Computer score: {computer_score} vs Player score: {player_score}")
