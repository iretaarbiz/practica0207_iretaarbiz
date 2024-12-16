import os
cliente = int(input("Introduce el número entero del 1 al 10 para devolver su tabla de multiplicar: "))
numerotfno = int(input("Introduce el número entero del 1 al 10 para devolver la fila correspondiente a ese numero de la tabla de multiplicar del numero anterior: "))
def crearlistin():
    if not os.path.isfile("listin.txt"):
        file = open("listin.txt", 'w')
    else:
        print("El fichero ya existe")
    file = close()
def consultartfno(cliente):
    file = open("listin.txt", 'r')
    filas = file.readlines()