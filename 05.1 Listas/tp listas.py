#TP Listas. Natalia Diaz - Comision 7.

#1
multiplos_de_cuatro = []
for numero in range(1, 101):
    if numero % 4 == 0:
        multiplos_de_cuatro.append(numero)

print(multiplos_de_cuatro)

#2
lista_ej2 = ["Soledad", "Natalia", "Diego", "Valentina", "Nicolas"]
print (f"El penúltimo elemento de la lista es: {lista_ej2[3]}")

#Con indexing con numero negativo:
lista_ej2 = ["Soledad", "Natalia", "Diego", "Valentina", "Nicolas"]
print (f"El penúltimo elemento de la lista es: {lista_ej2[-2]}")

#3
lista_vacia = []

lista_vacia.append("Natalia")
lista_vacia.append("Ayelen")
lista_vacia.append("Diaz")

print(lista_vacia)

#4
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"

print(animales)

#5
# Este programa elimina el mayor elemento de la lista.
#En este caso, el elemento es el 22.
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print (numeros)

#6
lista_ej6 = list(range(10, 31, 5))
print (lista_ej6[:2])

#7
autos = ["sedan", "polo", "suran", "gol"]
autos[1]= "Corolla"
autos[2]= "Focus"

print(autos)

#8
dobles = []

dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

print(dobles)

#9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
["agua"]]

#a
compras[2].append("jugo")
#b
compras[1][1] = "tallarines"
#c
compras[0].remove("pan")
#d
print(compras)

#10
lista_anidada = [15, "True", [25.5, 57.9, 30.6], "False"]
print(lista_anidada)
