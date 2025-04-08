#10) Escribe un programa que invierta el orden de los 
# dígitos de un número ingresado por el usuario.

num = int(input("Ingrese el sumer al que le quiere invertir el orden: "))
num_inv = 0
#Mientras el numero ingresado sea distinto de 0:
while num != 0 :
    #Obtenemos el ultimo dígito:
    digito = num % 10
    num_inv = 10*num_inv 
    #Sumamos el digito al numero invertido, pero primero lo multiplicamos por 10 para sumarlo en la posicion correcta:
    num_inv = num_inv + digito 
    #Dividimos el numeero original entre 10 sin restos para poder seguir trabajando con el siguiente dígito:
    num = num // 10

print("El numero invertido es: " + str(num_inv))