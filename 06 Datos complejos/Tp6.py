# TP 6 - Datos Complejos
# Natalia Diaz - Comisión 7

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}

#1
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

#2
precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800
print(precios_frutas)

#3
print(precios_frutas.keys())

#4
#Cargar contactos por pantalla
def programa_telefonos():
    contactos = {}
    for i in range(5):
        while True:
            nombre = input(f"Ingresa el nombre del contacto {i+1}: ").strip() #strip elimina espacios en blanco
            if nombre:  # Asegura que el nombre no esté vacío
                break
            else:
                print("El nombre no puede estar vacío. Por favor, intenta de nuevo.")
        
        while True:
            numero = input(f"Ingresa el número de teléfono de {nombre}: ").strip()
            if numero.isdigit() and len(numero) > 0: # Valida que sea un número y no esté vacío
                break
            else:
                print("El número de teléfono debe contener solo dígitos y no puede estar vacío. Por favor, intenta de nuevo.")
        
        contactos[nombre] = numero
        print(f"Contacto '{nombre}' agregado exitosamente.")
    
    # 2. Pedir un nombre y mostrar el número asociado
    while True:
        nombre_buscar = input("Ingresa el nombre del contacto que deseas buscar, ingrese 'salir' para terminar: ").strip()
        
        if nombre_buscar.lower() == 'salir':
            print("¡Hasta luego!")
            break
        
        if nombre_buscar in contactos:
            print(f"El número de teléfono de '{nombre_buscar}' es: {contactos[nombre_buscar]}")
        else:
            print(f"El contacto '{nombre_buscar}' no se encontró en la lista.")

if __name__ == "__main__":
    programa_telefonos()

#5
def analizar_frase():
    # Solicitar la frase al usuario
    frase = input("Por favor, ingresa una frase: ")
    
    # Preprocesar la frase: convertir a minúsculas y dividir en palabras
    # Usamos .lower() para que "Hola" y "hola" se traten como la misma palabra.
    # Usamos .split() para dividir la frase en una lista de palabras, separando por espacios.
    palabras = frase.lower().split()
    
    # Encontrar las palabras únicas usando un set
    palabras_unicas = set(palabras)
    
    # Contar la cantidad de veces que aparece cada palabra (usando un diccionario)
    recuento_palabras = {}
    for palabra in palabras:
        # Si la palabra ya está en el diccionario, incrementa su contador.
        # Si no, la añade con un contador de 1.
        recuento_palabras[palabra] = recuento_palabras.get(palabra, 0) + 1
        
    # Imprimir los resultados
    print(f"Palabras_únicas: {palabras_unicas}")
    print(f"Recuento: {recuento_palabras}")

if __name__ == "__main__":
    analizar_frase()

#6
def calcular_promedios_alumnos():
    alumnos = {}

    # Ingresar los nombres de 3 alumnos y sus notas
    for i in range(3):
        while True:
            nombre_alumno = input(f"Ingresa el nombre del alumno {i+1}: ").strip()
            if nombre_alumno:
                break
            else:
                print("El nombre del alumno no puede estar vacío. Intenta de nuevo.")

        notas = []
        print(f"Ingresa las 3 notas para {nombre_alumno}:")
        for j in range(3):
            while True:
                try:
                    nota = float(input(f"  Nota {j+1}: "))
                    if 0 <= nota <= 10: # Asumiendo notas de 0 a 10
                        notas.append(nota)
                        break
                    else:
                        print("La nota debe estar entre 0 y 10.")
                except ValueError:
                    print("Entrada inválida. Por favor, ingresa un número para la nota.")
        
        # Almacenar las notas como una tupla
        alumnos[nombre_alumno] = tuple(notas)
        print(f"Notas de {nombre_alumno} guardadas: {alumnos[nombre_alumno]}\n")

    # 2. Mostrar el promedio de cada alumno
    for nombre, notas_tuple in alumnos.items():
        # Calcular el promedio: suma de notas dividida por la cantidad de notas
        promedio = sum(notas_tuple) / len(notas_tuple)
        print(f"El promedio de {nombre} es: {promedio:.2f}") # Formatear a 2 decimales

if __name__ == "__main__":
    calcular_promedios_alumnos()

#7
def analizar_aprobados():
    aprobados_parcial1 = {"Nico", "Vale", "Diego", "Nati", "Sole", "Ines"}
    aprobados_parcial2 = {"Nemi", "Sole", "Nati", "Dante", "Evi", "Lorenzo", "Ines"}

    # Los que aprobaron ambos parciales (&)
    ambos_parciales = aprobados_parcial1.intersection(aprobados_parcial2)
    print(f"Estudiantes que aprobaron ambos parciales: {ambos_parciales}")

    # Los que aprobaron solo uno de los dos (^)
    solo_un_parcial = aprobados_parcial1.symmetric_difference(aprobados_parcial2)
    print(f"Estudiantes que aprobaron solo un parcial: {solo_un_parcial}")

    # Los que aprobaron al menos un parcial (|)
    total_aprobados = aprobados_parcial1.union(aprobados_parcial2)
    print(f"Estudiantes que aprobaron al menos un parcial: {total_aprobados}")

if __name__ == "__main__":
    analizar_aprobados()

#8
def gestionar_stock():
    stock_productos = {'Banana': 1330, 'Anana': 2500, 'Melon': 2800, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1700, 'Pera': 2300}
    # Elegir que hacer
    while True:
        print("\nOpciones:")
        print("1. Consultar stock de un producto")
        print("2. Agregar unidades a un producto existente / Agregar nuevo producto")
        print("3. Salir")
        opcion = input("Elige una opción (1-3): ").strip()

        if opcion == '1':
            # Consultar stock
            producto_consulta = input("Ingresa el nombre del producto a consultar: ").strip().capitalize()
            if producto_consulta in stock_productos:
                print(f"El stock de '{producto_consulta}' es: {stock_productos[producto_consulta]} unidades.")
            else:
                print(f"El producto '{producto_consulta}' no se encuentra en el stock.")
        
        elif opcion == '2':
            # Agregar unidades o nuevo producto
            producto_modificar = input("Ingresa el nombre del producto: ").strip().capitalize()
            
            while True:
                try:
                    cantidad = int(input("Ingresa la cantidad de unidades a agregar: "))
                    if cantidad > 0:
                        break
                    else:
                        print("La cantidad debe ser un número positivo. Intenta de nuevo.")
                except ValueError:
                    print("Entrada inválida. Por favor, ingresa un número entero para la cantidad.")

            if producto_modificar in stock_productos:
                # El producto existe, agregar unidades
                stock_productos[producto_modificar] += cantidad
                print(f"Se agregaron {cantidad} unidades a '{producto_modificar}'. Nuevo stock: {stock_productos[producto_modificar]}.")
            else:
                # El producto no existe, agregarlo como nuevo
                stock_productos[producto_modificar] = cantidad
                print(f"Producto '{producto_modificar}' agregado con {cantidad} unidades.")
    
        elif opcion == '3':
            print("Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige un número del 1 al 3.")

if __name__ == "__main__":
    gestionar_stock()

#9
def gestionar_agenda():
    agenda_facu_c7 = {
        ("lunes", "15:00"): "Matematica",
        ("martes", "15:00"): "Organización empresarial",
        ("miercoles", "14:00"): "Programación",
        ("miercoles", "15:00"): "Arq y Sist. Operativos",
        ("jueves", "14:00"): "Arq y Sist. Operativos",
        ("jueves", "15:00"): "Matemática",
        ("viernes", "16:00"): "Organizacion empresarial",
        ("viernes", "17:00"): "Programación"
    }

    print("Horarios de clases de la comisión 7:")
    for (dia, hora), evento in agenda_facu_c7.items():
        print(f"  {dia.capitalize()} a las {hora}: {evento}")


    while True:
        print("\nOpciones:")
        print("1. Consultar una clase en un día y hora específicos")
        print("2. Salir")

        opcion = input("Elige una opción (1-2): ").strip()

        if opcion == '1':
            # Consultar evento
            dia_consulta = input("Ingresa el día: ").strip().lower()
            hora_consulta = input("Ingresa la hora: ").strip()

            clave_busqueda = (dia_consulta, hora_consulta)

            if clave_busqueda in agenda_facu_c7:
                print(f"La clase para el {dia_consulta.capitalize()} a las {hora_consulta} es: '{agenda_facu_c7[clave_busqueda]}'.")
            else:
                print(f"No hay clase programada para el {dia_consulta.capitalize()} a las {hora_consulta}.")
        
        elif opcion == '2':
            print("Hasta luego!")
            break
        
        else:
            print("Opción no válida. Por favor ingrese 1 o 2.")

if __name__ == "__main__":
    gestionar_agenda()

#10

def invertir_diccionario_capitales():
    original = {
        "Argentina": "Buenos Aires",
        "Chile": "Santiago",
        "EEUU": "Washintong",
        "Brasil": "Brasilia",
        "Peru": "Lima",
    }
    print(f"Diccionario original: {original}")

    # Construir el diccionario invertido
    invertido = {}
    
    # Iterar sobre los pares key-value (país, capital) del diccionario original
    for pais, capital in original.items():
        # Asignar la capital como nueva key y el país como nuevo value
        invertido[capital] = pais
    
    print(f"Diccionario invertido: {invertido}")

if __name__ == "__main__":
    invertir_diccionario_capitales()