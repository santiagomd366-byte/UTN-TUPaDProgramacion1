#PUNTO 1

multiplo_cuatro = list(range(1,100))

for i in range(1, 100):
    if i % 4 == 0:
        print(i)
    else:
        pass

#PUNTO 2

lista_cinco = [23, "hola", -12, "Mendoza", 8]
penultimo_elemento = lista_cinco[-2]
print(penultimo_elemento)

#PUNTO 3

lista_vacia = []

lista_vacia.append(15)
lista_vacia.append("Hola mundo")
lista_vacia.append(83)

print(lista_vacia)

#PUNTO 4

animales = ["perro", "gato", "conejo", "pez"]

animales[-3] = "loro"
animales[-1] = "oso"

print(animales)

#PUNTO 5 

#Lo que hace el programa es eliminar el elemento de mayor valor en una lista, en este caso el 22.

#PUNTO 6

lista_saltos = []

for i in range(10, 31, 5):
    lista_saltos.append(i)

print(lista_saltos)

#PUNTO 7

autos = ["sedan", "polo", "suran", "gol"]

autos[1] = 34
autos[2] = "hola mundo"

print(autos)

#PUNTO 8

dobles= []

dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

print(dobles)

#PUNTO 9

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")

print(compras)

#PUNTO 10

lista_anidada = [[15], [True], [25.5, 57.9, 30.6], [False]]

print(lista_anidada)