

#PUNTO 1

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}

precios_frutas['Naranja'] = 1300
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)


#PUNTO 2

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

#PUNTO 3

lista_frutas = precios_frutas.keys()

print(lista_frutas)


#PUNTO 4

contacto_numeros = { }

for i in range(5):
    contacto_temp = str(input("Escribir el nombre del contacto: "))
    num_temp = int(input("Escribir el número del contacto: "))
    contacto_numeros[contacto_temp] = num_temp

print(contacto_numeros)

contacto_buscar = input("Escribir el contacto que desea corroborar número: ")

lista_nombres = list(contacto_numeros.keys())

for i in range(5):
    if contacto_buscar == lista_nombres[i]:
        print(contacto_numeros[contacto_buscar])



#PUNTO 5

lista_palabras = []
recuento = {}

frase = str(input("Ingresar una frase: "))
palabras = frase.split()
longitud = len(palabras)

for i in range(longitud):
    palabra = palabras[i]
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

palabras_unicas = set(palabras)
lista_palabras = list(palabras_unicas)

print("Palabras únicas:", lista_palabras)
print("Recuento de palabras:", recuento)



#PUNTO 6

alumnos = { }
promedio = []

for i in range(3): 
    alumno = str(input("Ingresar nombre del alumno: "))
    nota_uno = int(input("Ingresar primera nota: "))
    nota_dos = int(input("Ingresar segunda nota: "))
    nota_tres = int(input("Ingresar tercera nota: "))
    promedio_alumno = (nota_uno + nota_dos + nota_tres) / 3
    promedio.append(promedio_alumno)
    alumnos[alumno] = (nota_uno, nota_dos, nota_tres)
    
    
print(f"Las notas de cada alumno fueron: {alumnos} ")
print(f"Los promedios de cada alumno fueron: {promedio}")



#PUNTO 7

alumnos_parcial = { }
ambos_parciales = [ ]
un_parcial = [ ]
almenos_uno = []
for i in range(5):
    alumno_nombre = str(input("Ingresar nombre del alumno: "))
    primer_parcial = int(input("Ingresar nota del primer parcial: "))
    segundo_parcial = int(input("Ingresar nota del segundo parcial: "))
    alumnos_parcial[alumno_nombre] = (primer_parcial, segundo_parcial)
    if primer_parcial >= 6 and segundo_parcial >= 6:
        ambos_parciales.append(alumno_nombre)
        almenos_uno.append(alumno_nombre)
    elif primer_parcial >= 6 and segundo_parcial < 6:
        un_parcial.append(alumno_nombre)
        almenos_uno.append(alumno_nombre)
    elif segundo_parcial >= 6 and primer_parcial < 6:
        un_parcial.append(alumno_nombre)
        almenos_uno.append(alumno_nombre)
        

print(f"Las notas resultantes de los alumnos fueron: {alumnos_parcial}")
print(f"Los alumnos que aprobaron ambos parciales fueron: {ambos_parciales}")
print(f"Los alumnos que aprobaron solo un parcial fueron: {un_parcial}")
print(f"Los alumnos que aprobaron al menos un parcial fueron: {almenos_uno}")



#PUNTO 8
productos = { 'pan': 10, 'leche': 5, 'azucar': 8 }

producto_buscar = input("Ingrese el nombre del producto: ").lower()

if producto_buscar in productos:
    print(f"El stock actual de '{producto_buscar}' es {productos[producto_buscar]}")
    agregar_producto = int(input("¿Cuántas unidades desea agregar?: "))
    productos[producto_buscar] += agregar_producto
    print(f"Nuevo stock de '{producto_buscar}': {productos[producto_buscar]}")
else:
    print(f"El producto '{producto_buscar}' no existe.")
    nuevo_stock = int(input("Ingrese el stock inicial para el nuevo producto: "))
    productos[producto_buscar] = nuevo_stock
    print(f"Producto '{producto_buscar}' agregado con stock {nuevo_stock}")

print("Stock actual:", productos)



#PUNTO 9
agenda_horario = {('lunes', '10:00'): 'Reunión', ('martes', '15:00'): 'Clase de inglés'}

dia_agenda = input("Ingrese el día: ").lower()
hora_agenda = input("Ingrese la hora: ")

if (dia_agenda, hora_agenda) in agenda_horario:
    print(f"En {dia_agenda} a las {hora_agenda} tenés: {agenda_horario[(dia_agenda, hora_agenda)]}")
else:
    print(f"No hay actividades registradas en {dia_agenda} a las {hora_agenda}.")



#PUNTO 10

mapeo_original = {
    'Argentina': 'Buenos Aires',
    'Chile': 'Santiago',
    'Brasil': 'Brasilia',
    'Uruguay': 'Montevideo',
    'Perú': 'Lima',
}

mapeo_invertido = {}

for pais in mapeo_original:
    capital = mapeo_original[pais]
    mapeo_invertido[capital] = pais

print("Diccionario original: ", mapeo_original)
print("Diccionario invertido: ", mapeo_invertido)

