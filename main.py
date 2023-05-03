from art import *
import os
import pandas as pd



def clear():
    os.system('clear')


clear()


text = "Dondi"
tprint(text)



#Verificar si existe el archivo csv
#Si no existe sera á creado el archivo con las columnas fecha, proveedor y monto 

filename = "registros.csv"
file_exists = os.path.isfile(filename)

if not file_exists:

    df = pd.DataFrame(columns=['fecha', 'proveedor', 'monto'])
    df.to_csv(filename, index=False)







    
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
