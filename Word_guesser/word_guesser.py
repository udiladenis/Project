import random
import os
lst = ["yes", "y"]
list = ["aluna", "bicicleta", "trotineta"]
rasp = input("Hello fella! Do you wanna play a game?: ")
if rasp.lower() in lst:
    print("Welcome to our game Fella!")
    print("In this game you should pick an item from a given list. You will play against the computer! He will also pick an item from that list and what u need to do is to guess which was the computer selected item!")
    print("Rules: ")
    print("1.The game will start ONLY IF YOU PICK ITEMS FROM LIST! ")
    print("2.You will have a number of lifes. If lives runes out, the game will stop!")
    print("3. And the most important RULE: HAVE FUN! :)")
    list = ["aluna", "bicicleta", "trotineta", "nu"]
    random_item = random.choice(list)
    print("\nHere we GO!")
    nr_of_lifes = 3
    # Validarea inputului
    while True and nr_of_lifes > 0:
        choice = input(f"Please pick in item from this list {list}: ")
        if choice in list:
            if choice == random_item:
                print("Well done mate! You guessed it!")
                break
            else:
                nr_of_lifes -= 1
                print(f"Ups! Wrong item! Your lifes: {nr_of_lifes}")
        else:
            print("Please pick an item that exists in list!")
            choice = input(f"Pick item from this list {list}: ")
    else:
        print("It seems that you just run ouf of lifes")
else:
    print("Have a nice day! :)")
