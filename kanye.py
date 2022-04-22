#!/usr/bin/python3
import requests
kanye_url = requests.get('https://api.kanye.rest')
def main():
    while True:    
        print("\nThe Gospel According to Kanye West\n")
        user_input1 = input("Would you like to hear a quote from the Gospel of Kanye West? y/n")
        if user_input1 == "y":
            print(kanye_url.json())
        user_input2 = input("would you like to hear another? y/n")
        if user_input1 == "y":
            print(kanye_url.json())
            break
        elif user_input2 == "n":
            print("goodbye")   
        elif user_input1 == "n":
            print("Goodbye!")
main()