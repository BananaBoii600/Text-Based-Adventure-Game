import time

def intro():
	print("After a long night party at your friend's house you arrive home.")
	print("You see a letter in your mailbox. An unusual occurence as bill day")
	print("is Monday not Friday.")
	print("You walk up to the mailbox and see that there is a red letter.")
	print("**QUITE SUSPICIOUS**\n")
	print("Press 'open' to open the mail.")
	print("Press 'go' to go inside.")

def go_inside():
	print("\nOn your way inside, you stepped on water and slipped.")
	print("On falling down, your head hit a rock and you died.")
	print("No one knows what happened to your body. Did the writer take it?")
	print("Play again to find out")

	print("THE END.")

def dive():
	print("\nOh no! You dived right into the mouth of a crocodile.")
	print("The END.")

def run_right():
	print("\nYou approach a fence and jumped the fence.")
	print("On looking up. You see a police station and you run into it.")
	time.sleep(3)
	print("45 minutes later the police sergeant returns.")
	print("He tells you that you were the bait in a drug bust...")
	print("but you're safe now. They've handled the situation.")
	time.sleep(2)
	print("\nYOU SURVIVED...")
	time.sleep(2)
	print("THE END.")

def stand_your_ground():
	print("\nAs the bike got to you.")
	print("It drifts to the side with a sharp stop.")
	time.sleep(3)
	print("Alas! It is a lady.")
	print("Then she pulls a shotgun towards you and...")
	time.sleep(3)
	print("\nshe said where is the money but you were confused.")
	print("You run into an old building by your right.")
	time.sleep(3)
	print("At the backdoor of the building...")
	print("There is a river and a short path to your right")
	time.sleep(3)
	print("\nPress 'dive' to jump into the river and swim across.")
	print("Press 'right' to run through the short path.")

	next_step = input(":> ")
	if next_step in "dive":
		dive()
	elif next_step in "right":
		run_right()


def run_away():
	print("\nYou run into a dark alleyway by your left.")
	print("At the end of the alleyway...")
	time.sleep(3)
	print("There is a river and a short path to your right")
	print("\nPress 'dive' to jump into the river and swim across.")
	print("Press 'right' to run through the short path.")

	next_step = input(":> ")
	if next_step in "dive":
		dive()
	elif next_step in "right":
		run_right()

def go_to_beach():
	print("\nYou get to the beach a minute to 11.P.M.")
	print("All you see is the empty atmosphere.")
	time.sleep(3)
	print("There is nobody here. Now you're beginning to wonder, is this a prank or")
	print("did the person forget?:(")
	time.sleep(3)
	print("\nThen you heard the rumble of an engine...")
	print("As you looked to your side, you saw a bike moving towards you.")
	print("It's coming at an high speed.")
	time.sleep(3)
	print("Will you stand your ground or run away?\n")
	print("\nPress 'stay' to stand your ground")
	print("Press 'run' to run away.")

	next_step = input(":> ")
	if next_step in "stay your ground":
		stand_your_ground()
	elif next_step in "run away":
		run_away()
	else:
		print("Wooo! Wrong input. PLAY AGAIN.")

def open_letter():
	print("\nYou are too curious to check your mail.")
	print("You grab it and find 8 words")
	print("Meet me on the beach side at 11 P.M.\n")
	print("You're not sure whether to go or not")
	print("\nPress 'go inside' to go inside your house")
	print("Press 'go to beach' to go to the beach side.")

	next_step = input(":> ")
	if next_step in "go inside":
		go_inside()
	elif next_step in "go to beach":
		go_to_beach()
	else:
		print("You should watch your spellings. GAME OVER.")


def start():
	intro()
	next_step = input(":> ")
	if next_step in "open letter":
		open_letter()
	elif next_step in "go inside":
		go_inside()
	else:
		print("Wrong Input. GAME OVER.")

start()