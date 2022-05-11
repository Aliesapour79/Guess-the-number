import random 
import sys
i=0
x = random.randint(0,5) 

while i<3:
	nuser = input("Please Enter Number : ")
	nuser = int(nuser)
	if nuser == x : 
		print("...WoW...")
		print("Shoma movafagh Shodid ... ")
		sys.exit(0)
		# end()
	elif x > nuser :
		print("Add tolid shode bozorgtar ast. ")
	else :
		print("Add tolid shode kochektar ast ast. ")
	i+=1
print("Shoma movafagh NaShodid ... ")