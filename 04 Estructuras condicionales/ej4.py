#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. 
# El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

print("Introduzca los valores que quiere sumar, cuando finalice, presione 0")
total = 0
valor = input()
while int(valor) != int(0):
    total = int(total) + int(valor)
    valor = input()
print("La sumatoria de los numeros ingresados es: ", total)