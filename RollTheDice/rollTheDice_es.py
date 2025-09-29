import random
import time

def roll():
    print("Tirando el dado...")
    time.sleep(2)

    number = random.randint(1, 6)
    print("Ha salido: ", number)

    rota()

def rota():
    rotar = input("Quieres volver a tirar el dado? (Y/N): ")
    if rotar.lower() == 'y':
        roll()
    elif rotar.lower() == 'n':
        print("Adios!")
    else:
        print("Has ingresado un valor invalido, guardando el dado.")

roll()
