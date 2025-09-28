import os
import time

operacion = 0

def suma():
    nums = list(map(int, input("Ingresa todos los numeros separados por un espacio: ").split()))
    return sum(nums)

def resta():
    n1 = float(input("Ingresa el primer numero: "))
    n2 = float(input("Ingresa el segundo numero: "))
    return n1 - n2

def multiplicacion():
    nums = list(map(int, input("Ingresa todos los numeros separados por un espacio: ").split()))

    rpta = 1
    for num in nums:
        rpta *= num

    return rpta

def division():
    n1 = float(input("Ingresa el primer numero: "))
    n2 = float(input("Ingresa el segundo numero: "))

    if n2 == 0:
        print("Division invalida.")
    else:
        return n1/n2


def calc():
    print("Ingresa '1' para sumar.")
    print("Ingresa '2' para restar.")
    print("Ingresa '3' para multiplicar.")
    print("Ingresa '4' para dividir.")

    global operacion
    operacion = input("Has ingresado: ")
    if operacion == "1":
        rpta = suma()

    if operacion == "2":
        rpta = resta()

    if operacion == "3":
        rpta = multiplicacion()

    if operacion == "4":
        rpta = division()

    else:
        print("Has ingresado un valor invalido.")

    os.system("cls||clear")

    print(f"La respuesta es: {rpta}")
    time.sleep(5)

    rota()


def rota():
    rotar = input("Quieres volver a calcular? (Y/N): ")
    if rotar.lower() == 'y':
        calc()
    elif rotar.lower() == 'n':
        print("Adios!")
    else:
        print("Has ingresado un valor invalido, cerrando la calculadora.")

calc()