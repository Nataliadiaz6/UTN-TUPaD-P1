import sys
sys.setrecursionlimit(20000)

#Funcion iterativa
def factorial(x):
    f = 1
    for i in range (1, x + 1):
        f *= i
    return f

#funcion recursiva
def factorial_recur(x):
    if x == 0:
        return 1
    else:
        return x * factorial_recur(x-1)
    
#hecha mas corto
def factorial_recurs(x):
    #return valor_true if condicion else valor_false
    return 1 if x==0 else x * factorial_recurs( x - 1 )
    
#programa principal
print( factorial(5))
print(factorial_recur(5))
print (factorial_recurs(5))