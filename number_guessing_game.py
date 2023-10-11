import random
import time
num = random.randint(1,100)
limit = 5
cnt = 0

print("Welcome to the number guessing game!")
print(f"Guess number between 1 and 100. you have 5 attempts.")

while cnt < limit:
    guess = input("Enter the Number:").strip()

    if guess.isdigit():
        guess = int(guess)
    else:
        print("Invalid! Enter numeric")
        continue

    cnt+=1

    if guess < num:
        print("try higher number")
    elif guess > num:
        print("try lower number")
    else:
        print(f"Congratulations! You guessed the correct number, which is {num}.")
        break


    time.sleep(1)

    if cnt == limit and guess != num:
        print(f"Sorry, you've run out of attempts. The correct number was {num}.")

