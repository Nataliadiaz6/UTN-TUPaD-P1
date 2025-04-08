#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. 
# Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

intentos = 1
import random
numero = random.randint(0, 9)
print(numero)
num = int(input("Adivina en que numero entre 0 y 9 estoy pensando: "))

while num != numero:
    intentos += 1
    num = int(input("Incorrecto, intenta otra vez: "))

print("Acertaste! la cantidad de intentos fueron ", intentos)


