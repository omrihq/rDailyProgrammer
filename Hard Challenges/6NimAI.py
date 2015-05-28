#create a AI that will play NIM. 
#NIM is a game in which two players want to be the last to take a token. Either player can take 1, 2, or 3 tokens per turn, but must take a token.
#I made two AI's, an easy one that is random, or a hard one

import random

def easy_nim_strategy(first):
	tokens = 15
	turn = first
	while tokens > 0:
		print "=========="
		if not turn:
			print "Okay, my turn now"
			if tokens <= 3:
				print "I\'m taking the last %s tokens! I win!" %tokens
				tokens - tokens
				break
			else:
				to_take = random.randrange(1,4)
				tokens = tokens - to_take
				print "I\'m taking %s tokens! There are %s tokens left" % (to_take, tokens)
				turn = not turn
		else:
			print "Your turn! There are %s tokens left" % tokens
			to_take = int(raw_input("How many tokens would you like to take? (Enter 1, 2 or 3) "))
			tokens = tokens-to_take
			print "After taking %s tokens, there are %s tokens left" % (to_take, tokens)
			turn = not turn
			if tokens <= 0:
				print "Wow, you managed to beat me!"

def hard_nim_strategy(first):
	tokens = 15
	#Want to take 3, 7, 11, and 15
	while tokens > 0:
		print "=========="
		if not first:
			print "Okay, my turn"
			if tokens <= 3:
				print "I\'m taking the last %s tokens! I win!" %tokens
				tokens - tokens
				break
			else:
				if tokens % 4 != 0:
					to_take = tokens%4
				else: to_take = 1
				tokens = tokens - to_take
				print "I\'m taking %s tokens! There are %s tokens left" % (to_take, tokens)
				first = not first
		else:
			print "Your turn! There are %s tokens left" % tokens
			to_take = int(raw_input("How many tokens would you like to take? (Enter 1, 2 or 3) "))
			tokens = tokens-to_take
			print "After taking %s tokens, there are %s tokens left" % (to_take, tokens)
			first = not first
			if tokens <= 0:
				print "Wow, you managed to beat me!"


def main():
	tokens = 15
	welcome = "Welcome to NIM, NIM is a game in which two players want to be the last to take a token, from a pile of 15 tokens. A player can take 1, 2, or 3 tokens per turn, but must take a token. The winner is the player to take the last token."
	strategy = raw_input(welcome + " What difficulty would you like to play on easy or hard difficulty (E or H) ") == "H"
	first = raw_input("Would you like to go first? (Y or N) ") == "Y"

	if strategy:
		hard_nim_strategy(first)
	else:
		easy_nim_strategy(first)

if __name__ == '__main__':
	main()