from art import *
import os



def clear():
    os.system('clear')


clear()


text = "Dondi"
tprint(text)


def menu():
    print("1) Ingresar registro")
    print("2) Visualizar deuda")
    print("3) Agregar proveedor")
    print("4) Salir")
    opcion = input("\nIngrese una opción: ")
    return opcion

while True:
    opcion = menu()
    if opcion == "1":
        print("Ingresar registro")
    elif opcion == "2":
        print("Visualizar deuda")
    elif opcion == "3":
        print("Agregar proveedor")
    elif opcion == "4":
        break

clear()
