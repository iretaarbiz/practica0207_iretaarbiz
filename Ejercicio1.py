numero = int(input("Introduce el número entero del 1 al 10 para guardar su tabla de multiplicar: "))
tablamult = ""
for i in range(1, 11):
    tablamult += str(numero) + " * " + str(i) + " = " + str(numero * i) + "\n"
nombre = "tabla-" + str(numero) + ".txt"
file = open(nombre, 'w')
file.write(tablamult)
file.close()
