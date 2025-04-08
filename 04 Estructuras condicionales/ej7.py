#7) Crea un programa que calcule la suma de todos los números comprendidos 
# entre 0 y un número entero positivo indicado por el usuario.
#La suma excluye el valor ingresado por el usuario.

valor_2 = int(input("Ingrese un numero mayor a 0: "))
sumatoria = 0

if 0 < valor_2:
    for x in range (0, valor_2):
        sumatoria += x
    print(f"La sumatria de los numeros comprendidos entre 0 y {valor_2} es {sumatoria} ")
else:
    print("El numero ingresado debe ser mayor que 0")
