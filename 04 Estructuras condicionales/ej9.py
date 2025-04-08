#9) Elabora un programa que permita al usuario ingresar
# 100 números enteros y luego calcule la media de esos valores.

cant_numeros = 3
sumatoria = 0
for cont in range (1, cant_numeros+1):
    print ("Ingrese un número", cont)
    num = int(input())
    sumatoria += num

print(f"La media de los {cant_numeros} números ingresados es",(sumatoria / cant_numeros))

