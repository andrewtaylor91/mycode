import random
answer = input("Would you like to play a game? y/n ")
rps = {"rock":1, "paper":2, "scissors":3}
if answer == "y":
    choice = input("Choose rock, paper, or scissors: ")
    our_choice = random.choice(["rock", "paper", "scissors"])
    print(choice, our_choice)
    if choice == our_choice:
        print(f"Both players selected {user_action}. It's a tie!")
elif choice == "rock":
    if user_choice == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif choice == "paper":
    if our_choice == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif choice == "scissors":
    if our_choice  == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")



