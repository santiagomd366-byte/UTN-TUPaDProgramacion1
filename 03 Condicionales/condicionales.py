#PUNTO 1
edad_usuario = int(input("Ingresar la edad correspondiente: "))
if edad_usuario >= 18: 
    print("Usted es mayor de edad")
elif edad_usuario <= 0:
    print("Ingresar una edad realista")
else: 
    print ("Usted es menor de edad")

#PUNTO 2
nota_examen = int(input("Ingresar la nota conseguida"))
if nota_examen >= 6:
    print("Aprobaste")
elif nota_examen <= 0:
    print("Ingresar una nota realista")
else:
    print("Desaprobaste")

#PUNTO 3

numero_parimpar = int(input("Ingresar número: "))
if numero_parimpar % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par:")
    numero_parimpar = int(input("Ingresar número: "))

#PUNTO 4

edad_categoria = int(input("Ingresar la edad correspondiente: "))

if edad_categoria < 12:
    print("pertenece a la categoría: Niño/a")
elif edad_categoria >= 12 and edad_categoria < 18:
    print("pertenece a la categoría: Adolescente")
elif edad_categoria >= 18 and edad_categoria < 30:
    print("pertenece a la categoría: Adulto/a jóven")
elif edad_categoria >= 30:
    print("pertenece a la categoría: Adulto/a")
else: print("No pertenece a ninguna categoría")

#PUNTO 5

contraseña_usuario = str(input("Ingresar contraseña: "))

if len(contraseña_usuario) >= 8 and len(contraseña_usuario) <= 14:
    print("Ha ingresado una contraseña correcta")
else: 
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#PUNTO 6 

from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
mean(numeros_aleatorios)
mode(numeros_aleatorios)
median(numeros_aleatorios)

print(numeros_aleatorios)
print("La media es: ", mean(numeros_aleatorios))
print("La moda es: ", mode(numeros_aleatorios))
print("La mediana es: ", median(numeros_aleatorios))

if median(numeros_aleatorios) < mean(numeros_aleatorios) and median(numeros_aleatorios) > mode(numeros_aleatorios):
    print("Hay sesgo positivo")
elif median(numeros_aleatorios) > mean(numeros_aleatorios) and median(numeros_aleatorios) < mode(numeros_aleatorios):
    print("Hay sesgo negativo")
elif median(numeros_aleatorios) == mean(numeros_aleatorios) and median(numeros_aleatorios) == mode(numeros_aleatorios):
    print("No hay sesgo")

#PUNTO 7

texto_usuario = str(input("Ingresar una frase o palabra: "))
ultima_letra = texto_usuario[-1]

if texto_usuario[-1].lower() in "aeiou":
   texto_usuario += "!"
   print(texto_usuario)
else: 
    print (texto_usuario)

#PUNTO 8

nombre_opciones = str(input("Ingresar nombre: "))
numero_opciones = int(input("1: nombre en mayúsculas 2: nombre en minúsculas 3: nombre con solo la primera letra mayúscula"))
if numero_opciones == 1:
    print(nombre_opciones.upper())
elif numero_opciones == 2:
    print(nombre_opciones.lower())
elif numero_opciones == 3:
    print(nombre_opciones.title())
else: 
    print("Ingresar un número de las opciones establecidas")
    numero_opciones = int(input("1: nombre en mayúsculas 2: nombre en minúsculas 3: nombre con solo la primera letra mayúscula"))

#PUNTO 9 

magnitud_terre = float(input("Ingresar la magnitud del terremoto: "))
if magnitud_terre < 3:
    print("Resultado: Muy leve (Imperceptible)")
elif magnitud_terre >= 3 and magnitud_terre < 4:
    print("Resultado: Leve (ligeramente perceptible)")
elif magnitud_terre >= 4 and magnitud_terre < 5:
    print("Resultado: Moderado (sentido por personas, pero generalmente no causa daño)")
elif magnitud_terre >= 5 and magnitud_terre < 6:
    print("Resultado: Fuerte(puede causar daño en estructuras libres)")
elif magnitud_terre >=6 and magnitud_terre < 7:
    print("Resultado: Muy Fuerte(puede causar daños significativos)")
elif magnitud_terre <= 7:
    print("Extremo(puede causar graves daños a gran escala)")

#PUNTO 10

hemisferio_ns = str(input("Ingresar el hemisferio donde se encuentra (N / Norte) (S / Sur): ")) 
if hemisferio_ns not in "nNsS":
    print("Hemisferio ingresado incorrecto")
    hemisferio_ns = str(input("Ingresar el hemisferio donde se encuentra (N / Norte) (S / Sur): "))

dia_año = int(input("Ingresar el día del año: "))
mes_año = int(input("Ingresar mes del año (en numérico): "))

estacion_rango = None  

if mes_año >= 1 and mes_año <= 12:
    if mes_año == 12:
        if dia_año >= 21:
            estacion_rango = 89
        else:
            estacion_rango = 356
    elif mes_año == 1 or mes_año == 2:
        estacion_rango = 89
    elif mes_año == 3:
        if dia_año >= 21:
            estacion_rango = 178
        else:
            estacion_rango = 89
    elif mes_año == 4 or mes_año == 5:
        estacion_rango = 178
    elif mes_año == 6:
        if dia_año >= 21:
            estacion_rango = 257
        else:
            estacion_rango = 178
    elif mes_año == 7 or mes_año == 8:
        estacion_rango = 257
    elif mes_año == 9:
        if dia_año >= 21:
            estacion_rango = 356
        else:
            estacion_rango = 257
    elif mes_año == 10 or mes_año == 11:
        estacion_rango = 356

if estacion_rango is None:
    print("No se pudo determinar la estación con los datos ingresados.")
else:
    if estacion_rango == 89:
        if hemisferio_ns in "nN":
            print("El usuario se encuentra en invierno")  
        elif hemisferio_ns in "sS":
            print("El usuario se encuentra en verano")
    elif estacion_rango == 178:       
        if hemisferio_ns in "nN":
            print("El usuario se encuentra en primavera")
        else: 
            print("El usuario se encuentra en otoño")
    elif estacion_rango == 257:
        if hemisferio_ns in "nN":
            print("El usuario se encuentra en verano")
        else:
            print("El usuario se encuentra en invierno")
    elif estacion_rango == 356:
        if hemisferio_ns in "nN":
            print("El usuario se encuentra en otoño")
        else:
            print("El usuario se encuentra en primavera")

    