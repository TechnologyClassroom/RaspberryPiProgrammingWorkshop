# Instructions
# Run the game with this command in a terminal:
# python3 TheGameThatMarioBeat.py

print("Press the enter key to beat the game.")

game = input("Press the enter key now.")

if not game:
	print('You win, Mario.  Now you can say, "The only game that I have ever beaten is The Game That Mario Beat!"')
else:
	print("You lose, try again!")

