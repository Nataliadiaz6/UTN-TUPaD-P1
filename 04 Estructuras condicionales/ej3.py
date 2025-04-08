#3) Escribe un programa que sume todos los números enteros comprendidos entre 
# dos valores dados por el usuario, excluyendo esos dos valores.

valor = int(input("Ingrese un numero entero: "))
valor_2 = int(input("Ingrese otro numero entero, debe ser mayor al anterior y no puede ser consecutivo: "))
sumatoria = 0
valor_1 = valor + 1
if valor_1 < valor_2:
    for x in range (valor_1, valor_2):
        sumatoria += x
    print(f"La sumatria de los numeros comprendidos entre {valor} y {valor_2} es de {sumatoria} ")
else:
    print("El primer numero debe ser menor al segundo numero, y no pueden ser numeros consecutivos")

