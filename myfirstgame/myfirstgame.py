import random
computerGuess= random.randint(0,100)
while True:
	user= input("guess a number between 0-100:")
	if user > computerGuess:
		print("guess lower")
	elif user < computerGuess:
		print("guess higher")
	else:
		print("You are right")
			



