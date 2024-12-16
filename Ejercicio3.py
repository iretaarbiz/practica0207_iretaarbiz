import os
numero = int(input("Introduce el número entero del 1 al 10 para devolver su tabla de multiplicar: "))
numfila = int(input("Introduce el número entero del 1 al 10 para devolver la fila correspondiente a ese numero de la tabla de multiplicar del numero anterior: "))
nombre = "tabla-" + str(numero) + ".txt"
if os.path.isfile(nombre):
    file = open(nombre, 'r')
    filas = file.readlines()
    print(filas[numfila-1])
else:
    print("El fichero no existe")
file = close()