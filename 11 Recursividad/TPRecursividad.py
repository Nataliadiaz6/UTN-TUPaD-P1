#1
#El factorial de un entero positivo n, se define como el producto 
# de todos los números enteros positivos desde 1 hasta n.

def factorial_recursivo(n):
    if n == 0: #Caso base
        return 1
    else:
        return n * factorial_recursivo(n - 1)

def mostrar_factoriales(num):
    if num < 1:
        print("El numero ingresado debe ser mayor o igual a 1.")
        return

    for i in range(1, num + 1):
        factorial = factorial_recursivo(i)
        print(f"El factorial de {i} es: {factorial}")

numero = int(input("Ingrese un número mayor o igual a 1: "))

mostrar_factoriales(numero)

#2
#La serie de Fibonacci se trata de una secuencia de números,
# de manera que cada número es igual a la suma de sus dos anteriores.
def fibonacci_recursivo(pos):
    if pos==0: #caso base
        return 0
    elif pos==1: #caso base
        return 1
    else:
        return fibonacci_recursivo(pos-1)+fibonacci_recursivo(pos-2)
    
def mostrar_serie(n):
    if n < 1:
        print("El numero ingresado debe ser mayor o igual a 1.")
        return

    print(f"La sucesión de Fibonacci hasta la posición {n} es: ")
    for i in range(1, n + 1):
        valor = fibonacci_recursivo(i)
        print(f"Posición {i}: {valor}")

pos = int(input("Ingrese la posición hasta la que desea ver la serie de Fibonacci: "))

mostrar_serie(pos)

#3
#𝑛^𝑚 = 𝑛 ∗ 𝑛^(𝑚−1)
def potencia_recursiva(n, m):
    if m == 0:
        return 1
    elif m < 0:
        return 1 / potencia_recursiva(n, -m)
    else:
        return n * potencia_recursiva(n, m - 1)

#Algoritmo

n = float(input("Ingrese n: "))
m = int(input("Ingrese m: "))

resultado = potencia_recursiva(n, m)
print(f"{n} elevado a la {m} es igual a {resultado}")

#4
def decimal_a_binario_recursivo(n):
    if n == 0:
        return ""
    else:
        resto = n % 2
        cociente = n // 2
        return decimal_a_binario_recursivo(cociente) + str(resto)

n = int(input("Ingrese el numero decimal que desea pasar a binario: "))
binario=(decimal_a_binario_recursivo(n))
print(f"El número decimal {n} en binario es: {binario}")

#5
#Palíndromo: Palabra o frase cuyas letras están dispuestas de tal manera que 
# resulta la misma leída de izquierda a derecha que de derecha a izquierda.
def palindromo(palabra):
    palabra = palabra.lower() #paso a minusculas

    if len(palabra) <= 1:
        return True
    elif palabra[0] == palabra[-1]:
        return palindromo(palabra[1:-1])
    else:
        return False
    
palabra = input("Ingrese una palabra y te diré si es un palíndromo: ")

if palindromo(palabra):
    print(f"'{palabra}' es un palíndromo.")
else:
    print(f"'{palabra}' no es un palíndromo.")

#6
def suma(n):
    if n == 0:
        return 0
    else:
        ult_digito = n % 10
        numero_restante = n // 10
        return ult_digito + suma(numero_restante)

#Con un numero ingresado por el usuario:
n = int(input("Ingrese un número entero positivo: "))
if (n < 0):
    print("El número ingresado debe ser positivo.")
else:
    total = suma(n)
    print(f"La suma de los dígitos de {n} es: {total}")



#7
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)
    
#Con un numero ingresado por el usuario:

n = int(input("Ingrese el número de bloques del nivel más bajo: "))
if n < 1:
    print("El número ingresado debe ser mayor o igual a 1.")
else:
    total = contar_bloques(n)
    print(f"Para una pirámide con una base de {n} bloques, se necesitan {total} bloques.")


#8
def rep_digito(num, digito):
    if num == 0:
        if digito == 0:
            return 1
        else:
            return 0
    else:
        ult_digito = num % 10
        numero_rest = num // 10
        if ult_digito == digito:
            contador = 1
        else:
            contador = 0
        return contador + rep_digito(numero_rest, digito)

#Con un numero ingresado por el usuario:
num= int(input("Ingrese un número: "))
digito= int(input("Ingrese el dígito que quieres ver cuantas veces se repite: "))

if (digito or num) < 0:
    print("Los valores ingresados deben ser positivos")
else:
    print(f"El dígito {digito} se repite {rep_digito(num, digito)} veces en el número {num}.")