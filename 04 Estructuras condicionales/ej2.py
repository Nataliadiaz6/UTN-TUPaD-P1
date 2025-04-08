#2) Desarrolla un programa que solicite al usuario un número entero 
# y determine la cantidad de dígitos que contiene.

n = int(input("Ingrese un numero: "))
i = 0
while n > 0:
    n = n // 10
    i += 1
print(f"El numero tiene {i} dígitos")