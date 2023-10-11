import random
#min and max dice number
min_dnum = 1
max_dnum = 6
#default player scores
ComputerScore = 0
PlayerScore = 0
inplay = True

#define random

test = random.randint(min_dnum, max_dnum)
print(test)


#defining the game structure
def gamePlay():
    global inplay
    global ComputerScore
    global PlayerScore
    while inplay:
        Player = random.randint(min_dnum, max_dnum)
        Computer = random.randint(min_dnum, max_dnum)
        print(f"You got {Player} vs {Computer}")
        if (Player == Computer):
            print("it's tie")
        elif (Player > Computer):
            print ("Player won")
            PlayerScore +=1
        else:
            print("computer won")
            ComputerScore +=1
        inplay = input("Roll again?")
        if inplay == "exit or Exit":
            print("Game Over")
            print(f"computer score: {ComputerScore} vs player score: {PlayerScore}")
            break

gamePlay()
print("Game Over")
print(f"computer score: {ComputerScore} vs player score: {PlayerScore}")