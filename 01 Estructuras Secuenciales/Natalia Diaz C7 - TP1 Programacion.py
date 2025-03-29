#NATALIA DIAZ - Comision 7

#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo")

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado.
nombre= input("Ingrese su nombre: ")
print (f"Hola {nombre}" "!")

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. 
nombre= input("Ingrese su nombre: "),
apellido= input("Ingrese su apellido: "),
edad= input("Ingrese su edad: "),
residencia= input("Ingrese su lugar de residencia: "),
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.
radio= float(input("Por favor, ingrese el radio del circulo: "))
pi= 3.1416
area= pi * radio ** 2
perimetro= 2 * pi * radio
print (f"El área del círculo es {area} y el periímetro del círculo es {perimetro}")

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.
segundos= float(input("Ingrese la cantidad de segundos que desea pasar a horas: "))
horas= segundos / 3600
print (f"{segundos} segundos equivalen a {horas} hora/s.")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.
n= int(input("Ingrese el numero del cual desea saber su tabla (debe ser un numero entero positivo): "))
if n > 0:
    for i in range(1,11):
        print (n, "x", i, " = ", n*i)
else:
    print( "El número ingresado no es correcto")

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
a= float(input("Ingrese el primer numero: "))
b= float(input("Ingrese el segundo numero: "))
suma= a+b
resta= a-b
division= a/b
multiplicacion= a*b
print(f"la suma de {a} + {b} es igual a {suma}, la resta de {a} - {b} es igual a {resta}, la division a {a} / {b} es igual a {division}, la multiplicacion de {a} * {b} es igual a {multiplicacion}")

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal
peso= float(input("Ingrese su peso en kilogramos: "))
altura= float(input("Ingrese su altura en metros: "))
imc= peso / (altura**2)
print("Su índice de masa corporal es", imc)

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. 
c= float(input("Ingrese una temperatura en grados Celcius: "))
f= c * 1.8 + 32
print(f"{c} grados Celcius son equivalentes a {f} grados Fahrenheit")

#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.
n1= float(input("Ingrese el primer número: "))
n2= float(input("Ingrese el segundo número: "))
n3= float(input("Ingrese el tercer número: "))
p= (n1 + n2 + n3) / 3
print ("El promedio de los tres numeros ingresados es: ", p)

#Saludos!