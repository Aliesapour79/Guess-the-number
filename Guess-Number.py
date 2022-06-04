import random 
import sys
i=0
x = random.randint(0,5) 

while i<3:
	nuser = input("Please Enter Number : ")
	nuser = int(nuser)
	if nuser == x : 
		print("...WoW...")
		print("You have succeeded in guessing the number")
		sys.exit(0)
		
	elif x > nuser :
		print("Input Number Is Low. ")
	else :
		print("Input Number Is High. ")
	i+=1
print("You have not been able to guess the number ... ")
print("Try again")