#!/usr/bin/env python3


score = int(input("What is your score out of 100?"))

if score >= 90:
    print('You got an A!')
elif score >= 80:
    print ('You got a B!')
elif score >= 70:
    print ('You got a C!')
elif score >= 60:
    print ('You got a D!')
elif score <= 59:
    print ('You got a F!')
else:
    print("You did not enter a valid score!")
