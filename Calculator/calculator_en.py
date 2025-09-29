import os
import time

operation = 0

def addition():
    nums = list(map(int, input("Enter all the numbers separating them by a space: ").split()))
    return sum(nums)

def substraction():
    n1 = float(input("Enter the first number: "))
    n2 = float(input("Enter the second number: "))
    return n1 - n2

def multiplication():
    nums = list(map(int, input("Enter all the numbers separating them by a space: ").split()))

    rpta = 1
    for num in nums:
        rpta *= num

    return rpta

def division():
    n1 = float(input("Enter the first number: "))
    n2 = float(input("Enter the second number: "))

    if n2 == 0:
        print("Invalid division.")
    else:
        return n1/n2


def calc():
    print("Enter '1' for addition.")
    print("Enter '2' for substraction.")
    print("Enter '3' for multiplication.")
    print("Enter '4' for division.")

    global operation
    operation = input("You have entered: ")
    if operation == "1":
        rpta = addition()

    if operation == "2":
        rpta = substraction()

    if operation == "3":
        rpta = multiplication()

    if operation == "4":
        rpta = division()

    else:
        print("You have entered an invalid value.")

    os.system("cls||clear")

    print(f"The answer is: {rpta}")
    time.sleep(5)

    rota()


def rota():
    rotar = input("Do you want to use the calculator again? (Y/N): ")
    if rotar.lower() == 'y':
        calc()
    elif rotar.lower() == 'n':
        print("Bye!")
    else:
        print("You have entered an invalid value, closing the calculator.")

calc()