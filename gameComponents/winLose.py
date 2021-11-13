from gameComponents import gameVars

def winorlose(status):
	print("You " + status + "! Would you like to play again?")
	choice = input(" Y / N? ")

	if choice == "n":
		print(" Better luck next time!")
		exit()
	# reset and restart
	elif choice == "y":
		gameVars.playerLives = 5
		gameVars.computerLives = 5
		gameVars.player = False