#8) Escribe un programa que permita al usuario ingresar 100 números enteros. 
# Luego, el programa debe indicar cuántos de estos números son pares, 
# cuántos son impares, cuántos son negativos y cuántos son positivos.

#El 0 es considerado numero positivo y par.

cant_numeros = 10
pares= 0
impares= 0
positivos= 0
negativos= 0

for cont in range (1, cant_numeros+1):
    print ("Ingrese un número", cont)
    num = int(input())
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num >= 0:
        positivos += 1
    else:
        negativos += 1

print(f"De los numeros ingresados: {pares} son pares, {impares} son impares, {positivos} son positivos y {negativos} son negativos.")

