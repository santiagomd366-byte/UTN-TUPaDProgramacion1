
#PUNTO 1
from statistics import mode, median, mean 

listas_estudiantes = []
for i in range (10):
    nota = float(input("Ingresar nota del estudiante: "))
    listas_estudiantes.append(nota)

print(listas_estudiantes)
mean(listas_estudiantes)

print(mean(listas_estudiantes))

max_valor = max(listas_estudiantes)
min_valor = min(listas_estudiantes)

print(max_valor)
print(min_valor)


#PUNTO 2

lista_producto = []

for i in range(5):
    producto = input("Ingresar producto: ")
    lista_producto.append(producto)

productos_ordenados = sorted(lista_producto)

producto_eliminar = input("¿Que producto desea eliminar?: ")
for i in range(5):
   if producto_eliminar == lista_producto[i]:
       producto_nuevo = input("Nombrar nuevo producto: ")
       lista_producto[i] = producto_nuevo

print(lista_producto)
       

#PUNTO 3

import random 

random_lista = []
par = []
impar = []
random_num = 0
for i in range(15):
   random_num = random.randint(1,100)
   random_lista.append(random_num)

for i in range(15):
   if random_lista[i] % 2 == 0:
      num_temp = random_lista[i]
      par.append(num_temp)
   else:
      num_temp = random_lista[i]
      impar.append(num_temp) 


longitud_par = len(par)
longitud_impar = len(impar)

print(impar)
print("La cantidad de valores de la lista de impares es de: ", longitud_impar)
print(par)
print("La cantidad de valores de la lista de pares es de: ", longitud_par)

#PUNTO 4

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]

sin_duplicados = list(set(datos))

print(sin_duplicados)


#PUNTO 5

presentes = ["santiago", "julio", "cesar", "miguel", "manuel", "tiago", "tomi", "fran"]
dato_estudiante = 0
dato_estudiante = int(input("¿Desea agregar o eliminar a algún estudiante? 0:Agregar 1:Eliminar"))

if dato_estudiante == 0:
   nuevo_estudiante = input("Ingresar nuevo estudiante: ")
   presentes.append(nuevo_estudiante)

elif dato_estudiante == 1:
   print(presentes)
   eliminar_estudiante = input("¿Que estudiante desea eliminar?: ")
   for i in range(len(presentes)):
      if eliminar_estudiante == presentes[i]:
         presentes.remove(eliminar_estudiante)
         break


print(presentes)

#PUNTO 6
lista_rotar = [1, 2, 3, 4, 5, 6, 7]
ultimo = 7

for i in range(len(lista_rotar)-1, 0, -1):
    lista_rotar[i] = lista_rotar[i-1]
   

lista_rotar[0] = ultimo
print(lista_rotar)
#PUNTO 7
