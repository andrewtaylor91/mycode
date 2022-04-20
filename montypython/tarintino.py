#!/usr/bin/env python3 #shebang
import random #import random

films = ["Resivour Dogs", "Kill Bill", "Pulp Fiction", "Ingloriuos Basterds" , "The Hateful 8", "Django: Unchained"] #list of tarintino films
print("Would you like to watch a tarintino film? y/n")
answer1 = input()
if answer1 == "y":
    print("You should watch -" + random.choice(films))
    print("would you like to know more about the film?")
    answer2 = input()
    if answer2 == "y":
        print("Synopsis")
    elif answer2 == "n":
            print("Enjoy the movie!")
elif answer1 == "n":
        print("Are you sure?")
        answer3 = input()
        if answer3 == "y":
            print("You should watch -" + random.choice(films))
        elif answer3 == "n":
            print("Maybe another time!")
else:
    print("please enter y or n")