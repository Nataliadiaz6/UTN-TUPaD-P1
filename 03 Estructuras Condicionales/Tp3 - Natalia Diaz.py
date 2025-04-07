#TP3-Condicionales. Natalia Diaz-Comision 7.

#1) Escribir un programa que solicite la edad del usuario. 
# Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input("Ingrese su edad: "))
if (edad >=18):
    print("Es mayor de edad") 
else:
    pass


#2)  Escribir un programa que solicite su nota al usuario. 
# Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; 
# en caso contrario deberá mostrar el mensaje “Desaprobado”.

nota = int(input("Ingrese su nota: "))
if (nota >=6):
    print("Aprobado") 
else:
    print("Desaprobado")


#3) Escribir un programa que permita ingresar solo números pares. 
# Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; 
# en caso contrario, imprimir por pantalla "Por favor, ingrese un número par".

numero = int(input("Ingrese un numero par: "))
#Si el resto del numero ingresado dividido 2 es cero, significa que el usuario ingreso un numero par, 
# si la division arroja un resto, significa que el usuario ingreso un numero impar.
if (numero % 2 == 0):
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")


#4) Escribir un programa que solicite al usuario su edad e imprima a que categoria pertenece:
#Niño/a < 12 años.
#12 años <= Adolecente <18 años.
#18 años <= Adulto/a joven <30 años.
#30 años <= Adulto/a.

edad = int(input("Ingrese su edad: "))
if (edad < 12):
    print("Usted esta dentro de la categoria de niño/a.")
elif (12 <= edad < 18):
    print ("Usted está dentro de la categoria de adolecente.")
elif (18 <= edad < 30):
    print ("Usted está dentro de la categoria de adulto/a joven.")
else:
    print ("Usted está dentro de la categoria de adulto/a.")


#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". 

contra = (input("Ingrese una contraseña que contenga entre 8 y 14 caracteres: "))
num = len(contra)
if (8 <= num <= 14):
    print ("Ha ingresado una contraseña correcta")
else:
    print ("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


#6) Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana 
# y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo.

#Importo la moda, la mediana y la media desde el paquete de estadisticas.
from statistics import mode, median, mean
#Genero una lista aleatoria tomando 50 numeros entre el 0 y el 100.
import random
lista = [random.randint(1, 100) for i in range (59)]
#Calculo moda, mediana y media.
moda = mode(lista)
print("La moda de la lista es", moda)
mediana = median(lista)
print("La mediana de la lista es", mediana)
media = mean(lista)
print("La media de la lista es", media)
#Segun los resultados anteriores, defino que forma de distribucion tiene la lista generada.
if (media > mediana > moda):
    print("Esta lista posee una distribución con un sesgo positivo o a la derecha.")
elif (media < mediana < moda):
    print("Esta lista posee una distribución con un sesgo negativo o la izquierda.")
elif (media == mediana == moda):
    print("Esta lista posee una distribución que no contiene sesgo.")
else: 
    print ("No se cumplen ninguna de las tres condiciones.")


#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; 
# en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

def validar(c):
    vocales = "aeiouAEIOU"
    if c in vocales:
        print (frase,"!")
    else:
        print (frase)
frase = input("Ingrese una frase o palabra: ")
c = frase[- 1]
validar(c)

#8) Escribir un programa que solicite al usuario que ingrese su nombre 
# y el número 1, 2 o 3 dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla.

nombre = (input("Ingrese su nombre: "))
opcion = int(input("¿Como desea leer su nombre? 1- En mayúsculas, 2- En minusculas o 3- Primer letra mayuscula y las demas en minusculas. Escriba 1, 2 o 3 segun desee: "))
if (opcion == 1):
    nombre_nuevo = nombre.upper()
    print (nombre_nuevo)
elif (opcion == 2):
    nombre_nuevo = nombre.lower()
    print (nombre_nuevo)
elif (opcion == 3):
    nombre_nuevo = nombre.title()
    print (nombre_nuevo)
else:
    print("Ingrese 1, 2 o 3.")


#9) Escribir un programa que pida al usuario la magnitud de un terremoto, 
# clasifiquelo según la escala de Richter e imprima el resultado por pantalla.

magnitud = int(input("Ingrese la magnitud de un terremoto: "))
if (magnitud < 3):
    print ("El terremoto fue muy leve. (imperceptible)")
elif (3 <= magnitud < 4):
    print("El terremoto fue leve. (ligeramente perceptible)")
elif (4 <= magnitud < 5):
    print("El terremoto fue moderado. (sentido por personas, pero generalmente no causa daños)")
elif (5 <= magnitud < 6):
    print("El terremoto fue fuerte. (puede causar daños en estructuras débiles)")
elif (6 <= magnitud < 7):
    print("El terremoto fue muy fuerte. (puede causar daños significativos)")
else:
    print("El terremoto fue extremo. (puede causar graves daños a gran escala)")



#10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio=int(input("Ingrese por favor en que hemisferio se encuentra.Usar '1' para Norte o '2' para Sur: "))
mes=int(input("Ingrese en que mes se encuentra (expresado en números): "))
dia=int(input("Ingrese el día (expresado en números): "))
if (mes==12 and dia >=21) or mes==1 or mes==2 or (mes==3 and dia<21):
    if hemisferio==1:
        print ("Usted se encuentra en invierno.")
    elif hemisferio ==2:
        print ("Usted se encuentra en verano.")
elif (mes==3 and dia >=21) or mes==4 or mes==5 or (mes==6 and dia<21):
    if hemisferio ==1:
        print ("Usted se encuentra en primavera.")
    elif hemisferio ==2:
        print ("Usted se encuentra en otoño.")
elif (mes==6 and dia >=21) or mes==7 or mes==8 or (mes==9 and dia<21):
    if hemisferio ==1:
        print ("Usted se encuentra en verano.")
    elif hemisferio ==2: 
        print ("Usted se encuentra en invierno.")
elif (mes==9 and dia >=21) or mes==10 or mes==11 or (mes==12 and dia<21):
    if hemisferio ==1:
        print ("Usted se encuentra en otoño.")
    elif hemisferio ==2:
        print ("Usted se encuentra en primavera.")

#fin