# Okay it's time to get busy. I will get all of the little python knowledge
# I had back.
# I will make a text adventure game on this platform if it kills me!
'''
TO DO:
-Cool text art stuff
-Thinking chart
'''
import os
from datetime import datetime

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

clear()
print "Welcome to Dungeons of Chaos"
#see this is where i want that cool text art
raw_input("PRESS ENTER TO CONTINUE")
clear()
print "The current date and time is:"
print datetime.now()
raw_input("PRESS ENTER TO CONTINUE")
clear()
print "This is a work in progress, under developement by Mitchel Geerds."
print "What you see here is not a final copy."
raw_input("PRESS ENTER TO CONTINUE")
clear()
print "You are about to enter a very dangerous dungeon full of traps to kill you."
raw_input("PRESS ENTER TO CONTINUE")
clear()
print "But if you can make it to the end, you will be rewarded."
raw_input("PRESS ENTER TO CONTINUE")
clear()
print "Prepare to enter the dungeon!"
#maybe more cool text art? idk something transitiony
raw_input("PRESS ENTER TO CONTINUE")
clear()
print "There is no save game function in Dungeon of Chaos."
print "The game is controled by typing z or x for one of the two choices."
print "IMPORTANT: There is currently a codeing error with DoC where answering something other than x or z will exit the game."
print "Good luck!"
raw_input("PRESS ENTER TO CONTINUE")
clear()
#MOAR TRANSITIONS NEEDED
print "You awaken in the middle of a dark and damp room. You can hear running water close by."
print "z: You get up to examin your surroundings."
print "x: You stay sitting a bit longer to gather your thoughts."
def answerone():
	answer = raw_input("z or x?")

	if answer == "z":
		clear()
		print "You stand up just to fall back down. Your legs are asleep!. What do you do?"
		print "z: Try again"
		print "x: Slap your legs silly"
		answer = raw_input("z or x?")
		clear()
		if answer == "z":
			clear()
			print "You attempt to get up again, but fall right back down."
		elif answer == "x":
			clear()
			print "You slap your legs until they are a bright red. It hurts, but your legs are now awake and you stand up."
	elif answer == "x":
		clear()
		print "You sit on the floor for five minutes allowing your mind to clear. Feeling refreshed, you stand up."
		print "z: Go towards sound of running water"
		print "x: Look around walls for doors"
	else:
		print "I do not understand. Please answer z or x."
		answerone()
