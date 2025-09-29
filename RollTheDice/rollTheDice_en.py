import random
import time

def roll():
    print("Rolling the dice...")
    time.sleep(2)

    number = random.randint(1, 6)
    print("It has rolled a: ", number)

    rota()

def rota():
    rotar = input("Do you want to roll the dice again? (Y/N): ")
    if rotar.lower() == 'y':
        roll()
    elif rotar.lower() == 'n':
        print("Bye!")
    else:
        print("You have entered an invalid value, putting the dice away.")

roll()