#You're challenge for today is to create a random password generator!
#For extra credit, allow the user to specify the amount of passwords to generate.
#For even more extra credit, allow the user to specify the length of the strings he wants to generate!


import random

amount_of_passwords = int(raw_input("Enter the amount of passwords you would like generated: "))
password_length = int(raw_input("Enter the length of the passwords: "))

password_list = []

for i in xrange(amount_of_passwords):
	password = ""
	for x in xrange(password_length):
		#Generate random character in range of ascii characters
		password += chr(random.randrange(33,125))
	password_list.append(password)

print password_list

