#we all know the classic "guessing game" with higher or lower prompts. lets do a role reversal; you create a program that will guess numbers between 1-100, and respond 
#appropriately based on whether users say that the number is too high or too low. Try to make a program that can guess your number based on user input and great code!

print "Think of a number between 1 and 100:"
print "Got it? Great, now I will guess it!"

guess = 50
low = 0
high = 100

while True:
	lowHigh = " (Enter \"Lower\" or \"Higher\" or \"Correct!\") "
	accuracy = raw_input("Is your number " + str(guess) + lowHigh)

	if accuracy == "Lower":
		high = guess
		guess = (low + high)/2
	elif accuracy == "Higher":
		low = guess
		guess = (low + high)/2
	else:
		break
		
print "Ha! So your number was " + str(guess) + "!" 