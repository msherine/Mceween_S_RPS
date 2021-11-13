from random import randint
from gameComponents import winLose, gameVars

# create an infinite loop
while gameVars.player is False:

    gameVars.player = input("Choose your weapon: rock, paper or scissors: ")
    computer = gameVars.choices[randint(0, 2)]

    print("player choose: " + gameVars.player)
    print("computer choose: " + computer)

    if gameVars.player == computer:
        print("Tie! Try again.")

    elif gameVars.player == "rock":
        if computer == "paper":
            print("You lose!")
            gameVars.playerLives = gameVars.playerLives - 1
        else:
            print("You win!")
            gameVars.computerLives = gameVars.computerLives - 1

    elif gameVars.player == "paper":
        if computer == "scissors":
            print("You lose!")
            gameVars.playerLives = gameVars.playerLives - 1
        else:
            print("You win!")
            gameVars.computerLives = gameVars.computerLives - 1

    elif gameVars.player == "scissors":
        if computer == "rock":
            print("You lose!")
            gameVars.playerLives = gameVars.playerLives - 1
        else:
            print("You win!")
            gameVars.computerLives = gameVars.computerLives - 1

    print("player life count: " + str(gameVars.playerLives))
    print("computer life count: " + str(gameVars.computerLives))

    if gameVars.playerLives == 0:
        winLose.winorlose("lost")

    elif gameVars.computerLives == 0:
        winLose.winorlose("won")

    gameVars.player = False