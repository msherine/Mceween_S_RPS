from random import randint
from gameComponents import winLose, gameVars

# create an infinite loop
while gameVars.player is False:
    print("∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ RPS GAME ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫▫·∙∙")
    gameVars.player = input("Choose your weapon: rock, paper or scissors: \n")
    computer = gameVars.choices[randint(0, 2)]

    print("player choose: \n" + gameVars.player)
    print("computer choose: \n" + computer)
    print("====================================================")

    if gameVars.player == computer:
        print("It's a tie! Try again.")

    elif gameVars.player == "rock":
        if computer == "paper":
            print("Oh no! You lose :(")
            gameVars.playerLives = gameVars.playerLives - 1
        else:
            print("You win! (ﾉ^ヮ^)ﾉ*:・ﾟ✧")
            gameVars.computerLives = gameVars.computerLives - 1

    elif gameVars.player == "paper":
        if computer == "scissors":
            print("Oh no! You lose :(")
            gameVars.playerLives = gameVars.playerLives - 1
        else:
            print("You win! (ﾉ^ヮ^)ﾉ*:・ﾟ✧")
            gameVars.computerLives = gameVars.computerLives - 1

    elif gameVars.player == "scissors":
        if computer == "rock":
            print("Oh no! You lose :(")
            gameVars.playerLives = gameVars.playerLives - 1
        else:
            print("You win! (ﾉ^ヮ^)ﾉ*:・ﾟ✧")
            gameVars.computerLives = gameVars.computerLives - 1

    print("Player life count: " + str(gameVars.playerLives))
    print("Computer life count: " + str(gameVars.computerLives))

    if gameVars.playerLives == 0:
        winLose.winorlose("lost")

    elif gameVars.computerLives == 0:
        winLose.winorlose("won")

    gameVars.player = False