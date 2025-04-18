#TP4 - NATALIA DIAZ - COMISION 7

#1- imprimir_hola_mundo
#Definicion de funciones
def imprimir_hola_mundo():
    return print("Hola Mundo!")

#Programa principal
imprimir_hola_mundo()

#2- saludar_usuario(nombre)
#Definicion de funciones
def saludar_usuario(nombre):
    return print(f"Hola {nombre}!")

#Programa principal
nombre= input("Ingrese su nombre: ")
saludar_usuario(nombre)

#3-informacion_personal(nombre, apellido, edad, residencia)
#Definicion de funciones
def informacion_personal(nombre, apellido,edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

#Programa principal
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")

informacion_personal(nombre, apellido,edad, residencia)

#4-calcular_area_circulo(radio) y  calcular_perimetro_circulo(radio)
#Definicion de funciones
import math
def calcular_area_circulo(radio):
    area = math.pi * radio**2
    return print(f"El area del circulo es {area}")

def calcular_perimetro_circulo(radio):
    perimetro = math.pi * radio * 2
    return print(f"El perimetro del circulo es {perimetro}")

#Programa principal
radio = int(input("Ingrese el radio del circulo: "))
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)

#5- segundos_a_horas(segundos)
#Definicion de funciones
def segundos_a_horas(segundos):
    horas = segundos / 3600
    return print(f"{segundos} segundos equivalen a {horas} hora/s.")

#Programa principal
segundos = int(input("Ingrese los segundos: "))
segundos_a_horas(segundos)

#6-tabla_multiplicar(numero) 
#Definicion de funciones
def tabla_multiplicar(numero):
    
    for i in range(0, 11):
        mult = numero * i 
        print(f"{numero} x {i} = {mult}")

#Programa principal
numero = int(input("Ingrese el numero del cual desea saber su tabla del 1 al 10:"))
tabla_multiplicar(numero)

#7-operaciones_basicas(a, b)
#Definicion de funciones
def operaciones_basicas(a, b):
    print(f"{a} + {b} =", a + b)
    print(f"{a} - {b} =", a - b)
    print(f"{a} / {b} =", a / b)
    print(f"{a} * {b} =", a * b)

#Programa principal
a = int(input("Ingrese el primer número:"))
b = int(input("Ingrese el segundo número:"))
operaciones_basicas(a,b)

#8-calcular_imc(peso, altura)
#Definicion de funciones
def calcular_imc(peso, altura):
    imc = peso / (altura**2)
    return print(f"Su índice de masa corporal (IMC) es de", round(imc, 2))

#Programa principal
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
calcular_imc(peso, altura)

#9- celsius_a_fahrenheit(celsius)
#Definicion de funciones
def celsius_a_fahrenheit(celsius):
    farhenheit = (celsius * 1.8) + 32
    return print(f"{celsius} grados celsius equivalen a {farhenheit} grados farhenheit.")

#Programa principal
celsius = float(input("Ingrese los grados celsius que desea pasar a grados farhenheit: "))
celsius_a_fahrenheit(celsius)

#10-calcular_promedio(a, b, c) 
#Definicion de funciones
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return print(f"El promedio de los numeros ingresados es {promedio}.")

#Programa principal
a = float(input("Ingrese el primer numero: "))
b = float(input("Ingrese el segundo numero: "))
c = float(input("Ingrese el tercer numero: "))
calcular_promedio(a, b, c)