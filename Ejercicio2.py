import os
numero = int(input("Introduce el número entero del 1 al 10 para devolver su tabla de multiplicar: "))
nombre = "tabla-" + str(numero) + ".txt"
if os.path.isfile(nombre):
    file = open(nombre, 'r')
    print(file.read())
else:
    print("El fichero no existe")
file.close()