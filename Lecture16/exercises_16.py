#!/usr/bin/python3

#-----------------------------------
#A silly script, asking silly questions 
#Made by Max Falk
#07.12.24
#--------------------------------------

import os
info = {}

def personal() :
	name = input("What is your name?")
	info['name'] = name
	if name.lower().startswith('m'):
		print("Only fantastic names start with M!")
	else:
		print("Your name sucks!")

	age = int(input("How old are you?"))
	info['age'] = age
	if age >= 18 and age <=  29:
		print("What a nice youthful soul you are")
	else:
		print("Ye old HAG")

	return info
	
##NOTE:this is how you'd feed a dictionary of keys into function as arguments
##personal(*list(details.values()))


