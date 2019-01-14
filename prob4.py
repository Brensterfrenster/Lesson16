password = input("What is your password? " )
while password not in ["Open Sesame"]:
	print('Password is invalid, try again.')
	password = input("What is your password?" )
print('Password is valid, welcome!')
