import string
import random

len = int(input("Enter length of the password : "))

print('''Choose the character for password from these : 
		1. Digits
		2. Letters
		3. Special characters
		4. Exit''')

char_List = ""

while(True):
	choice = int(input("Pick a number : "))
	if(choice == 1):
		
		
		char_List += string.ascii_letters
	elif(choice == 2):
		
		
		char_List += string.digits
	elif(choice == 3):
		
		
		char_List += string.punctuation
	elif(choice == 4):
		break
	else:
		print("Pick a valid option !")

password = []

for i in range(len):


	randomchar = random.choice(char_List)
	
	
	password.append(randomchar)


print("The random password is : " + "".join(password))
